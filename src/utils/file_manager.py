"""
File management utilities for JP Assistant
"""

import json
import os
from typing import Dict, Any, Optional

class FileManager:
    """Handles file operations for JP Assistant"""
    
    def __init__(self, data_dir="data"):
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)
    
    def save_json(self, filename: str, data: Dict[str, Any]) -> bool:
        """Save data to JSON file"""
        try:
            filepath = os.path.join(self.data_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error saving {filename}: {e}")
            return False
    
    def load_json(self, filename: str) -> Optional[Dict[str, Any]]:
        """Load data from JSON file"""
        try:
            filepath = os.path.join(self.data_dir, filename)
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return {}
        except Exception as e:
            print(f"Error loading {filename}: {e}")
            return {}
    
    def save_memory(self, memories: Dict[str, str]) -> bool:
        """Save memory data to file"""
        return self.save_json("memory.json", memories)
    
    def load_memory(self) -> Dict[str, str]:
        """Load memory data from file"""
        data = self.load_json("memory.json")
        return data if data else {}
    
    def save_settings(self, settings: Dict[str, Any]) -> bool:
        """Save user settings"""
        return self.save_json("settings.json", settings)
    
    def load_settings(self) -> Dict[str, Any]:
        """Load user settings"""
        data = self.load_json("settings.json")
        return data if data else {}
