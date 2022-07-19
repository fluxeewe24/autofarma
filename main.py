from ast import keyword
from telnetlib import OUTMRK
from tkinter import Y, Button
from tkinter.messagebox import YES
from typing import KeysView

def title1():
    from datetime import datetime, timedelta
    import os

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    os.system("title by fluxeewe#4323 / Czas rozpoczęcia " + current_time)

title1()



def farm():

    from pynput.keyboard import Key, Controller
    import time
    from colorama import Fore, Back, Style 
    import os
    import keyboard
    import random
    from datetime import datetime, timedelta

    os.system('cls')
    
    keyboard1 = Controller()

    print(Fore.GREEN + ("\nZa 2 sekundy zacznie się praca :)\n"))
    Style.RESET_ALL

    time.sleep(2)

    work = "!work"
    for char in "!work":
        keyboard1.press(char)
        keyboard1.release(char)
        time.sleep(0.12)
    keyboard1.press(Key.enter)
    if keyboard1.pressed():
        print(Fore.GREEN + "[WYKONANO]", Style.RESET_ALL + work)

    time.sleep(0.4)

    depall = '!dep all'
    for char in "!dep all":
        keyboard1.press(char)
        keyboard1.release(char)
        time.sleep(0.12)
    keyboard1.press(Key.enter)
    if keyboard1.pressed():
        print(Fore.YELLOW + "[WYKONANO]", Style.RESET_ALL + depall)
    
    time.sleep(0.4)

    bal = '!bal'
    for char in "!bal":
        keyboard1.press(char)
        keyboard1.release(char)
        time.sleep(0.12)
    keyboard1.press(Key.enter)
    if keyboard1.pressed():
        print(Fore.YELLOW + "[WYKONANO]", Style.RESET_ALL + bal)
   
    from datetime import datetime, timedelta
    now = datetime.now()
    now_plus_10 = now + timedelta(minutes = 5)
    print(Fore.CYAN + "\nNastępne wykonanie komend: ", now_plus_10)
    Style.RESET_ALL

    time.sleep(300)
    
    farm()

farm()








