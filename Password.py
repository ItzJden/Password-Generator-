# random modules

import random
import string

print("Welcome to the Random Password Generator!")

# Combine letters, digits, and symbols into one string

characters = string.ascii_letters + string.digits + string.punctuation

# Ask user how long they want the password to be

answer = int(input("Enter desired password length:"))


# Generate password:
# - Pick a random character from 'characters'
# - Repeat that process 'answer' times
# - Join all the picked characters into one string

password = ''.join(random.choice(characters) for _ in range(answer))


print(f"Your generated password is: {password}")