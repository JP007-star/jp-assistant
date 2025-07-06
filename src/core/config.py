# Configuration settings for JP Assistant

# Audio Settings
MICROPHONE_INDEX = 3
TIMEOUT_SECONDS = 8
PHRASE_TIME_LIMIT = 8
AMBIENT_NOISE_DURATION = 2

# Wake Word Settings
WAKE_WORDS = ["hey jp", "jp", "hello jp", "wake up jp", "hello", "hey", "hi jp"]
SLEEP_WORDS = ["bye jp", "goodbye jp", "sleep jp", "stop listening", "go to sleep", "bye"]
WAKE_WORD_TIMEOUT = 3  # Shorter timeout for wake word detection

# Speech Settings
TTS_RATE = 200
TTS_VOLUME = 0.9

# System Settings
MAX_FILES_TO_SHOW = 10
MAX_SEARCH_RESULTS = 5

# Application Info
APP_NAME = "JP Assistant"
APP_VERSION = "2.0"
AUTHOR = "Your Name"

# Available Commands Help Text
HELP_TEXT = """
I can help you with:
• Time and Date information
• System status (CPU, Memory, Disk usage)
• Open programs (Notepad, Calculator, Browser)
• Web search on Google
• File and folder listing
• Remember and recall information
• Tell jokes and have conversations
• Much more!
"""

# Joke Database
JOKES = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "I told my computer a joke about UDP, but it didn't get it.",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
    "Why did the developer go broke? Because he used up all his cache!",
    "What's a computer's favorite beat? An algo-rhythm!",
]

# Error Messages
ERROR_MESSAGES = {
    "mic_not_found": "❌ Microphone not found or not accessible",
    "speech_timeout": "⏰ No speech detected within timeout period",
    "speech_unclear": "🤔 Could not understand the audio clearly",
    "system_info_failed": "❌ Could not retrieve system information",
    "file_access_failed": "❌ Could not access file system",
    "program_launch_failed": "❌ Could not launch the requested program",
    "search_failed": "❌ Could not perform web search",
    "general_error": "❌ An unexpected error occurred"
}
