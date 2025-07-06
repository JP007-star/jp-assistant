import os
import json
import pyttsx3
import pyaudio
from vosk import Model, KaldiRecognizer

engine = pyttsx3.init()

# ✅ Text to speech (offline)
def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"[TTS Error] {e}")

# ✅ Offline speech recognition with Vosk
def listen():
    mic = None
    stream = None
    
    try:
        mic = pyaudio.PyAudio()

        print("🎤 Available Microphones:")
        for i in range(mic.get_device_count()):
            info = mic.get_device_info_by_index(i)
            print(f"{i}: {info['name']}")

        # Try to find a suitable default microphone if index 18 isn't available
        try:
            mic_index = int(input("Enter microphone index: "))  # Let user choose
            mic_info = mic.get_device_info_by_index(mic_index)
            if mic_info['maxInputChannels'] < 1:
                raise ValueError("Selected device is not an input device")
        except (ValueError, OSError) as e:
            print(f"Invalid microphone selection: {e}")
            # Try to find the default input device
            mic_index = mic.get_default_input_device_info()['index']
            print(f"Using default microphone at index {mic_index}")

        model = Model("models/vosk-model-small-en-in-0.4")
        if not model:
            raise RuntimeError("Failed to load Vosk model")

        recognizer = KaldiRecognizer(model, 16000)
        if not recognizer:
            raise RuntimeError("Failed to initialize recognizer")

        stream = mic.open(format=pyaudio.paInt16, 
                         channels=1,
                         rate=16000, 
                         input=True, 
                         input_device_index=mic_index,
                         frames_per_buffer=8192)
        
        print("🎧 Speak now (English)...")
        stream.start_stream()

        max_silent_loops = 30  # About 3 seconds of silence
        silent_loops = 0
        
        while True:
            data = stream.read(4000, exception_on_overflow=False)
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result.get("text", "").strip()
                if text:
                    print(f"🟢 [Vosk] Transcript: {text}")
                    return text
                else:
                    silent_loops += 1
                    if silent_loops >= max_silent_loops:
                        return "🤔 Couldn't catch anything clearly."
            else:
                partial = json.loads(recognizer.PartialResult())
                if partial.get("partial", "").strip():
                    silent_loops = 0  # Reset counter if we're getting partial results

    except Exception as e:
        print(f"❌ Error in offline listen(): {e}")
        return f"❌ Error: {str(e)}"
    finally:
        if stream:
            try:
                stream.stop_stream()
                stream.close()
            except:
                pass
        if mic:
            try:
                mic.terminate()
            except:
                pass