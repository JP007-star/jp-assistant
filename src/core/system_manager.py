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
    def find_files_by_extension(extension: str, directory: str = None, system_wide: bool = True) -> str:
        """Find files with specific extension across system or specific directory"""
        try:
            files = []
            search_locations = []
            
            if directory:
                # Search specific directory
                search_locations = [directory]
            elif system_wide:
                # Search common user directories and system locations
                user_home = os.path.expanduser("~")
                search_locations = [
                    os.path.join(user_home, "Documents"),
                    os.path.join(user_home, "Downloads"), 
                    os.path.join(user_home, "Music"),
                    os.path.join(user_home, "Videos"),
                    os.path.join(user_home, "Pictures"),
                    os.path.join(user_home, "Desktop"),
                    "C:\\Users\\Public",
                    "C:\\Program Files",
                    "C:\\Program Files (x86)"
                ]
                # Add current directory
                search_locations.append(os.getcwd())
            else:
                # Just current directory
                search_locations = [os.getcwd()]
            
            total_searched = 0
            locations_found = []
            
            for search_dir in search_locations:
                if not os.path.exists(search_dir):
                    continue
                    
                try:
                    # Walk through directory and subdirectories with limits
                    for root, dirs, filenames in os.walk(search_dir):
                        # Skip system directories that might cause issues
                        dirs[:] = [d for d in dirs if not d.startswith('.') and 
                                 d not in ['System32', 'Windows', 'Program Files', '__pycache__']]
                        
                        for filename in filenames:
                            if filename.lower().endswith(extension.lower()):
                                full_path = os.path.join(root, filename)
                                files.append(full_path)
                                if search_dir not in locations_found:
                                    locations_found.append(os.path.basename(search_dir))
                                
                                # Limit to prevent overwhelming results
                                if len(files) >= 50:  # Increased limit for system-wide search
                                    break
                        
                        total_searched += 1
                        # Prevent searching too deep
                        if total_searched > 1000:
                            break
                            
                        if len(files) >= 50:
                            break
                    
                    if len(files) >= 50:
                        break
                        
                except (PermissionError, OSError):
                    # Skip directories we can't access
                    continue
            
            if not files:
                search_desc = "entire system" if system_wide else "current directory"
                return f"No {extension} files found in {search_desc}"
            
            file_count = len(files)
            
            # Group files by directory for better organization
            file_locations = {}
            for file_path in files[:20]:  # Show details for first 20
                dir_name = os.path.dirname(file_path)
                base_dir = os.path.basename(dir_name) if dir_name else "Root"
                if base_dir not in file_locations:
                    file_locations[base_dir] = []
                file_locations[base_dir].append(os.path.basename(file_path))
            
            result = [f"🔍 Found {file_count} {extension} files across {len(locations_found)} locations"]
            
            if file_count > 50:
                result.append(f"📊 Showing first 50 results (found {file_count} total)")
            
            result.append("📁 File locations:")
            for location, files_in_loc in list(file_locations.items())[:5]:  # Show top 5 locations
                sample_files = files_in_loc[:3]  # Show 3 files per location
                result.append(f"   📂 {location}: {', '.join(sample_files)}")
                if len(files_in_loc) > 3:
                    result.append(f"      ... and {len(files_in_loc) - 3} more")
            
            if len(file_locations) > 5:
                result.append(f"   📂 ... and {len(file_locations) - 5} more locations")
                
            return "\n".join(result)
            
        except Exception as e:
            return f"Error searching for {extension} files: {str(e)}"
    
    @staticmethod
    def search_files_by_name(filename: str, system_wide: bool = True) -> str:
        """Search for files by name across system"""
        try:
            files = []
            search_locations = []
            
            if system_wide:
                # Search common user directories
                user_home = os.path.expanduser("~")
                search_locations = [
                    os.path.join(user_home, "Documents"),
                    os.path.join(user_home, "Downloads"), 
                    os.path.join(user_home, "Desktop"),
                    os.path.join(user_home, "Music"),
                    os.path.join(user_home, "Videos"),
                    os.path.join(user_home, "Pictures"),
                    os.getcwd()
                ]
            else:
                search_locations = [os.getcwd()]
            
            for search_dir in search_locations:
                if not os.path.exists(search_dir):
                    continue
                    
                try:
                    for root, dirs, filenames in os.walk(search_dir):
                        # Skip system directories
                        dirs[:] = [d for d in dirs if not d.startswith('.') and 
                                 d not in ['System32', 'Windows', '__pycache__']]
                        
                        for file in filenames:
                            if filename.lower() in file.lower():
                                full_path = os.path.join(root, file)
                                files.append(full_path)
                                
                                if len(files) >= 30:
                                    break
                        
                        if len(files) >= 30:
                            break
                            
                except (PermissionError, OSError):
                    continue
                
                if len(files) >= 30:
                    break
            
            if not files:
                return f"No files found containing '{filename}'"
            
            file_count = len(files)
            result = [f"🔍 Found {file_count} files containing '{filename}'"]
            
            # Show organized results
            for i, file_path in enumerate(files[:10], 1):
                dir_name = os.path.basename(os.path.dirname(file_path))
                file_name = os.path.basename(file_path)
                result.append(f"   {i}. {file_name} (in {dir_name})")
            
            if file_count > 10:
                result.append(f"   ... and {file_count - 10} more files")
                
            return "\n".join(result)
            
        except Exception as e:
            return f"Error searching for files: {str(e)}"
    
    @staticmethod
    def get_drive_usage() -> str:
        """Get usage information for all available drives"""
        try:
            import string
            drives_info = []
            
            # Check all possible drive letters
            for letter in string.ascii_uppercase:
                drive_path = f"{letter}:\\"
                if os.path.exists(drive_path):
                    try:
                        drive_usage = psutil.disk_usage(drive_path)
                        total_gb = drive_usage.total // (1024**3)
                        used_gb = drive_usage.used // (1024**3)
                        free_gb = drive_usage.free // (1024**3)
                        used_percent = (drive_usage.used / drive_usage.total) * 100
                        
                        drives_info.append(f"💿 Drive {letter}: {used_gb}GB/{total_gb}GB ({used_percent:.1f}% used, {free_gb}GB free)")
                    except:
                        drives_info.append(f"💿 Drive {letter}: Unable to access")
            
            if not drives_info:
                return "No drives found"
                
            return "\n".join(drives_info)
            
        except Exception as e:
            return f"Error getting drive information: {str(e)}"

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
