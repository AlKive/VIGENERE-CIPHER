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

'''this function includes the algorithm that is based on vigerene cipher fomula.
 The encryption equation (E) for a Vigenere cipher: 
 #Cipher text, C = E (K, P) = (Pi + Ki) mod 26. 
 Here Ci, Pi, and Ki denote the offset of the ith character of cipher text, plain text, and key.'''


def _encrypt_decrypt_char(PlainTextChar, KeyChar, mode='encrypt'):
    if PlainTextChar.isalpha():
        firstLetter = 'a'
        if PlainTextChar.isupper():
            firstLetter = 'A'
        # Getting the index and ASCII code of the plain text and keyword
        old_char_position = ord(PlainTextChar) - ord(firstLetter)
        key_char_position = ord(KeyChar.lower()) - ord('a')
