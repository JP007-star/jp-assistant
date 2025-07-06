# JP Assistant - Enhanced Voice-Activated AI Assistant

A powerful, modular voice-activated AI assistant built in Python with advanced system integration capabilities.

## Features

### 🎙️ Voice Recognition
- Google Speech Recognition for high accuracy
- Automatic microphone calibration
- Configurable timeout and phrase limits
- Multiple microphone support

### 🤖 Text-to-Speech
- Natural voice synthesis
- Configurable voice selection
- Adjustable speech rate and volume
- Fallback to text display

### 💻 System Integration
- Real-time system monitoring (CPU, Memory, Disk)
- File system operations and search
- Program launching (Notepad, Calculator, Browser, etc.)
- Web search capabilities

### 🧠 Memory System
- Store and recall information
- Persistent memory during session
- Natural language memory commands

### 🎯 Smart Commands
- Time and date information
- System status monitoring
- File operations and search
- Web search and browsing
- Entertainment (jokes, conversations)
- Help and guidance system

## Installation

1. **Clone or download the project files**

2. **Install dependencies:**
   ```bash
   pip install -r requirements_new.txt
   ```

3. **Configure microphone (if needed):**
   - Edit `config.py` and change `MICROPHONE_INDEX` to your preferred microphone
   - Run a test to find your microphone index if needed

## Usage

### Quick Start
```bash
python jp_assistant.py
```

### Voice Commands Examples

**System Information:**
- "What's my system status?"
- "Check CPU usage"
- "How much disk space do I have?"

**File Operations:**
- "List files"
- "Find MP3 files"
- "Show me PDF files"

**Program Control:**
- "Open calculator"
- "Open notepad"
- "Open browser"

**Web Search:**
- "Search for Python tutorials"
- "Google weather forecast"

**Memory:**
- "Remember my birthday is June 15th"
- "What is my birthday?"
- "List memories"

**Time & Date:**
- "What time is it?"
- "What's today's date?"

**Entertainment:**
- "Tell me a joke"
- "Sing a song"

## Project Structure

```
jp-assistant/
├── jp_assistant.py          # Main application
├── config.py               # Configuration settings
├── speech_engine.py        # Speech recognition & TTS
├── command_processor.py    # Command parsing & execution
├── system_manager.py       # System operations
├── requirements_new.txt    # Dependencies
└── README.md              # This file
```

## Architecture

### Modular Design
- **SpeechEngine**: Handles all speech I/O operations
- **CommandProcessor**: Processes and routes commands
- **SystemManager**: System information and operations
- **MemoryManager**: Memory storage and retrieval
- **ProgramLauncher**: External program management

### Configuration
All settings are centralized in `config.py`:
- Audio settings (microphone, timeouts)
- TTS configuration
- System limits and thresholds
- Help text and error messages

## Customization

### Adding New Commands
1. Edit `command_processor.py`
2. Add new conditions in `process_command()` method
3. Implement the command logic

### Changing Voice Settings
1. Edit `config.py`
2. Modify `TTS_RATE`, `TTS_VOLUME`
3. Adjust microphone settings

### Adding New Programs
1. Edit `system_manager.py`
2. Add entries to `ProgramLauncher.PROGRAMS`

## Troubleshooting

### Microphone Issues
- Check microphone permissions in Windows
- Try different microphone indices in config
- Ensure microphone is not used by other applications

### Speech Recognition Issues
- Check internet connection (Google Speech API)
- Speak clearly and avoid background noise
- Adjust timeout settings in config

### TTS Issues
- Install additional voice packages if needed
- Check system audio settings
- Try different voice selections

## Requirements

- Python 3.7+
- Windows 10/11 (tested)
- Microphone access
- Internet connection (for Google Speech Recognition)

## License

Open source - feel free to modify and distribute.

## Author

Created for enhanced voice assistant functionality with system integration.
