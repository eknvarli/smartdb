# generate_strong_password | SmartDB

import string
import random


def generate_strong_password(length=10):
    # Characters to choose from including ! and ?
    chars = string.ascii_letters + string.digits + "!?"
    
    # Ensure both ! and ? are in the password
    password = ''.join(random.choice(chars) for _ in range(length - 2))
    password += random.choice("!?")  # Add either ! or ? at the end
    password += random.choice("!?")  # Add the other one at the end

    # Shuffle the password to make it more random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    
    return password