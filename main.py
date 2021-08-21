from time import sleep
from pyfiglet import Figlet
from colorama import Fore, Back, Style
import requests
import json

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

sleep(1)

print("Seçenekler Yükleniyor...")

sleep(1)

# Seçenekler

secenek1metin = "1-) SMS Spam İşlemi \n"

secenek2metin = "2-) Çıkış İşlemi \n"

secenek1 = input(secenek1metin + Fore.RED + secenek2metin + Fore.WHITE )


print(Fore.RED)


# Koşullar
 
kosul1 = "1"
kosul2 = "2"

# SMS Spam

smsinfo1 = "1-) Ülke Kodu: "
smsinfo2 = "2-) Telefon Numarası: "
smsinfo3 = "3-) Gönderilecek Metin:  "



if secenek1 == kosul1:
    smspam1 = input(smsinfo1 + Fore.WHITE)
    smspam2 = input(Fore.RED + smsinfo2 + "+ " + smspam1 + Fore.WHITE)
    smspam3 = input(Fore.RED + smsinfo3 + Fore.WHITE)







# Tool Çıkış
if secenek1 == kosul2:
    print("Çıkış Yapılıyor...")
    sleep(1)