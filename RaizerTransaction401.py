import random
import sys
import typing
import time
import os
import math
import colour
import telethon
import asyncio
import requests
import colorama
import pyfiglet
import datetime
from os import write
from colorama import Fore, Back, Style, init
class typer:
    def __init__(self, text: str, delay: float = 0.05):
        self.text = text
        self.delay = delay

    def type(self):
        for char in self.text:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(self.delay)
        print(Style.RESET_ALL)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

typing.Type = typing.Union[str, typing.List[str]]
print(Fore.RED + "@Banking.server|> ENTER LOGIN/COSTUMER ID.")
login_id = input(Fore.WHITE + "root@|> ")
time.sleep(0.5)
print(Fore.GREEN + "@accepted|> Input Successfully")
time.sleep(2)
clear()
print(Fore.RED + "@Banking.server|> ENTER CORPORATE ID.")
corporate_id = input(Fore.WHITE + "root@|> ")
time.sleep(0.5)
print(Fore.GREEN + "@accepted|> Input Successfully")
time.sleep(2)
clear()
print(Fore.RED + "@Banking.server|> ENTER ACCOUNT NUMBER.")
account_number = input(Fore.WHITE + "root@|> ")
time.sleep(0.5)
print(Fore.GREEN + "@accepted|> Input Successfully")
time.sleep(2)
clear()
print(Fore.RED + "@Banking.server|> ENTER IFSC CODE.")
ifsc_code = input(Fore.WHITE + "root@|> ")
time.sleep(0.5)
print(Fore.GREEN + "@accepted|> Input Successfully")
time.sleep(2)
clear()
print(Fore.RED + "@Banking.server|> ENTER ACCOUNT NAME. (OPTIONAL)")
account_name = input(Fore.WHITE + "root@|> ")
time.sleep(0.5)
print(Fore.GREEN + "@accepted|> Input Successfully")
time.sleep(2)
clear()
print(Fore.RED + "@Banking.server|> ENTER MICR CODE.")
micr_code = input(Fore.WHITE + "root@|> ")
time.sleep(0.5)
print(Fore.GREEN + "@accepted|> Input Successfully")
time.sleep(2)
clear()
print(Fore.RED + "@Banking.server|> ENTER BANK NAME.")
bank_name = input(Fore.WHITE + "root@|> ")
time.sleep(0.5)
print(Fore.GREEN + "@accepted|> Input Successfully")
time.sleep(2)
clear()
print(Fore.YELLOW + "Successfull Your Data Saved. Get Starting Transaction Mode Wait a Second.")
time.sleep(5)
print(Fore.LIGHTYELLOW_EX + "Starting Transaction Program.")
time.sleep(5)
starting_transaction = input(Fore.WHITE + "System_Ip_root@|> ")
time.sleep(5)
os.system(Fore.GREEN + "pip install lyricsgenius")
time.sleep(5)
os.system(Fore.GREEN + "pip install tgcrypto")
time.sleep(5)
os.system(Fore.GREEN + "pip install pillow")
time.sleep(5)
os.system(Fore.GREEN + "pip install hachoir")
time.sleep(5)
os.system(Fore.GREEN + "pip install gitpython")
time.sleep(5)
os.system(Fore.GREEN + "pip install dnspython")
time.sleep(5)
os.system(Fore.GREEN + "pip install asyncio")
time.sleep(5)
print("--------------------------------------------------------------------")
print(Fore.RED + "@Banking.Phone_Number|> ENTER BANK PHONE NUMBER.")
phone_number = input(Fore.WHITE + "Input_Number_root@|> ")
time.sleep(0.5)
print(Fore.GREEN + "@accepted|> Sending Otp Successfully")
time.sleep(0.5)
sending_otp = input(Fore.WHITE + "Otp_root@|> ")
time.sleep(2)
os.system(Fore.GREEN + "pip install heroku3")
time.sleep(5)
clear()
print("--------------------------------------------------------------------")
print(Fore.RED + "@Banking.Email_ID|> ENTER BANK EMAIL ID.")
Email_id = input(Fore.WHITE + "Input_Email_root@|> ")
time.sleep(0.5)
print(Fore.GREEN + "@accepted|> Sending Email Otp Successfully")
time.sleep(0.5)
sending_otp = input(Fore.WHITE + "Email_Otp_root@|> ")
time.sleep(2)
os.system(Fore.GREEN + "pip install numpy")
time.sleep(5)
clear()
print("--------------------------------------------------------------------")
