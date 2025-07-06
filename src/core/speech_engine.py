"""
Speech Engine Module - Handles speech recognition and text-to-speech
"""

import speech_recognition as sr
import pyttsx3
from typing import Optional
from . import config

class SpeechEngine:
    """Handles speech recognition and text-to-speech functionality"""
    
    def __init__(self):
        """Initialize speech recognition and TTS engine"""
        self.recognizer = sr.Recognizer()
        self.tts_engine = pyttsx3.init()
        self.microphone = None
        self.setup_tts()
        self.setup_microphone()
    
    def setup_tts(self) -> None:
        """Configure text-to-speech settings"""
        try:
            voices = self.tts_engine.getProperty('voices')
            if voices:
                # Use female voice if available
                for voice in voices:
                    if 'female' in voice.name.lower() or 'zira' in voice.name.lower():
                        self.tts_engine.setProperty('voice', voice.id)
                        break
            
            self.tts_engine.setProperty('rate', config.TTS_RATE)
            self.tts_engine.setProperty('volume', config.TTS_VOLUME)
        except Exception as e:
            print(f"⚠️ TTS setup warning: {e}")
    
    def setup_microphone(self) -> bool:
        """Setup and calibrate microphone"""
        try:
            self.microphone = sr.Microphone(device_index=config.MICROPHONE_INDEX)
            
            # Calibrate for ambient noise
            print("🎤 Calibrating microphone for ambient noise...")
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(
                    source, 
                    duration=config.AMBIENT_NOISE_DURATION
                )
            
            print(f"✅ Microphone {config.MICROPHONE_INDEX} ready!")
            return True
            
        except Exception as e:
            print(f"❌ Microphone setup failed: {e}")
            return False
    
    def speak(self, text: str) -> None:
        """Convert text to speech"""
        try:
            print(f"🤖 JP: {text}")
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        except Exception as e:
            print(f"⚠️ TTS Error: {e}")
            print(f"🤖 JP: {text}")  # Fallback to text only
    
    def listen(self, wake_word_mode: bool = False) -> str:
        """Listen for speech and convert to text"""
        if not self.microphone:
            return ""
        
        timeout = config.WAKE_WORD_TIMEOUT if wake_word_mode else config.TIMEOUT_SECONDS
        
        try:
            with self.microphone as source:
                if wake_word_mode:
                    print("💤 Sleeping... Say 'Hey JP' to wake me up")
                else:
                    print("🎤 Listening... (speak now)")
                
                # Listen for audio
                audio = self.recognizer.listen(
                    source, 
                    timeout=timeout,
                    phrase_time_limit=config.PHRASE_TIME_LIMIT
                )
                
                if not wake_word_mode:
                    print("🔄 Processing speech...")
                
                # Convert to text using Google Speech Recognition
                text = self.recognizer.recognize_google(audio)
                
                if wake_word_mode:
                    print(f"🔍 Heard: {text}")
                else:
                    print(f"👤 You: {text}")
                    
                return text.lower()
                
        except sr.WaitTimeoutError:
            if not wake_word_mode:
                print(config.ERROR_MESSAGES["speech_timeout"])
            return ""
        except sr.UnknownValueError:
            if not wake_word_mode:
                print(config.ERROR_MESSAGES["speech_unclear"])
            return ""
        except sr.RequestError as e:
            print(f"❌ Speech service error: {e}")
            return ""
        except Exception as e:
            print(f"{config.ERROR_MESSAGES['general_error']}: {e}")
            return ""
    
    def is_ready(self) -> bool:
        """Check if speech engine is ready"""
        return self.microphone is not None
