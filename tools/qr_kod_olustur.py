from time import sleep
from pyfiglet import Figlet
from colorama import Fore, Back, Style
import smtplib
import requests
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import platform
import os
import qrcode

os.system("clear")

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

# QRCode Bilgi

urlmetin = " URL Adresi: "

urlbilgi = input(Fore.RED + urlmetin + Fore.WHITE) 

# QRCode İşlem

leg = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 100,
    border = 4
)

leg.add_data(urlmetin)
leg.make(fit=True)

# Resim Kayıt

resim = leg.make_image(fill_color=(0,153,206),back_color="white")
resim.save("Resimler/QRCode/LegQrCode.png")

print(Fore.GREEN + "QRCode" + Fore.YELLOW +  " Resimler\QRCode" + Fore.GREEN + " Yoluna Kayıt Edilmiştir!" + Fore.WHITE)