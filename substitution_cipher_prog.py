import random
import string
import time

chars = " " + string.punctuation + string.digits + string.ascii_letters  # Returns a string of chars
chars = list(chars)  # Returns a list containing strings 
key = chars.copy()  # Returns a shallow copy of the chars list

random.shuffle(key)  # Shuffle the list of key

# ENCRYPT
plain_text = input("Enter a message to encrypt: ") #original message
cipher_text = ""  # encrypted message

for char in plain_text:  # Iterate over every character in plain txt string
    index = chars.index(char)  # find the index of every char from plain text string within chars list
    cipher_text = cipher_text + key[index]  # char appended to cipher  txt string, refer to key list and get char in the index

print()
print(f"Original message: {plain_text}\n")
print("Encrypting...\n")
time.sleep(3)
print(f"Encryted message: {cipher_text}\n")

# DECRYPT
time.sleep(5)
cipher_text = input("Enter a message to decrypt: ") #original message
plain_text = ""  # decrypted message

for char in cipher_text:
    index = key.index(char)
    plain_text = plain_text + chars[index]

print()
print(f"Original message: {cipher_text}\n")
print("Decrypting...\n")
time.sleep(3)
print(f"Encryted message: {plain_text}")