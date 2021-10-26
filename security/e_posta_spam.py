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

# E-Posta Spam

mailinfo1 = "1-) Hedef E-Posta: "
mailinfo2 = "2-) Konu: "
mailinfo3 = "3-) E-Posta Metini:  "
mailinfo4 = "!! Döngüyü Durdurmak İçin 'CTRL+C' Kısa Yolunu Kullanın !! "




custom_kosul2 = Figlet(font='block')
print(Fore.BLUE + custom_kosul2.renderText("E-Posta"))
print(Fore.GREEN)
sleep(1)
mailspam1 = input(mailinfo1 + Fore.WHITE)
mailspam2 = input(Fore.RED + mailinfo2 + Fore.WHITE)
mailspam3 = input(Fore.RED + mailinfo3 + Fore.WHITE)
print()
mailspam4 = print(Fore.RED + mailinfo4 + Fore.WHITE)


# E-Posta Spam İşlemleri

etekrarla = 1

etekrarla2 = 100
while etekrarla<=etekrarla2:
    mail = smtplib.SMTP("smtp.gmail.com",587)          
    mail.ehlo()
    mail.starttls()

    mail.login("legendarysptool@gmail.com", "legendarysp1111@@@")  

    mesaj = MIMEMultipart()

    mesaj["From"] = " legendarysptool@gmail.com"        
    mesaj["To"] = " " + mailspam1          

    mesaj["Subject"] = mailspam2 

    body = mailspam3

    body_text = MIMEText(body, "plain")  
    mesaj.attach(body_text)

    mail.sendmail( mesaj["From"], mesaj["To"], mesaj.as_string())

sleep(1)

print(Fore.YELLOW)

print("E-Posta: " + Fore.WHITE + mailspam1 + Fore.YELLOW)

print("Konu: " + Fore.WHITE + mailspam2 + Fore.YELLOW)

print("Mesaj: " + Fore.WHITE + mailspam3 + Fore.YELLOW)