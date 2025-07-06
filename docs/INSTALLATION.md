# Installation Guide - JP Assistant

## Prerequisites

- **Python 3.7+** (recommended: Python 3.9 or higher)
- **Windows 10/11** (currently optimized for Windows)
- **Microphone** (built-in or external)
- **Internet connection** (for Google Speech Recognition)

## Quick Installation

### Method 1: Simple Setup

1. **Download the project**
   ```bash
   git clone <repository-url>
   cd jp-assistant
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements_new.txt
   ```

3. **Run the assistant**
   ```bash
   python main.py
   ```

### Method 2: Development Setup

1. **Create virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

2. **Install in development mode**
   ```bash
   pip install -e .
   ```

3. **Run from anywhere**
   ```bash
   jp-assistant
   ```

## Configuration

### Microphone Setup

1. **Find your microphone index:**
   - Run the assistant and check the console output
   - It will show detected microphones
   - Note the index number of your preferred microphone

2. **Update configuration:**
   - Edit `src/core/config.py`
   - Change `MICROPHONE_INDEX = 3` to your microphone index

### Audio Settings

In `src/core/config.py`, you can adjust:

```python
# Audio Settings
MICROPHONE_INDEX = 3          # Your microphone index
TIMEOUT_SECONDS = 8           # How long to wait for speech
PHRASE_TIME_LIMIT = 8         # Maximum phrase length
AMBIENT_NOISE_DURATION = 2    # Noise calibration time

# Speech Settings
TTS_RATE = 200               # Speech speed
TTS_VOLUME = 0.9            # Speech volume

# Wake Word Settings
WAKE_WORDS = ["hey jp", "jp", "hello jp"]
SLEEP_WORDS = ["bye jp", "goodbye jp", "sleep jp"]
```

## Troubleshooting

### Common Issues

1. **Microphone not working:**
   - Check Windows microphone permissions
   - Try different microphone indices
   - Ensure microphone is not used by other apps

2. **Speech recognition failing:**
   - Check internet connection
   - Speak clearly and avoid background noise
   - Increase timeout settings

3. **Import errors:**
   - Ensure you're in the project directory
   - Check Python path: `python -c "import sys; print(sys.path)"`
   - Reinstall dependencies: `pip install -r requirements_new.txt`

4. **Permission errors:**
   - Run as administrator if needed
   - Check file permissions in the project directory

### Dependencies Issues

If you encounter issues with specific packages:

1. **PyAudio installation issues:**
   ```bash
   # Try installing with conda
   conda install pyaudio
   
   # Or use pre-compiled wheel
   pip install pipwin
   pipwin install pyaudio
   ```

2. **Speech Recognition issues:**
   ```bash
   pip install --upgrade SpeechRecognition
   ```

3. **TTS issues:**
   ```bash
   pip install --upgrade pyttsx3
   ```

## Performance Optimization

1. **Reduce startup time:**
   - Keep models in memory (already implemented)
   - Use SSD storage if possible

2. **Improve speech recognition:**
   - Use a quality microphone
   - Minimize background noise
   - Speak clearly and at moderate pace

3. **System resources:**
   - Close unnecessary applications
   - Ensure adequate RAM (4GB+ recommended)
   - Use wired internet for better recognition

## Advanced Configuration

### Custom Commands

To add custom commands, edit `src/core/command_processor.py`:

```python
elif "your custom command" in command:
    return "Your custom response"
```

### Custom Wake Words

Edit `src/core/config.py`:

```python
WAKE_WORDS = ["your wake word", "another wake word"]
```

### Logging

Logs are automatically saved to the `logs/` directory. To change log level:

```python
# In src/utils/logger.py
console_handler.setLevel(logging.DEBUG)  # Show all messages
```

## Verification

After installation, verify everything works:

1. **Basic test:**
   ```bash
   python main.py
   ```
   Should show initialization messages and start listening

2. **Voice test:**
   - Say "Hey JP" to wake up
   - Ask "What time is it?"
   - Should respond with current time

3. **System test:**
   - Say "Check system status"
   - Should provide CPU, memory, and disk information

If all tests pass, your installation is successful!
