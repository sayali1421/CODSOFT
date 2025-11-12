# Password Generator Program

import random
import string

# Ask user for password length
length = int(input("Enter how long you want your password to be: "))

# Combine letters, numbers and symbols
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

all_characters = letters + numbers + symbols

# Generate random password
password = ""
for i in range(length):
    password += random.choice(all_characters)

# Show the password
print("Your new password is:", password)
