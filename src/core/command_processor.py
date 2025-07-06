"""
Command Processor Module - Handles command parsing and execution
"""

import datetime
import random
from typing import Dict, Any
from . import config
from .system_manager import SystemManager, ProgramLauncher

class MemoryManager:
    """Handles memory storage and retrieval"""
    
    def __init__(self):
        self.memories: Dict[str, str] = {}
    
    def remember(self, command: str) -> str:
        """Store information in memory"""
        words = command.split()
        
        if "remember" in words and "is" in words:
            try:
                remember_idx = words.index("remember")
                is_idx = words.index("is")
                key = " ".join(words[remember_idx+1:is_idx]).strip()
                value = " ".join(words[is_idx+1:]).strip()
                
                if key and value:
                    self.memories[key] = value
                    return f"Got it! I'll remember that {key} is {value}"
            except (ValueError, IndexError):
                pass
        
        return "I didn't understand what to remember. Say 'remember [something] is [value]'"
    
    def recall(self, command: str) -> str:
        """Retrieve information from memory"""
        # Check if any stored key matches the query
        for key in self.memories:
            if key in command:
                return f"{key} is {self.memories[key]}"
        
        # If no exact match, try partial matching
        query_words = command.replace("what is", "").replace("recall", "").strip().split()
        for key in self.memories:
            if any(word in key for word in query_words):
                return f"{key} is {self.memories[key]}"
        
        return "I don't have that information stored in my memory."
    
    def list_memories(self) -> str:
        """List all stored memories"""
        if not self.memories:
            return "I don't have any memories stored yet."
        
        memory_list = []
        for key, value in list(self.memories.items())[:5]:  # Show first 5
            memory_list.append(f"{key} is {value}")
        
        return f"Here's what I remember: {'; '.join(memory_list)}"

class CommandProcessor:
    """Main command processing engine"""
    
    def __init__(self):
        self.memory_manager = MemoryManager()
        self.command_count = 0
    
    def process_command(self, command: str) -> str:
        """Process voice command and return appropriate response"""
        if not command.strip():
            return "I didn't hear anything. Please try again."
        
        command = command.lower().strip()
        self.command_count += 1
        
        # Greeting commands
        if any(word in command for word in ["hello", "hi", "hey", "good morning", "good afternoon"]):
            greetings = [
                "Hello! How can I help you today?",
                "Hi there! What would you like to know?",
                "Hey! I'm here to help. What do you need?",
                "Good to hear from you! How can I assist?"
            ]
            return random.choice(greetings)
        
        # Time and date commands
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            return f"The current time is {current_time}"
        
        elif any(word in command for word in ["date", "today", "day"]):
            today = datetime.datetime.now().strftime("%A, %B %d, %Y")
            return f"Today is {today}"
        
        # Identity commands
        elif any(phrase in command for phrase in ["your name", "who are you", "what are you"]):
            return f"I'm {config.APP_NAME} version {config.APP_VERSION}, your advanced voice-activated AI helper!"
        
        # Gratitude responses
        elif any(word in command for word in ["thank", "thanks", "appreciate"]):
            responses = [
                "You're very welcome!",
                "Happy to help!",
                "My pleasure!",
                "Anytime! I'm here to help."
            ]
            return random.choice(responses)
        
        # System information commands
        elif any(word in command for word in ["storage", "disk", "space", "memory", "system"]):
            return SystemManager.get_system_status()
        
        elif any(word in command for word in ["cpu", "processor", "performance"]):
            return SystemManager.get_cpu_usage()
        
        # File operations
        elif any(word in command for word in ["files", "folder", "directory", "list"]):
            if "mp3" in command:
                return SystemManager.find_files_by_extension(".mp3")
            elif "jpg" in command or "jpeg" in command:
                return SystemManager.find_files_by_extension(".jpg")
            elif "pdf" in command:
                return SystemManager.find_files_by_extension(".pdf")
            elif "txt" in command:
                return SystemManager.find_files_by_extension(".txt")
            else:
                return SystemManager.list_files()
        
        # Program launching
        elif "open" in command:
            if "browser" in command or "chrome" in command or "edge" in command:
                return ProgramLauncher.open_browser()
            else:
                # Extract program name
                for program in ProgramLauncher.PROGRAMS.keys():
                    if program in command:
                        return ProgramLauncher.launch_program(program)
                return ProgramLauncher.launch_program("")  # Show available programs
        
        # Web search
        elif "search" in command or "google" in command or "find" in command:
            # Extract search terms
            search_terms = command
            for remove_word in ["search", "for", "google", "find", "on", "the", "internet", "web"]:
                search_terms = search_terms.replace(remove_word, "")
            search_terms = search_terms.strip()
            
            return ProgramLauncher.search_web(search_terms)
        
        # Memory commands
        elif "remember" in command:
            return self.memory_manager.remember(command)
        
        elif any(phrase in command for phrase in ["what is", "recall", "what do you know about"]):
            return self.memory_manager.recall(command)
        
        elif "list memories" in command or "what do you remember" in command:
            return self.memory_manager.list_memories()
        
        # Entertainment
        elif "joke" in command or "funny" in command:
            return random.choice(config.JOKES)
        
        elif "sing" in command:
            return "🎵 I'm just a voice assistant, but here's a classic: 'Daisy, Daisy, give me your answer true...' 🎵"
        
        # Help and capabilities
        elif any(word in command for word in ["help", "what can you do", "capabilities", "features"]):
            return config.HELP_TEXT.strip()
        
        # Weather (placeholder)
        elif "weather" in command:
            return "I don't have direct weather access, but I can search for weather information if you'd like! Just say 'search weather in [your city]'"
        
        # Shutdown/restart (security)
        elif any(word in command for word in ["shutdown", "restart", "reboot", "turn off"]):
            return "I cannot perform system shutdown or restart commands for security reasons."
        
        # Stats about usage
        elif "stats" in command or "statistics" in command:
            return f"I've processed {self.command_count} commands in this session and have {len(self.memory_manager.memories)} memories stored."
        
        # Exit commands
        elif any(word in command for word in ["goodbye", "bye", "exit", "quit", "stop"]):
            return "Goodbye! It was great helping you today!"
        
        # Default response for unrecognized commands
        else:
            suggestions = [
                "I'm not sure about that. Try asking about time, system info, or say 'help' to see what I can do!",
                "I didn't understand that command. Would you like to see my capabilities? Just say 'help'!",
                "Hmm, I'm not familiar with that. Ask me about the time, open programs, or search the web!",
            ]
            return random.choice(suggestions)
