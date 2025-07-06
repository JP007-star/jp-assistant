"""
System Manager Module - Handles system operations and information
"""

import os
import psutil
import subprocess
import webbrowser
from typing import Dict, List, Optional
from . import config

class SystemManager:
    """Handles system information and operations"""
    
    @staticmethod
    def get_system_info() -> Optional[Dict[str, float]]:
        """Get comprehensive system information"""
        try:
            # Get system metrics
            cpu_percent = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            
            # Get disk usage for Windows (C: drive)
            disk = psutil.disk_usage('C:')
            
            return {
                'cpu': cpu_percent,
                'memory_used': memory.percent,
                'memory_total': memory.total // (1024**3),  # GB
                'memory_available': memory.available // (1024**3),  # GB
                'disk_used': disk.used // (1024**3),  # GB
                'disk_total': disk.total // (1024**3),  # GB
                'disk_free': disk.free // (1024**3),  # GB
                'disk_percent': (disk.used / disk.total) * 100
            }
        except Exception as e:
            print(f"{config.ERROR_MESSAGES['system_info_failed']}: {e}")
            return None
    
    @staticmethod
    def get_system_status() -> str:
        """Get formatted system status string"""
        info = SystemManager.get_system_info()
        if not info:
            return config.ERROR_MESSAGES["system_info_failed"]
        
        return (f"System Status: CPU {info['cpu']:.1f}%, "
                f"Memory {info['memory_used']:.1f}% used "
                f"({info['memory_available']} GB available), "
                f"Disk {info['disk_used']} GB used out of {info['disk_total']} GB "
                f"({info['disk_free']} GB free)")
    
    @staticmethod
    def get_cpu_usage() -> str:
        """Get CPU usage information"""
        info = SystemManager.get_system_info()
        if not info:
            return config.ERROR_MESSAGES["system_info_failed"]
        
        return f"CPU usage is currently at {info['cpu']:.1f} percent"
    
    @staticmethod
    def list_files(directory: str = None) -> str:
        """List files in specified directory"""
        try:
            target_dir = directory or os.getcwd()
            files = os.listdir(target_dir)[:config.MAX_FILES_TO_SHOW]
            
            if not files:
                return f"The directory {target_dir} appears to be empty."
            
            file_list = ", ".join(files)
            more_text = "and more" if len(os.listdir(target_dir)) > config.MAX_FILES_TO_SHOW else ""
            
            return f"In {target_dir}, I can see: {file_list} {more_text}".strip()
            
        except Exception as e:
            print(f"{config.ERROR_MESSAGES['file_access_failed']}: {e}")
            return config.ERROR_MESSAGES["file_access_failed"]
    
    @staticmethod
    def find_files_by_extension(extension: str, directory: str = None) -> str:
        """Find files with specific extension"""
        try:
            target_dir = directory or os.getcwd()
            files = []
            
            # Walk through directory and subdirectories
            for root, dirs, filenames in os.walk(target_dir):
                for filename in filenames:
                    if filename.lower().endswith(extension.lower()):
                        files.append(os.path.join(root, filename))
                        if len(files) >= config.MAX_FILES_TO_SHOW:
                            break
                if len(files) >= config.MAX_FILES_TO_SHOW:
                    break
            
            if not files:
                return f"No {extension} files found in {target_dir}"
            
            file_count = len(files)
            sample_files = [os.path.basename(f) for f in files[:5]]
            
            return f"Found {file_count} {extension} files. Examples: {', '.join(sample_files)}"
            
        except Exception as e:
            return f"Error searching for {extension} files: {str(e)}"

class ProgramLauncher:
    """Handles launching external programs"""
    
    PROGRAMS = {
        'notepad': ['notepad.exe'],
        'calculator': ['calc.exe'],
        'paint': ['mspaint.exe'],
        'cmd': ['cmd.exe'],
        'powershell': ['powershell.exe'],
        'explorer': ['explorer.exe'],
        'control': ['control.exe'],  # Control Panel
    }
    
    @staticmethod
    def launch_program(program_name: str) -> str:
        """Launch a system program"""
        program_name = program_name.lower()
        
        if program_name in ProgramLauncher.PROGRAMS:
            try:
                subprocess.Popen(ProgramLauncher.PROGRAMS[program_name])
                return f"Opening {program_name.title()} for you!"
            except Exception as e:
                return f"Couldn't open {program_name}: {str(e)}"
        else:
            available = ", ".join(ProgramLauncher.PROGRAMS.keys())
            return f"I can open: {available}. What would you like to open?"
    
    @staticmethod
    def open_browser(url: str = "https://www.google.com") -> str:
        """Open web browser with specified URL"""
        try:
            webbrowser.open(url)
            return "Opening your web browser!"
        except Exception as e:
            return f"Couldn't open browser: {str(e)}"
    
    @staticmethod
    def search_web(query: str) -> str:
        """Perform web search"""
        if not query.strip():
            return "What would you like me to search for?"
        
        try:
            search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            webbrowser.open(search_url)
            return f"Searching for '{query}' on Google!"
        except Exception as e:
            return f"{config.ERROR_MESSAGES['search_failed']}: {str(e)}"
