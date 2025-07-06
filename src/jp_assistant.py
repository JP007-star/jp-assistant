"""
JP Assistant - Enhanced Voice-Activated AI Assistant
Main application module
"""

import os
import sys
from typing import Optional
from core import config
from core.speech_engine import SpeechEngine
from core.command_processor import CommandProcessor

class JPAssistant:
    """Main application class for JP Voice Assistant"""
    
    def __init__(self):
        """Initialize the assistant"""
        self.speech_engine: Optional[SpeechEngine] = None
        self.command_processor: Optional[CommandProcessor] = None
        self.running = False
        self.awake = False  # Wake word state
        
        # Initialize components
        self.initialize()
    
    def initialize(self) -> bool:
        """Initialize all components"""
        print(f"🚀 Initializing {config.APP_NAME} v{config.APP_VERSION}...")
        
        try:
            # Initialize speech engine
            self.speech_engine = SpeechEngine()
            if not self.speech_engine.is_ready():
                print("❌ Speech engine initialization failed")
                return False
            
            # Initialize command processor
            self.command_processor = CommandProcessor()
            
            print("✅ All systems ready!")
            return True
            
        except Exception as e:
            print(f"❌ Initialization failed: {e}")
            return False
    
    def display_welcome(self) -> None:
        """Display welcome message and instructions"""
        print("\n" + "="*60)
        print(f"🎙️ {config.APP_NAME} v{config.APP_VERSION} - Enhanced Edition")
        print("="*60)
        print("💡 Controls:")
        print("   • Say 'Hey JP' or 'JP' to wake up")
        print("   • Say 'Bye JP' to go to sleep")
        print("   • Press ENTER for manual mode")
        print("   • Type 'quit' to exit")
        print("\n🌟 Enhanced Features:")
        print("   • System Information & Control")
        print("   • File Operations & Search")
        print("   • Web Search & Program Launching")
        print("   • Memory Storage & Recall")
        print("   • Entertainment & Conversations")
        print("-"*60)
    
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
    
    def check_wake_word(self, text: str) -> bool:
        """Check if text contains wake word"""
        text = text.lower().strip()
        
        # Check for exact matches first
        for wake_word in config.WAKE_WORDS:
            if wake_word in text:
                print(f"✅ Wake word detected: '{wake_word}' in '{text}'")
                return True
        
        # Check for partial matches (more flexible)
        if "jp" in text or "hey" in text or "hello" in text:
            print(f"✅ Partial wake word detected in: '{text}'")
            return True
            
        print(f"❌ No wake word in: '{text}'")
        return False
    
    def check_sleep_word(self, text: str) -> bool:
        """Check if text contains sleep word"""
        text = text.lower().strip()
        
        for sleep_word in config.SLEEP_WORDS:
            if sleep_word in text:
                print(f"✅ Sleep word detected: '{sleep_word}' in '{text}'")
                return True
        
        # Check for partial matches
        if ("bye" in text and "jp" in text) or "sleep" in text or "stop listening" in text:
            print(f"✅ Partial sleep word detected in: '{text}'")
            return True
            
        return False
    
    def run(self) -> None:
        """Main application loop"""
        if not self.speech_engine or not self.command_processor:
            print("❌ Cannot start - initialization failed")
            return
        
        # Display welcome information
        self.display_welcome()
        self.display_commands()
        
        # Initial greeting
        self.speech_engine.speak(
            f"Hello! I'm {config.APP_NAME}, your enhanced voice assistant. "
            "Say 'Hey JP' to wake me up, or press Enter for manual mode."
        )
        
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
                    
                    # Listen for wake word
                    wake_input = self.speech_engine.listen(wake_word_mode=True)
                    if wake_input:
                        if self.check_wake_word(wake_input):
                            self.awake = True
                            self.speech_engine.speak("Yes, I'm awake! How can I help you?")
                            continue
                        else:
                            # Continue listening for wake word
                            continue
                    
                else:
                    # Active listening mode
                    print("\n🎤 I'm awake! Say something (or 'Bye JP' to sleep)")
                    command = self.speech_engine.listen()
                    
                    if command:
                        # Check for sleep command
                        if self.check_sleep_word(command):
                            self.awake = False
                            self.speech_engine.speak("Going to sleep. Say 'Hey JP' to wake me up!")
                            continue
                        
                        # Check for exit commands
                        if any(word in command for word in ["goodbye", "bye", "exit", "quit"]):
                            response = self.command_processor.process_command(command)
                            self.speech_engine.speak(response)
                            self.shutdown()
                            break
                        
                        # Process regular command
                        response = self.command_processor.process_command(command)
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
        """Gracefully shutdown the assistant"""
        print("\n🔄 Shutting down...")
        self.running = False
        
        if self.speech_engine:
            self.speech_engine.speak("Goodbye! Thanks for using JP Assistant. Have a great day!")
        
        print(f"👋 {config.APP_NAME} stopped. Goodbye!")

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
