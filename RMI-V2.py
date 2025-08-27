import os
import ctypes
from pystyle import Colors, Colorate, Center

os.system("title RMI │ V2")

logo = """
ooooooooo.   ooo        ooooo ooooo 
`888   `Y88. `88.       .888' `888' 
 888   .d88'  888b     d'888   888  
 888ooo88P'   8 Y88. .P  888   888  
 888`88b.     8  `888'   888   888  
 888  `88b.   8    Y     888   888  
o888o  o888o o8o        o888o o888o 
"""

logo = Center.XCenter(logo)
print(Colorate.Vertical(Colors.red_to_black, logo, 1))
print()

k = ctypes.windll.kernel32
mutex = k.CreateMutexW(None, True, "ROBLOX_singletonEvent")

if mutex:
    status_text = "Mutex Released"
    title_status = "ENABLED"
else:
    status_text = "Failed To Create The Mutex"
    title_status = "DISABLED"

os.system(f"title RMI │ V2 │ Status: {title_status}")

box_top    = "╭" + "─" * (len(status_text) + 2) + "╮"
box_middle = f"│ {status_text} │"
box_bottom = "╰" + "─" * (len(status_text) + 2) + "╯"
status_box = f"{box_top}\n{box_middle}\n{box_bottom}"

status_box = Center.XCenter(status_box)
print(Colorate.Vertical(Colors.red_to_black, status_box, 1))

input("\n")

if mutex:
    k.CloseHandle(mutex)
