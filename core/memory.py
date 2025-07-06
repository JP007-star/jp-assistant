import json
from pathlib import Path

MEMORY_FILE = Path("data/memory.json")

def remember(text):
    MEMORY_FILE.parent.mkdir(exist_ok=True)
    memory = []
    if MEMORY_FILE.exists():
        memory = json.loads(MEMORY_FILE.read_text())
    memory.append(text)
    MEMORY_FILE.write_text(json.dumps(memory, indent=2))

def recall():
    if not MEMORY_FILE.exists():
        return "Nothing stored yet."
    memory = json.loads(MEMORY_FILE.read_text())
    return "\n".join(f"- {item}" for item in memory)