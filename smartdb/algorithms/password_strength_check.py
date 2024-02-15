# Password Strength Checker
import sqlite3

def password_strength_check(password):
    if len(password) < 8:
        print('Warn: password {} is less than 8 chars.'.format(password))
        return False
    
    if not any(char.isupper() for char in password):
        print('Warn: password {} does not contain uppercase letters.'.format(password))
        return False
    
    if not any(char.islower() for char in password):
        print('Warn: password {} does not contain lowercase letters.'.format(password))
        return False
    
    if not any(char.isdigit() for char in password):
        print('Warn: password {} does not contain digits.'.format(password))
        return False
    
    special_chars = "!@#$%^&*()_-+=<>?/{}[]|\~"
    if not any(char in special_chars for char in password):
        print('Warn: password {} does not contain special characters.'.format(password))
        return False
    
    # ...
    return True