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
    
        if mode == 'encrypt':
            new_char_position = (old_char_position + key_char_position) % 26
        else:  # this section if for the decryption, but i've decided that i will only display the encypted/ciphertext at the end
            new_char_position = (old_char_position -
                                 key_char_position + 26) % 26
        return chr(new_char_position + ord(firstLetter))
    return PlainTextChar

def encrypt(plaintext, key):
    ciphertext = ''
    user_key = _user_text(plaintext, key)
    for PlainTextChar, KeyChar in zip(plaintext, user_key):
        ciphertext += _encrypt_decrypt_char(PlainTextChar, KeyChar)
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    user_key = _user_text(ciphertext, key)
    for ciphertext_char, KeyChar in zip(ciphertext, user_key):
        plaintext += _encrypt_decrypt_char(ciphertext_char,
                                           KeyChar, mode='decrypt')
    return plaintext
