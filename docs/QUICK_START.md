# Quick Start Guide - JP Assistant

## 🚀 Get Started in 2 Minutes

### 1. Install Dependencies
```bash
pip install -r requirements_new.txt
```

### 2. Run the Assistant
```bash
python main.py
```

### 3. Start Using Voice Commands

**Wake up the assistant:**
- Say: "Hey JP" or "Hello"

**Basic commands:**
- "What time is it?"
- "What's today's date?"
- "Check system status"
- "Open calculator"

**Put to sleep:**
- Say: "Bye JP" or "Goodbye"

**Exit completely:**
- Type: "quit" or press Ctrl+C

## 🎯 Essential Voice Commands

| Category | Command Examples |
|----------|------------------|
| **Time & Date** | "What time is it?", "What's today's date?" |
| **System Info** | "Check system status", "CPU usage", "Disk space" |
| **Programs** | "Open calculator", "Open notepad", "Open browser" |
| **Web Search** | "Search for Python tutorials", "Google weather" |
| **Memory** | "Remember my name is John", "What is my name?" |
| **Files** | "List files", "Find MP3 files", "Show PDF files" |
| **Fun** | "Tell me a joke", "Sing a song" |
| **Help** | "Help", "What can you do?" |

## ⚙️ Quick Configuration

If microphone isn't working:

1. **Find your microphone:**
   - Look for console output showing microphone indices
   - Try speaking and see which responds

2. **Update config:**
   ```python
   # Edit src/core/config.py
   MICROPHONE_INDEX = 3  # Change to your microphone number
   ```

## 🎤 Voice Control Flow

```
💤 Assistant Sleeping
    ↓ Say "Hey JP"
🟢 Assistant Awake
    ↓ Give commands
🎯 Assistant Responds
    ↓ Say "Bye JP"
💤 Assistant Sleeping
```

## 🔧 Troubleshooting

**No response to wake word:**
- Speak louder and clearer
- Check microphone permissions
- Try "Hello" instead of "Hey JP"

**Speech not recognized:**
- Check internet connection
- Minimize background noise
- Speak at normal pace

**Can't find microphone:**
- Run: `python -c "import pyaudio; p=pyaudio.PyAudio(); [print(f'{i}: {p.get_device_info_by_index(i)[\"name\"]}') for i in range(p.get_device_count())]"`

## 🎉 You're Ready!

Your JP Assistant is now ready to help with:
- ✅ System monitoring and information
- ✅ File operations and search
- ✅ Web search and program launching
- ✅ Memory storage and conversations
- ✅ Entertainment and productivity tasks

Say "Hey JP" and start exploring! 🚀
