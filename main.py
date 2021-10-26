import os
from time import sleep
from pyfiglet import Figlet
from colorama import Fore, Back, Style
import smtplib
import requests
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import platform

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

sleep(1)

print("Seçenekler Yükleniyor...")

sleep(1)

# Seçenekler

secenek1metin = "1-) Yardımcı Toolar \n"

secenek2metin = "2-) Hack Tooları \n"

secenek3metin = "3-) Çıkış İşlemi \n"

secenek1 = input(secenek1metin + secenek2metin + Fore.RED + secenek3metin + Fore.WHITE )


print(Fore.RED)


# Koşullar
 
kosul1 = "1"
kosul2 = "2"
kosul3 = "3"


# Seçenek İşlem

# Hack Tooları

if secenek1 == kosul1:
    os.system("clear")
    os.system("python tools/yardimci.py")

if secenek1 == kosul2:
    os.system("clear")
    os.system("python security/hack.py")





# Tool Çıkış
if secenek1 == kosul3:
    print("Çıkış Yapılıyor...")
    sleep(1)
    print(Fore.WHITE)