'''BABIERA,ALEXA | CMPE 103 LAB EXERCISE NO. 1 (PROBLEM 3) | OOP|APRIL 07,2023 '''
# import the necessary module
from pyfiglet import figlet_format
import pygame
from termcolor import colored
import pyfiglet
from colorama import Back, Fore, Style, init
import time

# this function takes in alphabetic characters only from the users


def _user_text(plaintext, key):
    user_key = ''
    i = 0
    for char in plaintext:
        if char.isalpha():
            user_key += key[i % len(key)]
            i += 1
        else:
            user_key += ' '
    return user_key
