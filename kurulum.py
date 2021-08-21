from time import sleep
from pyfiglet import Figlet
from colorama import Fore, Back, Style
import requests
import json
import os
banner = 'Legendary Spam'
custom_fig = Figlet(font='big')
print(Fore.BLUE + custom_fig.renderText(banner))

sleep(1)

print(Fore.YELLOW)

print("""
#####################################################################
###################### Geliştirici: Yağızz#1881 #####################
###################### Sürüm: 1.0V              #####################
#####################################################################
""")

print(Fore.WHITE)

os.system("pip install pyfiglet")
os.system("pip install colorama")
os.system("pip install requests")

print(Fore.RED + "Sistemler Kuruldu !!")
print(Fore.GREEN + "Legendary Başlatılıyor...")
sleep(1)
os.system("python main.py")
