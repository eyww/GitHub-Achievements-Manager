import os
import requests
import time
from colorama import Fore
import sys as n
import time as mm
from time import sleep

def KURD(M):
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 100)

KURD('''
        __   __        _____     _          
        \ \ / /       |_   _|   | |         
         \ V /___  _   _| |_   _| |__   ___ 
          \ // _ \| | | | | | | | '_ \ / _ \\
          | | (_) | |_| | | |_| | |_) |  __/
          \_/\___/ \__,_\_/\__,_|_.__/ \___|
                                    
                Author --> #UNIX
                Telegram --> U33UP
                Telegram Channel --> B_G_Y / E4CBM
                Instagram --> E4CB
                Github --> 8LR
''')

good = 0
bad = 0
red = Fore.RED
green = Fore.GREEN
blue = Fore.BLUE

header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

id = input("Enter your Telegram ID >> ")
mm.sleep(1)
token = input("Enter your bot token >> ")
print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')

# Lê usernames do arquivo nomes.txt
try:
    with open("nomes.txt", "r", encoding="utf-8") as file:
        usernames = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    print("Arquivo nomes.txt não encontrado.")
    exit()

webhook_url = "https://discord.com/api/webhooks/1370141816007033003/uHYKVfWD9xGLY2tGkDQ_UCWbyz_Yhv7y4gyS5Oog7HJBfdtUsrGO8dWGvFFN38NIeswO"

for username in usernames:
    sleep(1)
    url = f'https://www.youtube.com/@{username}'
    response = requests.get(url, headers=header)
    if response.status_code == 404:
        print(Fore.GREEN + f"Username Available >> {username}")
        good += 1
        print(f"{green}Good:{good} {blue}/ {red}Bad:{bad}")
        discord_message = {
            "content": f"Username: {username}"
        }
        requests.post(webhook_url, json=discord_message)
    else:
        print(Fore.RED + f"Username Unavailable >> {username}")
        bad += 1
        print(f"{green}Good:{good} {blue}/ {red}Bad:{bad}")
