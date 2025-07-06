#!/usr/bin/env python3
"""
JP Assistant - Enhanced Voice-Activated AI Assistant
Main entry point for the application

Author: JP Assistant Team jayaprasad.jp.m@gmail.com
Version: 2.0
"""

import sys
import os

# Add src directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from jp_assistant import main

if __name__ == "__main__":
    main()
