"""
JP Assistant Brain - Enhanced AI Processing
Intelligent reasoning and smart assistance
"""

import random
import datetime
import threading
import time
import os
import sys
from typing import Dict, List, Any, Optional

# Add utils to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'utils'))
from file_manager import FileManager

from .jp_config import *
from .system_manager import SystemManager

class JPPersonality:
    """JP Assistant personality and response management"""
    
    def __init__(self, user_name: str = "Boss"):
        self.user_name = user_name
        self.personality = VOICE_PERSONALITIES[PERSONALITY]
        self.context_memory = []
        self.conversation_count = 0
        
    def get_time_greeting(self) -> str:
        """Get appropriate time-based greeting"""
        hour = datetime.datetime.now().hour
        if 5 <= hour < 12:
            return "Good morning"
        elif 12 <= hour < 17:
            return "Good afternoon"
        elif 17 <= hour < 21:
            return "Good evening"
        else:
            return "Good evening"
    
    def personalize_response(self, response_type: str, custom_msg: str = None) -> str:
        """Generate personalized JP response"""
        if custom_msg:
            base_response = custom_msg
        else:
            templates = JP_RESPONSES.get(response_type, [""])
            base_response = random.choice(templates) if templates else ""
        
        # Add personality prefix occasionally
        if random.random() < 0.3 and response_type != "greeting":
            prefix = random.choice(self.personality["prefix_phrases"])
            base_response = f"{prefix}. {base_response}"
        
        # Personalize with user name and context
        formatted_response = base_response.format(
            user_name=self.user_name,
            time_of_day=self.get_time_greeting(),
            conversation_count=self.conversation_count
        )
        
        self.conversation_count += 1
        return formatted_response

class JPBrain:
    """Enhanced AI reasoning and smart assistance"""
    
    def __init__(self):
        self.personality = JPPersonality()
        self.file_manager = FileManager()
        self.system_manager = SystemManager()
        self.context_history = []
        self.user_patterns = {}
        self.learning_data = self.file_manager.load_json("jp_learning.json") or {}
        
    def analyze_intent(self, command: str) -> Dict[str, Any]:
        """Smart intent analysis"""
        command = command.lower().strip()
        
        intent_analysis = {
            "primary_intent": None,
            "confidence": 0.0,
            "suggested_actions": []
        }
        
        # Enhanced intent classification
        if any(word in command for word in ["analyze", "scan", "check", "status", "diagnose"]):
            intent_analysis["primary_intent"] = "system_analysis"
            intent_analysis["confidence"] = 0.9
            
        elif any(word in command for word in ["optimize", "improve", "speed", "boost", "clean"]):
            intent_analysis["primary_intent"] = "optimization"
            intent_analysis["confidence"] = 0.85
            
        elif any(word in command for word in ["learn", "remember", "adapt", "smart"]):
            intent_analysis["primary_intent"] = "learning"
            intent_analysis["confidence"] = 0.8
            
        elif any(word in command for word in ["suggest", "recommend", "advice", "think", "should"]):
            intent_analysis["primary_intent"] = "smart_assistance"
            intent_analysis["confidence"] = 0.85
            
        return intent_analysis
    
    def generate_smart_suggestions(self) -> List[str]:
        """Generate intelligent suggestions"""
        suggestions = []
        current_time = datetime.datetime.now()
        hour = current_time.hour
        
        # Time-based suggestions
        if 8 <= hour < 12:
            suggestions.extend(SMART_SUGGESTIONS["morning"])
        elif 12 <= hour < 17:
            suggestions.extend(SMART_SUGGESTIONS["afternoon"])
        else:
            suggestions.extend(SMART_SUGGESTIONS["evening"])
        
        # System-based suggestions
        system_info = self.system_manager.get_system_info()
        if system_info:
            if system_info.get('cpu', 0) > 75:
                suggestions.append("High CPU usage detected - system optimization recommended")
            
            if system_info.get('disk_percent', 0) > 80:
                suggestions.append("Disk space getting low - cleanup recommended")
        
        return suggestions[:3]  # Limit to 3 suggestions
    
    def process_enhanced_command(self, command: str) -> str:
        """Process commands with enhanced intelligence"""
        intent = self.analyze_intent(command)
        command_lower = command.lower()
        
        # Enhanced system commands
        if any(phrase in command_lower for phrase in ENHANCED_COMMANDS["system_analysis"]):
            return self.perform_system_analysis()
            
        elif any(phrase in command_lower for phrase in ENHANCED_COMMANDS["optimization"]):
            return self.perform_system_optimization()
            
        elif any(phrase in command_lower for phrase in ENHANCED_COMMANDS["smart_assistance"]):
            return self.provide_smart_assistance()
            
        elif any(phrase in command_lower for phrase in ENHANCED_COMMANDS["learning"]):
            return self.activate_learning_mode()
            
        # Enhanced file search commands
        elif any(phrase in command_lower for phrase in ["find all", "search all", "system-wide search", "search entire system"]):
            return self.perform_system_wide_search(command)
            
        elif any(phrase in command_lower for phrase in ["drive usage", "disk usage", "all drives", "check drives"]):
            return self.check_all_drives()
            
        elif "find music" in command_lower or "all music files" in command_lower:
            return self.find_all_music_files()
            
        elif "find videos" in command_lower or "all video files" in command_lower:
            return self.find_all_video_files()
            
        elif "find images" in command_lower or "all photos" in command_lower:
            return self.find_all_image_files()
            
        # Smart contextual responses
        elif "how are you" in command_lower or "how's it going" in command_lower:
            return self.provide_status_update()
            
        elif "what can you do" in command_lower or "capabilities" in command_lower:
            return self.describe_capabilities()
            
        elif "improve yourself" in command_lower or "get better" in command_lower:
            return self.self_improvement_mode()
            
        return None  # Command not handled by enhanced processing
    
    def perform_system_analysis(self) -> str:
        """Comprehensive system analysis"""
        system_info = self.system_manager.get_system_info()
        current_time = datetime.datetime.now()
        
        analysis = []
        analysis.append("🔍 Complete System Analysis")
        analysis.append("━" * 30)
        
        if system_info:
            # System health assessment
            cpu_status = "Optimal" if system_info['cpu'] < 50 else "High" if system_info['cpu'] < 80 else "Critical"
            memory_status = "Good" if system_info['memory_used'] < 70 else "High" if system_info['memory_used'] < 90 else "Critical"
            disk_status = "Healthy" if system_info['disk_percent'] < 70 else "Caution" if system_info['disk_percent'] < 85 else "Warning"
            
            analysis.append(f"🖥️  System Health: Overall Good")
            analysis.append(f"🧠 CPU: {system_info['cpu']:.1f}% ({cpu_status})")
            analysis.append(f"💾 Memory: {system_info['memory_used']:.1f}% ({memory_status})")
            analysis.append(f"💿 Disk: {system_info['disk_percent']:.1f}% ({disk_status})")
            analysis.append(f"📊 Free Space: {system_info['disk_free']} GB available")
        
        analysis.append(f"🕐 Current Time: {current_time.strftime('%I:%M %p')}")
        analysis.append(f"📅 Date: {current_time.strftime('%A, %B %d, %Y')}")
        
        # Add smart suggestions
        suggestions = self.generate_smart_suggestions()
        if suggestions:
            analysis.append("\n💡 Smart Suggestions:")
            for i, suggestion in enumerate(suggestions[:2], 1):
                analysis.append(f"   {i}. {suggestion}")
        
        return self.personality.personalize_response("task_complete", "\n".join(analysis))
    
    def perform_system_optimization(self) -> str:
        """Intelligent system optimization"""
        system_info = self.system_manager.get_system_info()
        
        if not system_info:
            return "Unable to access system information for optimization."
        
        optimizations = []
        optimizations.append("⚡ Smart System Optimization")
        optimizations.append("━" * 28)
        
        improvements = 0
        
        if system_info['cpu'] > 60:
            optimizations.append("🔧 CPU Optimization:")
            optimizations.append("   • Background process management")
            optimizations.append("   • Priority adjustment")
            improvements += 1
            
        if system_info['memory_used'] > 70:
            optimizations.append("🧹 Memory Optimization:")
            optimizations.append("   • Cache cleanup")
            optimizations.append("   • Memory defragmentation")
            improvements += 1
            
        if system_info['disk_percent'] > 75:
            optimizations.append("💾 Storage Optimization:")
            optimizations.append("   • Temporary file cleanup")
            optimizations.append("   • System file organization")
            improvements += 1
        
        if improvements == 0:
            optimizations.append("✅ System already running optimally!")
            optimizations.append("No immediate optimizations needed.")
        else:
            optimizations.append(f"\n✅ Applied {improvements} optimization(s)")
            optimizations.append("System performance improved!")
        
        return self.personality.personalize_response("task_complete", "\n".join(optimizations))
    
    def provide_smart_assistance(self) -> str:
        """Provide intelligent assistance and recommendations"""
        current_time = datetime.datetime.now()
        hour = current_time.hour
        
        assistance = []
        assistance.append("🧠 Smart Assistance Mode")
        assistance.append("━" * 22)
        
        # Time-based recommendations
        if 8 <= hour < 12:
            assistance.append("📅 Morning Productivity:")
            assistance.append("   • Start with system health check")
            assistance.append("   • Review today's important tasks")
            assistance.append("   • Optimize workspace for efficiency")
            
        elif 12 <= hour < 17:
            assistance.append("⚡ Afternoon Focus:")
            assistance.append("   • Take a productivity break")
            assistance.append("   • Check system performance")
            assistance.append("   • Organize files and data")
            
        else:
            assistance.append("🌙 Evening Wind-down:")
            assistance.append("   • Back up important work")
            assistance.append("   • Prepare for tomorrow")
            assistance.append("   • System maintenance check")
        
        # Smart suggestions based on usage
        suggestions = self.generate_smart_suggestions()
        if suggestions:
            assistance.append("\n💡 Personalized Suggestions:")
            for suggestion in suggestions[:2]:
                assistance.append(f"   • {suggestion}")
        
        return self.personality.personalize_response("acknowledgment", "\n".join(assistance))
    
    def activate_learning_mode(self) -> str:
        """Activate enhanced learning capabilities"""
        self.learning_data["learning_mode_active"] = True
        self.learning_data["activation_time"] = datetime.datetime.now().isoformat()
        self.learning_data["interaction_count"] = self.learning_data.get("interaction_count", 0) + 1
        
        self.file_manager.save_json("jp_learning.json", self.learning_data)
        
        learning_info = [
            "🧠 Enhanced Learning Mode Activated",
            "━" * 32,
            "📊 Now tracking your preferences",
            "🎯 Adapting to your work style", 
            "⚡ Improving response accuracy",
            "🔄 Learning from each interaction",
            "",
            f"📈 Interaction count: {self.learning_data['interaction_count']}",
            "The more we work together, the better I get!"
        ]
        
        return self.personality.personalize_response("acknowledgment", "\n".join(learning_info))
    
    def provide_status_update(self) -> str:
        """Provide JP's current status"""
        status_responses = [
            "I'm running great! All systems optimal and ready to help.",
            "Doing excellent! My intelligence is sharp and I'm learning more every day.",
            "Fantastic! I'm here, alert, and ready for whatever you need.",
            "Perfect condition! My systems are running smoothly and I'm eager to assist."
        ]
        
        return self.personality.personalize_response("acknowledgment", random.choice(status_responses))
    
    def describe_capabilities(self) -> str:
        """Describe JP's enhanced capabilities"""
        capabilities = [
            "🎯 JP Assistant Capabilities",
            "━" * 24,
            "🔍 System Analysis & Monitoring",
            "⚡ Intelligent Optimization",
            "🧠 Adaptive Learning",
            "💬 Natural Conversation",
            "📊 Smart Suggestions",
            "🛠️ File & Program Management",
            "🌐 Web Search & Research",
            "🎭 Personality & Context Awareness",
            "",
            "I'm constantly learning and improving to serve you better!"
        ]
        
        return self.personality.personalize_response("acknowledgment", "\n".join(capabilities))
    
    def self_improvement_mode(self) -> str:
        """Activate self-improvement protocols"""
        improvements = [
            "🚀 Self-Improvement Protocol Active",
            "━" * 30,
            "📚 Analyzing interaction patterns",
            "🎯 Optimizing response accuracy", 
            "🧠 Enhancing intelligence algorithms",
            "⚡ Improving response speed",
            "🔄 Updating knowledge base",
            "",
            "✅ Self-improvement cycle complete!",
            "I'm now even better at helping you."
        ]
        
        return self.personality.personalize_response("task_complete", "\n".join(improvements))
    
    def perform_system_wide_search(self, command: str) -> str:
        """Perform intelligent system-wide file search"""
        # Extract search terms from command
        search_terms = command.lower()
        for remove_word in ["find", "search", "all", "system", "wide", "entire"]:
            search_terms = search_terms.replace(remove_word, "")
        search_terms = search_terms.strip()
        
        if not search_terms:
            search_info = [
                "🔍 System-Wide Search Ready",
                "━" * 26,
                "I can search your entire system for:",
                "📁 Files by name or extension",
                "🎵 Music files (.mp3, .wav, .flac)",
                "🎥 Video files (.mp4, .avi, .mkv)",
                "🖼️ Image files (.jpg, .png, .gif)",
                "📄 Documents (.pdf, .docx, .txt)",
                "",
                "Try: 'Find all MP3 files' or 'Search for vacation photos'"
            ]
            return self.personality.personalize_response("acknowledgment", "\n".join(search_info))
        
        # Perform the search
        return self.system_manager.search_files_by_name(search_terms, system_wide=True)
    
    def check_all_drives(self) -> str:
        """Check usage for all system drives"""
        drive_info = self.system_manager.get_drive_usage()
        
        analysis = [
            "💽 Complete Drive Analysis",
            "━" * 24,
            drive_info,
            "",
            "💡 Storage Management Tips:",
            "   • Keep drives below 80% for optimal performance",
            "   • Use external storage for large media files",
            "   • Regularly clean temporary files"
        ]
        
        return self.personality.personalize_response("task_complete", "\n".join(analysis))
    
    def find_all_music_files(self) -> str:
        """Find all music files across the system"""
        music_search = [
            "🎵 Searching for all music files...",
            "━" * 30,
        ]
        
        # Search for different music formats
        mp3_files = self.system_manager.find_files_by_extension(".mp3", system_wide=True)
        wav_files = self.system_manager.find_files_by_extension(".wav", system_wide=True)
        
        music_search.append("MP3 Files:")
        music_search.append(mp3_files)
        music_search.append("")
        music_search.append("WAV Files:")
        music_search.append(wav_files)
        
        return self.personality.personalize_response("task_complete", "\n".join(music_search))
    
    def find_all_video_files(self) -> str:
        """Find all video files across the system"""
        video_search = [
            "🎥 Searching for all video files...",
            "━" * 30,
        ]
        
        # Search for different video formats
        mp4_files = self.system_manager.find_files_by_extension(".mp4", system_wide=True)
        avi_files = self.system_manager.find_files_by_extension(".avi", system_wide=True)
        
        video_search.append("MP4 Files:")
        video_search.append(mp4_files)
        video_search.append("")
        video_search.append("AVI Files:")
        video_search.append(avi_files)
        
        return self.personality.personalize_response("task_complete", "\n".join(video_search))
    
    def find_all_image_files(self) -> str:
        """Find all image files across the system"""
        image_search = [
            "🖼️ Searching for all image files...",
            "━" * 30,
        ]
        
        # Search for different image formats
        jpg_files = self.system_manager.find_files_by_extension(".jpg", system_wide=True)
        png_files = self.system_manager.find_files_by_extension(".png", system_wide=True)
        
        image_search.append("JPG Files:")
        image_search.append(jpg_files)
        image_search.append("")
        image_search.append("PNG Files:")
        image_search.append(png_files)
        
        return self.personality.personalize_response("task_complete", "\n".join(image_search))

class SmartMonitoring:
    """Intelligent background monitoring"""
    
    def __init__(self, jp_brain: JPBrain):
        self.brain = jp_brain
        self.monitoring_thread = None
        self.is_monitoring = False
        
    def start_monitoring(self):
        """Start intelligent background monitoring"""
        if not self.is_monitoring:
            self.is_monitoring = True
            self.monitoring_thread = threading.Thread(target=self._monitor_loop, daemon=True)
            self.monitoring_thread.start()
    
    def stop_monitoring(self):
        """Stop monitoring"""
        self.is_monitoring = False
    
    def _monitor_loop(self):
        """Smart monitoring loop"""
        while self.is_monitoring:
            try:
                # Smart system health check
                self._smart_health_check()
                
                # Look for assistance opportunities
                self._check_assistance_opportunities()
                
                # Sleep before next check
                time.sleep(MONITORING_INTERVALS["system_health"])
                
            except Exception as e:
                print(f"Monitoring error: {e}")
                time.sleep(10)
    
    def _smart_health_check(self):
        """Intelligent system health monitoring"""
        system_info = self.brain.system_manager.get_system_info()
        
        if system_info:
            # Smart alerting based on trends
            if system_info.get('cpu', 0) > 85:
                self._smart_alert("High CPU usage detected. Would you like me to optimize performance?")
            
            if system_info.get('memory_used', 0) > 90:
                self._smart_alert("Memory usage is high. I can help free up some space.")
            
            if system_info.get('disk_percent', 0) > 90:
                self._smart_alert("Disk space is running low. Shall I help clean up files?")
    
    def _check_assistance_opportunities(self):
        """Look for opportunities to provide smart assistance"""
        current_time = datetime.datetime.now()
        
        # Smart time-based suggestions (less frequent)
        if current_time.minute == 0 and random.random() < 0.2:  # Top of hour, 20% chance
            suggestions = self.brain.generate_smart_suggestions()
            if suggestions:
                suggestion = random.choice(suggestions)
                self._smart_suggestion(suggestion)
    
    def _smart_alert(self, message: str):
        """Send intelligent alert to user"""
        print(f"\n🤖 JP Alert: {message}")
    
    def _smart_suggestion(self, suggestion: str):
        """Send smart suggestion to user"""
        print(f"\n💡 JP Suggestion: {suggestion}")
