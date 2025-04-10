import string
import secrets

# Check if password contains at least one uppercase letter
def contains_upper(password: str) -> bool:
    for char in password:
        if char.isupper():
            return True
    return False

# Check if password contains at least one symbol
def contains_symbols(password: str) -> bool:
    for char in password:
        if char in string.punctuation:
            return True
    return False

# Generate a password with specified length and options
def generate_password(length: int, symbols: bool, uppercase: bool) -> str:
    combination: str = string.ascii_lowercase + string.digits

    if symbols:
        combination += string.punctuation
    if uppercase:
        combination += string.ascii_uppercase

    combination_length = len(combination)
    new_password: str = ""

    for _ in range(length):
        new_password += combination[secrets.randbelow(combination_length)]

    return new_password

# Main program block
if __name__ == '__main__':
    new_pass: str = generate_password(length=10, symbols=False, uppercase=False)
    specs: str = f'U: {contains_upper(new_pass)}, S: {contains_symbols(new_pass)}'
    print(f'{new_pass} ({specs})')
