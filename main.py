#Cyber security like example (word encycription)

import random
import string
import copy
class Encrypting:
    def __init__(self, text):
        self.text = text
    def message_encrypting(self):
        characters = ' ' + string.punctuation + string.ascii_letters + string.digits
        letters = []
        for letter in characters:
            letters.append(letter)
        cipher = copy.copy(letters)
        random.shuffle(cipher)
        cipher_text = ''
        for l in self.text:
            letter_index = letters.index(l)
            cipher_text += cipher[letter_index]
        return cipher_text
    def __str__(self):
        return f'The {self.text} message is encrypted into {self.message_encrypting()}'



text1 = Encrypting('I sing')
text1.message_encrypting()
print(text1)
#descrypting a message

#cipher_message = input('Enter the message you want to descrypt: ')







