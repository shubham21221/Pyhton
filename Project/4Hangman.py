import random
from 4Words import Words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(4words)
    return word

def hungman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    
    user_letter = input("Guess a letter").upper()
    if user_letter in alphabet - used_letters:
        used_letters.remove(user_letter)
    elif user_letter in used_letters:
        print('you have already used that charater. please try again')
    else:
        print('Invalid character')
        
user_input = input('type someting')
print(user_input)