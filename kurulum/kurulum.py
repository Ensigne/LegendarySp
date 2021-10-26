from time import sleep
from pyfiglet import Figlet
from colorama import Fore, Back, Style
import requests
import json
import os
banner = 'LegendarySp Tools'
custom_fig = Figlet(font='big')
print(Fore.BLUE + custom_fig.renderText(banner))

sleep(1)

print(Fore.YELLOW)

print("""
#####################################################################
###################### Geliştirici: Yağız#3953  #####################
###################### Sürüm: 1.0V              #####################
#####################################################################
""")

print(Fore.WHITE)

os.system("pip install pyfiglet")
os.system("pip install colorama")
os.system("pip install requests")
os.system("pip install Pillow")
os.system("pip install opencv-python")
os.system("pip install pyzbar")
os.system("pip install qrcode pillow")

print(Fore.RED + "Sistemler Kuruldu !!")
print(Fore.GREEN + "Legendary Başlatılıyor...")
sleep(1)
os.system("python3 main.py")