# Project Structure - JP Assistant

## Overview

JP Assistant follows a modular architecture with clear separation of concerns:

```
jp-assistant/
├── main.py                 # Entry point
├── setup.py               # Package setup
├── requirements_new.txt   # Dependencies
├── .gitignore            # Git ignore rules
│
├── src/                  # Source code
│   ├── __init__.py
│   ├── jp_assistant.py   # Main application logic
│   │
│   ├── core/            # Core functionality
│   │   ├── __init__.py
│   │   ├── config.py           # Configuration settings
│   │   ├── speech_engine.py    # Speech I/O
│   │   ├── command_processor.py # Command handling
│   │   └── system_manager.py   # System operations
│   │
│   ├── ui/              # User interface (future)
│   │   └── __init__.py
│   │
│   └── utils/           # Utility modules
│       ├── __init__.py
│       ├── logger.py           # Logging functionality
│       └── file_manager.py     # File operations
│
├── data/                # Application data
│   ├── memory.json      # Stored memories
│   └── settings.json    # User settings
│
├── models/              # Speech recognition models
│   └── vosk-model-small-en-in-0.4/
│
├── logs/                # Application logs
│   └── jp_assistant_YYYYMMDD.log
│
├── docs/                # Documentation
│   ├── README.md
│   ├── INSTALLATION.md
│   └── PROJECT_STRUCTURE.md
│
├── config/              # Legacy (can be removed)
└── core/                # Legacy (can be removed)
```

## Module Descriptions

### Core Modules (`src/core/`)

#### `config.py`
- **Purpose**: Central configuration management
- **Contains**: Audio settings, wake words, timeouts, error messages
- **Key Classes**: Configuration constants and settings

#### `speech_engine.py`
- **Purpose**: Speech recognition and text-to-speech
- **Key Class**: `SpeechEngine`
- **Features**:
  - Google Speech Recognition integration
  - pyttsx3 TTS engine
  - Microphone calibration
  - Wake word detection mode

#### `command_processor.py`
- **Purpose**: Parse and execute voice commands
- **Key Classes**: `CommandProcessor`, `MemoryManager`
- **Features**:
  - Natural language command parsing
  - Memory storage and retrieval
  - Command routing and execution

#### `system_manager.py`
- **Purpose**: System information and program control
- **Key Classes**: `SystemManager`, `ProgramLauncher`
- **Features**:
  - System resource monitoring
  - File system operations
  - External program launching
  - Web search capabilities

### Utility Modules (`src/utils/`)

#### `logger.py`
- **Purpose**: Logging and debugging
- **Key Class**: `Logger`
- **Features**:
  - File and console logging
  - Configurable log levels
  - Automatic log rotation

#### `file_manager.py`
- **Purpose**: File operations and data persistence
- **Key Class**: `FileManager`
- **Features**:
  - JSON data storage
  - Memory persistence
  - Settings management

### Main Application (`src/jp_assistant.py`)

- **Purpose**: Main application orchestration
- **Key Class**: `JPAssistant`
- **Features**:
  - Component initialization
  - Main event loop
  - Wake word state management
  - Error handling and recovery

## Data Flow

```
User Speech Input
       ↓
SpeechEngine.listen()
       ↓
CommandProcessor.process_command()
       ↓
SystemManager / MemoryManager
       ↓
SpeechEngine.speak()
       ↓
Audio Output
```

## Design Patterns

### 1. **Modular Architecture**
- Clear separation of concerns
- Loose coupling between modules
- Easy to test and maintain

### 2. **Factory Pattern**
- `SpeechEngine` creates and configures TTS/STT components
- `CommandProcessor` creates appropriate response handlers

### 3. **State Machine**
- Wake/sleep states managed in main application
- Clear state transitions and handling

### 4. **Configuration Management**
- Centralized configuration in `config.py`
- Easy to modify settings without code changes

## Extension Points

### Adding New Commands

1. **Simple Commands**: Add to `command_processor.py`
   ```python
   elif "new command" in command:
       return "Response"
   ```

2. **Complex Commands**: Create new handler class
   ```python
   class NewCommandHandler:
       def handle(self, command):
           # Implementation
   ```

### Adding New System Operations

1. **Extend SystemManager**: Add new methods
   ```python
   @staticmethod
   def new_system_operation():
       # Implementation
   ```

### Adding New I/O Methods

1. **Extend SpeechEngine**: Add new recognition backends
2. **Create UI Module**: Add graphical interface

### Adding New Data Sources

1. **Extend FileManager**: Add new data formats
2. **Create Database Module**: Add persistent storage

## Configuration Management

### Environment-Specific Settings

```python
# Development
DEBUG = True
LOG_LEVEL = "DEBUG"

# Production
DEBUG = False
LOG_LEVEL = "INFO"
```

### User-Specific Settings

```python
# Stored in data/settings.json
{
  "microphone_index": 3,
  "preferred_voice": "female",
  "wake_words": ["custom wake word"]
}
```

## Testing Strategy

### Unit Tests (Future)
- Test individual modules in isolation
- Mock external dependencies
- Test configuration loading

### Integration Tests (Future)
- Test module interactions
- Test complete command flows
- Test error handling

### System Tests (Future)
- Test complete user scenarios
- Test with actual hardware
- Performance testing

## Security Considerations

### Data Protection
- No sensitive data stored in logs
- Memory data encrypted (future enhancement)
- Settings validation

### System Access
- Limited system operations
- No shell execution without validation
- Sandboxed file operations

## Performance Considerations

### Memory Management
- Lazy loading of speech models
- Efficient memory cleanup
- Limited memory storage

### Response Time
- Optimized command parsing
- Cached system information
- Async operations (future enhancement)

This modular structure ensures JP Assistant is maintainable, extensible, and robust.
