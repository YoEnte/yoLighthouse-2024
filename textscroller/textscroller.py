from pyghthouse import Pyghthouse
from textscroller.background.scroller import *
from textscroller.background.text import *
import os
import time

app_name = 'Text Scroller'
username = ''
token = ''

def execute(_username: str, _token: str):
    global username
    global token 

    username = _username
    token = _token
    os.system('cls' if os.name == 'nt' else 'clear')

    print(f"This is the {app_name} Application, welcome!\n")

    run()

def run():
    p = Pyghthouse(username, token)
    Pyghthouse.start(p)

    print("Please wait 1 second...")
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')

    img = Pyghthouse.empty_image()
    p.set_image(img)

    string = input("Input our display text: ")

    text1 = Text(string, "classic")
    scroller1 = Scroller(text1, 10, (255, 255, 255))

    #Pyghthouse.stop(p)

    time.sleep(1)

    while True:
        time.sleep(1 / scroller1.tps)
        os.system('cls' if os.name == 'nt' else 'clear')

        scroller1.next_frame()
        p.set_image(scroller1.current_frame)
