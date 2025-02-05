import os
import platform
import psutil
import time
from colorama import init, Fore, Style

# main
init(autoreset=True)

def get_system_info(): 
    disk_path = 'C:\\' if platform.system() == "Windows" else '/'
    info = {
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Kernel": platform.release(),
        "Architecture": platform.machine(),
         "CPU": get_cpu_info(),
        "CPU Cores": psutil.cpu_count(logical=False),
        "Memory": f"{round(psutil.virtual_memory().total / (1024 ** 3))} GB",
        "Disk Usage": f"{psutil.disk_usage(disk_path).percent}% used",
        "Uptime": f"{round((time.time() - psutil.boot_time()) / 3600, 2)} hours"
    }
    return info

def get_os_name():
    """Detect the operating system or Linux distribution."""
    system = platform.system()
    if system == "Linux":
        try:
            with open("/etc/os-release") as f:
                for line in f:
                    if line.startswith("ID="):
                        
                        distro_id = line.split("=")[1].strip().replace('"', '')
                        return distro_id.capitalize()  
        except FileNotFoundError:
            pass
    return system   
 #the ascii art built using ascii artist(my lastest tool)
def get_ascii_art(os_name):
    """Return ASCII art based on the OS."""
    ascii_art = {
        "Ubuntu": """
      _   _ _                 _           ____ _______        __
| | | | |__  _   _ _ __ | |_ _   _  | __ )_   _\ \      / /
| | | | '_ \| | | | '_ \| __| | | | |  _ \ | |  \ \ /\ / / 
| |_| | |_) | |_| | | | | |_| |_| | | |_) || |   \ V  V /  
 \___/|_.__/ \__,_|_| |_|\__|\__,_| |____/ |_|    \_/\_/   
        """,
        "Arch": """
                          _       ____ _______        __
  __ _ _ __ ___| |__   | __ )_   _\ \      / /
 / _` | '__/ __| '_ \  |  _ \ | |  \ \ /\ / / 
| (_| | | | (__| | | | | |_) || |   \ V  V /  
 \__,_|_|  \___|_| |_| |____/ |_|    \_/\_/   
        """,
        "Fedora": """
            _____        _                   ____ _______        __
|  ___|__  __| | ___  _ __ __ _  | __ )_   _\ \      / /
| |_ / _ \/ _` |/ _ \| '__/ _` | |  _ \ | |  \ \ /\ / / 
|  _|  __/ (_| | (_) | | | (_| | | |_) || |   \ V  V /  
|_|  \___|\__,_|\___/|_|  \__,_| |____/ |_|    \_/\_/   
        """,
        "Manjaro": """
__  __              _                   ____ _______        __
|  \/  | __ _ _ __  (_) __ _ _ __ ___   | __ )_   _\ \      / /
| |\/| |/ _` | '_ \ | |/ _` | '__/ _ \  |  _ \ | |  \ \ /\ / / 
| |  | | (_| | | | || | (_| | | | (_) | | |_) || |   \ V  V /  
|_|  |_|\__,_|_| |_|/ |\__,_|_|  \___/  |____/ |_|    \_/\_/   
                  |__/                        
        """,
        "Raspbian": """
 ____                 _     _             
|  _ \ __ _ ___ _ __ | |__ (_) __ _ _ __  
| |_) / _` / __| '_ \| '_ \| |/ _` | '_ \ 
|  _ < (_| \__ \ |_) | |_) | | (_| | | | |
|_| \_\__,_|___/ .__/|_.__/|_|\__,_|_| |_|
               |_|     
        """,
        "Debian": """
           ____       _     _               ____ _______        __
|  _ \  ___| |__ (_) __ _ _ __   | __ )_   _\ \      / /
| | | |/ _ \ '_ \| |/ _` | '_ \  |  _ \ | |  \ \ /\ / / 
| |_| |  __/ |_) | | (_| | | | | | |_) || |   \ V  V /  
|____/ \___|_.__/|_|\__,_|_| |_| |____/ |_|    \_/\_/ 
        """,
        "Mint": """
            __  __ _       _     ____ _______        __
|  \/  (_)_ __ | |_  | __ )_   _\ \      / /
| |\/| | | '_ \| __| |  _ \ | |  \ \ /\ / / 
| |  | | | | | | |_  | |_) || |   \ V  V /  
|_|  |_|_|_| |_|\__| |____/ |_|    \_/\_/   
                                           
        """,
       "Zorin": """
       _____          _         ____ _______        __
|__  /___  _ __(_)_ __   | __ )_   _\ \      / /
  / // _ \| '__| | '_ \  |  _ \ | |  \ \ /\ / / 
 / /| (_) | |  | | | | | | |_) || |   \ V  V /  
/____\___/|_|  |_|_| |_| |____/ |_|    \_/\_/ 

     """,
     "Popos": """
     ____                             ____ _______        __
|  _ \ ___  _ __  ___  ___  ___  | __ )_   _\ \      / /
| |_) / _ \| '_ \/ __|/ _ \/ __| |  _ \ | |  \ \ /\ / / 
|  __/ (_) | |_) \__ \ (_) \__ \ | |_) || |   \ V  V /  
|_|   \___/| .__/|___/\___/|___/ |____/ |_|    \_/\_/   
           |_|      

           """,
           "opensuse": """
                                                      ____ _______        __
  ___  _ __   ___ _ __  ___ _   _ ___  ___  | __ )_   _\ \      / /
 / _ \| '_ \ / _ \ '_ \/ __| | | / __|/ _ \ |  _ \ | |  \ \ /\ / / 
| (_) | |_) |  __/ | | \__ \ |_| \__ \  __/ | |_) || |   \ V  V /  
 \___/| .__/ \___|_| |_|___/\__,_|___/\___| |____/ |_|    \_/\_/   
      |_|                                                         
        
      """,
      "slackware": """
        
           _            _                              ____ _______        __
 ___| | __ _  ___| | ____      ____ _ _ __ ___  | __ )_   _\ \      / /
/ __| |/ _` |/ __| |/ /\ \ /\ / / _` | '__/ _ \ |  _ \ | |  \ \ /\ / / 
\__ \ | (_| | (__|   <  \ V  V / (_| | | |  __/ | |_) || |   \ V  V /  
|___/_|\__,_|\___|_|\_\  \_/\_/ \__,_|_|  \___| |____/ |_|    \_/\_/ 

              """,
              "centos": """
                          _              ____ _______        __
  ___ ___ _ __ | |_ ___  ___  | __ )_   _\ \      / /
 / __/ _ \ '_ \| __/ _ \/ __| |  _ \ | |  \ \ /\ / / 
| (_|  __/ | | | || (_) \__ \ | |_) || |   \ V  V /  
 \___\___|_| |_|\__\___/|___/ |____/ |_|    \_/\_/   
             """,
             "redhat": """

                       _ _           _     ____ _______        __
 _ __ ___  __| | |__   __ _| |_  | __ )_   _\ \      / /
| '__/ _ \/ _` | '_ \ / _` | __| |  _ \ | |  \ \ /\ / / 
| | |  __/ (_| | | | | (_| | |_  | |_) || |   \ V  V /  
|_|  \___|\__,_|_| |_|\__,_|\__| |____/ |_|    \_/\_/

        """,

        "gentoo": """
                       _                ____ _______        __
  __ _  ___ _ __ | |_ ___   ___   | __ )_   _\ \      / /
 / _` |/ _ \ '_ \| __/ _ \ / _ \  |  _ \ | |  \ \ /\ / / 
| (_| |  __/ | | | || (_) | (_) | | |_) || |   \ V  V /  
 \__, |\___|_| |_|\__\___/ \___/  |____/ |_|    \_/\_/   
 |___/    
       
       """,
       " endeavouros": """


                      _                                           
  ___ _ __   __| | ___  __ ___   _____  _   _ _ __ ___  ___ 
 / _ \ '_ \ / _` |/ _ \/ _` \ \ / / _ \| | | | '__/ _ \/ __|
|  __/ | | | (_| |  __/ (_| |\ V / (_) | |_| | | | (_) \__ \
 \___|_| |_|\__,_|\___|\__,_| \_/ \___/ \__,_|_|  \___/|___/
                                                            
 ____ _______        __
| __ )_   _\ \      / /
|  _ \ | |  \ \ /\ / / 
| |_) || |   \ V  V /  
|____/ |_|    \_/\_/   
   
 """,
 "artix": """

         _   _        _     _            
  __ _ _ __| |_(_)_  __ | |__ | |___      __
 / _` | '__| __| \ \/ / | '_ \| __\ \ /\ / /
| (_| | |  | |_| |>  <  | |_) | |_ \ V  V / 
 \__,_|_|   \__|_/_/\_\ |_.__/ \__| \_/\_/  

 """


    }
    return ascii_art.get(os_name, "Unknown OS")
def get_cpu_info():
     
    system = platform.system()
    if system == "Linux":
        try: 
            with open("/proc/cpuinfo") as f:
                for line in f:
                    if "model name" in line:
                        return line.split(":")[1].strip()
        except FileNotFoundError:
            pass   
        try:
            import subprocess
            result = subprocess.run(["sysctl", "-n", "machdep.cpu.brand_string"], stdout=subprocess.PIPE, text=True)
            return result.stdout.strip()
        except Exception:
            pass

     
    return platform.processor() or "Unknown"

def display_neofetch():
    """Display system information with ASCII art."""
    os_name = get_os_name()   
    ascii_art = get_ascii_art(os_name)  
    system_info = get_system_info()

    print(Fore.CYAN + ascii_art)   
    for key, value in system_info.items():
        print(f"{Fore.GREEN}{key}: {Fore.WHITE}{value}")   

if __name__ == "__main__":
    try:
        display_neofetch()
    except Exception as e:
        print(f"An error occurred: {str(e)}") 
        