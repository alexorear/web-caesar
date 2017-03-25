import string
#Encrypt a message using Caeser Cipher

def alphabet_position(letter):
    """Where is letter located in alpha"""
    letter = letter.lower()
    alpha = string.ascii_lowercase #"abcdefghijklmnopqustuvwxyz"
    return alpha.find(letter)

def rotate_character(char, rot):
    """rotate char to a newchar"""
    alpha = string.ascii_lowercase #"abcdefghijklmnopqustuvwxyz"
    new_pos = (alphabet_position(char) + int(rot)) % 26  #only 26 letters in alpha must wrap around
    new_char = alpha[new_pos]

    if char.islower() == True:  #return original char case
        return new_char.lower()
    else:
        return new_char.upper()

def encrypt(text, rot):
    """User input text to be encrypted usins top 2 functions"""
    encryption = ""
    for char in text:
        if char.isalpha() == True:
            new_char = rotate_character(char, rot)
            encryption += new_char
        else:
            encryption += char
    return encryption
