"""
JP Assistant - Enhanced Voice-Activated AI Assistant
Main application module
"""

import os
import sys
import threading
import time
from typing import Optional
from core import config
from core.jp_config import *
from core.speech_engine import SpeechEngine
from core.command_processor import CommandProcessor
from core.jp_brain import JPBrain, SmartMonitoring

class JPAssistant:
    """Enhanced JP Voice Assistant"""
    
    def __init__(self):
        """Initialize the enhanced assistant"""
        self.speech_engine: Optional[SpeechEngine] = None
        self.command_processor: Optional[CommandProcessor] = None
        self.jp_brain: Optional[JPBrain] = None
        self.monitoring: Optional[SmartMonitoring] = None
        self.running = False
        self.awake = True  # Start awake
        self.always_listening = ALWAYS_LISTENING
        
        # Initialize components
        self.initialize()
    
    def initialize(self) -> bool:
        """Initialize all enhanced components"""
        print(f"🚀 Initializing Enhanced {ASSISTANT_NAME}...")
        print("═" * 40)
        
        try:
            # Initialize speech engine
            print("🎤 Loading speech systems...")
            self.speech_engine = SpeechEngine()
            if not self.speech_engine.is_ready():
                print("❌ Speech engine initialization failed")
                return False
            print("✅ Speech systems online")
            
            # Initialize command processor
            print("🧠 Loading command processor...")
            self.command_processor = CommandProcessor()
            print("✅ Command processor ready")
            
            # Initialize JP brain
            print("🔮 Loading JP intelligence...")
            self.jp_brain = JPBrain()
            print("✅ JP brain online")
            
            # Initialize smart monitoring
            if ADVANCED_FEATURES["proactive_assistance"]:
                print("👁️ Activating smart monitoring...")
                self.monitoring = SmartMonitoring(self.jp_brain)
                print("✅ Smart monitoring active")
            
            print("═" * 40)
            print("🎯 All enhanced systems operational!")
            return True
            
        except Exception as e:
            print(f"❌ Initialization failed: {e}")
            return False
    
    def display_welcome(self) -> None:
        """Display enhanced welcome interface"""
        print("\n" + "═"*65)
        print(f"🤖 {ASSISTANT_NAME} - Enhanced AI Assistant")
        print("═"*65)
        print("🎯 Status: All enhanced systems operational")
        print("🎤 Voice Control: Always listening mode active")
        print("🧠 AI Mode: Smart intelligence online")
        print("👁️ Monitoring: Smart assistance active")
        print("")
        print("💬 Enhanced Voice Commands:")
        print("   🎙️ 'Hey JP' or 'JP' - Get attention")
        print("   📊 'System scan' - Complete analysis")
        print("   ⚡ 'Optimize system' - Smart optimization")
        print("   🧠 'Smart assistance' - AI recommendations")
        print("   📚 'Learn from me' - Adaptive learning")
        print("   💡 'What should I do?' - Smart suggestions")
        print("   😴 'Sleep' or 'Bye JP' - Standby mode")
        print("─"*65)
    
    def display_commands(self) -> None:
        """Display available commands"""
        print("\n🎯 Quick Command Examples:")
        print("   🕐 'What time is it?' | 'What's today's date?'")
        print("   💻 'Check system status' | 'What's my CPU usage?'")
        print("   📁 'List files' | 'Find MP3 files'")
        print("   🚀 'Open calculator' | 'Open browser'")
        print("   🔍 'Search for Python tutorials'")
        print("   🧠 'Remember my birthday is June 15th'")
        print("   😄 'Tell me a joke'")
        print("   ❓ 'Help' | 'What can you do?'")
        print("-"*60)
    
    def check_jp_attention(self, text: str) -> bool:
        """Check if user is addressing JP"""
        text = text.lower().strip()
        
        # Check for exact matches first
        for wake_word in WAKE_WORDS:
            if wake_word in text:
                print(f"✅ JP attention detected: '{wake_word}' in '{text}'")
                return True
        
        # Check for attention words
        for attention_word in ATTENTION_WORDS:
            if attention_word in text:
                print(f"✅ Attention word detected: '{attention_word}' in '{text}'")
                return True
            
        return False
    
    def check_sleep_word(self, text: str) -> bool:
        """Check if text contains sleep word"""
        text = text.lower().strip()
        
        for sleep_word in SLEEP_WORDS:
            if sleep_word in text:
                print(f"✅ Sleep word detected: '{sleep_word}' in '{text}'")
                return True
        
        return False
    
    def process_jp_command(self, command: str) -> str:
        """Process command with JP intelligence"""
        # First try JP brain for enhanced commands
        jp_response = self.jp_brain.process_enhanced_command(command)
        
        if jp_response:
            return jp_response
        
        # Fall back to standard command processing
        standard_response = self.command_processor.process_command(command)
        
        # Enhance with JP personality
        return self.jp_brain.personality.personalize_response(
            "acknowledgment",
            standard_response
        )
    
    def run(self) -> None:
        """Main application loop"""
        if not self.speech_engine or not self.command_processor:
            print("❌ Cannot start - initialization failed")
            return
        
        # Display enhanced interface
        self.display_welcome()
        
        # Start smart monitoring if enabled
        if self.monitoring and ADVANCED_FEATURES["proactive_assistance"]:
            self.monitoring.start_monitoring()
        
        # Enhanced greeting
        greeting = self.jp_brain.personality.personalize_response("greeting")
        self.speech_engine.speak(greeting)
        
        self.running = True
        
        # Main interaction loop
        while self.running:
            try:
                if not self.awake:
                    # Wake word detection mode
                    user_input = input("\n💤 Say 'Hey JP' to wake up (or press ENTER/type 'quit'): ").strip()
                    
                    # Handle manual input
                    if user_input.lower() == 'quit':
                        self.shutdown()
                        break
                    elif user_input.lower() == 'help':
                        print(config.HELP_TEXT)
                        continue
                    elif user_input:  # Manual command
                        response = self.command_processor.process_command(user_input)
                        self.speech_engine.speak(response)
                        continue
                    
                    # Listen for JP attention
                    wake_input = self.speech_engine.listen(wake_word_mode=True)
                    if wake_input:
                        if self.check_jp_attention(wake_input):
                            self.awake = True
                            acknowledgment = self.jp_brain.personality.personalize_response(
                                "acknowledgment", "Yes, I'm here! How can I help?"
                            )
                            self.speech_engine.speak(acknowledgment)
                            continue
                        else:
                            # Continue listening for attention
                            continue
                    
                else:
                    # Active listening mode
                    print("\n🎤 I'm awake! Say something (or 'Bye JP' to sleep)")
                    command = self.speech_engine.listen()
                    
                    if command:
                        # Check for sleep command
                        if self.check_sleep_word(command):
                            self.awake = False
                            sleep_msg = self.jp_brain.personality.personalize_response("standby")
                            self.speech_engine.speak(sleep_msg)
                            continue
                        
                        # Check for exit commands
                        if any(word in command for word in ["goodbye", "bye", "exit", "quit"]):
                            goodbye = self.jp_brain.personality.personalize_response(
                                "standby", "Goodbye! Thanks for using JP Assistant. Have a great day!"
                            )
                            self.speech_engine.speak(goodbye)
                            self.shutdown()
                            break
                        
                        # Process with enhanced intelligence
                        response = self.process_jp_command(command)
                        self.speech_engine.speak(response)
                    else:
                        self.speech_engine.speak("I didn't hear anything clearly. Try again or say 'Bye JP' to sleep.")
                
            except KeyboardInterrupt:
                print("\n\n👋 Interrupted by user")
                self.shutdown()
                break
            except Exception as e:
                print(f"❌ Unexpected error: {e}")
                self.speech_engine.speak("I encountered an error. Please try again.")
    
    def shutdown(self) -> None:
        """Gracefully shutdown the enhanced assistant"""
        print("\n🔄 Shutting down enhanced systems...")
        self.running = False
        self.awake = False
        
        # Stop smart monitoring
        if self.monitoring:
            self.monitoring.stop_monitoring()
        
        # Save learning data
        if self.jp_brain:
            self.jp_brain.file_manager.save_json(
                "jp_learning.json", 
                self.jp_brain.learning_data
            )
        
        print(f"👋 Enhanced {ASSISTANT_NAME} offline. All systems powered down.")

def main():
    """Main entry point"""
    try:
        assistant = JPAssistant()
        assistant.run()
    except Exception as e:
        print(f"❌ Critical error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
