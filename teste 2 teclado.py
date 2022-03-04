import keyboard
from os import system as S
from time import sleep
x = 1
while (x >= 1) :
    if keyboard.read_key() == "p":
        print("You pressed p")
        S('mspaint')
        x = 0
        sleep(0.5)
        x = 1