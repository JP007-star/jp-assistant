"""
JP Assistant Enhanced Configuration
Advanced settings for intelligent voice assistant
"""

# Assistant Identity
ASSISTANT_NAME = "JP Assistant"
ASSISTANT_FULL_NAME = "Just Perfect Assistant"
USER_NAME = "Boss"  # Default, can be customized
PERSONALITY = "professional"  # professional, friendly, technical

# Enhanced Audio Settings
MICROPHONE_INDEX = 3
ALWAYS_LISTENING = True
WAKE_WORD_SENSITIVITY = 0.7
CONTINUOUS_LISTENING = True

# JP Wake Words & Commands
WAKE_WORDS = [
    "hey jp", "jp", "hello jp", "okay jp", 
    "computer", "assistant", "hey", "hello"
]

ATTENTION_WORDS = [
    "jp", "computer", "assistant", "hey", "hello"
]

SLEEP_WORDS = [
    "bye jp", "goodbye jp", "sleep", "standby", 
    "go to sleep", "power down"
]

# Voice Personality Settings
VOICE_PERSONALITIES = {
    "professional": {
        "rate": 180,
        "volume": 0.9,
        "tone": "formal",
        "prefix_phrases": ["Certainly", "Right away", "Of course", "Absolutely"],
        "response_style": "professional"
    },
    "friendly": {
        "rate": 190,
        "volume": 0.85,
        "tone": "casual",
        "prefix_phrases": ["Sure thing", "Got it", "No problem", "You got it"],
        "response_style": "casual"
    },
    "technical": {
        "rate": 200,
        "volume": 0.8,
        "tone": "analytical", 
        "prefix_phrases": ["Analyzing", "Processing", "Computing", "Calculating"],
        "response_style": "technical"
    }
}

# Enhanced Features
ADVANCED_FEATURES = {
    "proactive_assistance": True,
    "learning_mode": True,
    "context_awareness": True,
    "predictive_suggestions": True,
    "environment_monitoring": True,
    "smart_responses": True
}

# Response Templates
JP_RESPONSES = {
    "greeting": [
        "Hello {user_name}! JP Assistant is online and ready to help.",
        "Good {time_of_day}, {user_name}. All systems ready. How can I assist?",
        "Hi {user_name}! I'm here and ready to help with anything you need.",
        "{time_of_day}, {user_name}. What can I do for you today?"
    ],
    
    "acknowledgment": [
        "Sure thing, {user_name}.",
        "Right away, {user_name}.",
        "Got it, {user_name}.",
        "On it, {user_name}."
    ],
    
    "task_complete": [
        "Task completed, {user_name}.",
        "Done! Anything else I can help with?",
        "Finished, {user_name}. What's next?",
        "Complete! Ready for the next task."
    ],
    
    "error": [
        "Sorry {user_name}, I ran into an issue with that.",
        "I'm having trouble with that request, {user_name}.",
        "Oops, something went wrong there.",
        "My apologies, {user_name}, I couldn't complete that."
    ],
    
    "standby": [
        "Going to sleep, {user_name}. Say 'Hey JP' to wake me up.",
        "Sleep mode activated. I'll be here when you need me.",
        "Taking a nap, {user_name}. Call me when you need help.",
        "Standby mode on. Just say my name when you're ready."
    ]
}

# Enhanced Commands
ENHANCED_COMMANDS = {
    "system_analysis": [
        "system scan", "full scan", "system status", "diagnostics",
        "check system", "analyze system", "system report"
    ],
    
    "optimization": [
        "optimize", "tune system", "improve performance", 
        "speed up", "clean system", "boost performance"
    ],
    
    "smart_assistance": [
        "what should I do", "suggestions", "recommendations",
        "help me decide", "what do you think", "advice"
    ],
    
    "learning": [
        "learn this", "remember this", "adapt", "improve",
        "learn from me", "get smarter", "understand me better"
    ]
}

# Monitoring Settings
MONITORING_INTERVALS = {
    "system_health": 300,      # 5 minutes
    "environment": 600,        # 10 minutes  
    "notifications": 60,       # 1 minute
    "learning": 900           # 15 minutes
}

# Learning Configuration
LEARNING_CONFIG = {
    "track_user_patterns": True,
    "learn_preferences": True,
    "adapt_responses": True,
    "remember_context": True,
    "predict_needs": True
}

# Smart Suggestions
SMART_SUGGESTIONS = {
    "morning": [
        "System health check and today's briefing",
        "Check for updates and optimize performance"
    ],
    "afternoon": [
        "Productivity boost and system cleanup",
        "File organization and backup check"
    ],
    "evening": [
        "End of day summary and system backup",
        "Tomorrow's preparation and shutdown routine"
    ]
}
