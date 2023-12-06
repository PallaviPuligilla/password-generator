import random

def generate_password(length=10):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    symbol = '()[]{};_#*.'
    number = '0123456789'
    all_chars = lower + upper + number + symbol
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def generate_multiple_passwords(count=5, length=20):
    passwords = [generate_password(length) for _ in range(count)]
    return passwords

def main():
    print('WELCOME TO THE PASSWORD GENERATOR!')
    length = int(input("Enter the desired length for the passwords: "))
    count = int(input("Enter the number of passwords to generate: "))
    passwords = generate_multiple_passwords(count, length)
    print("\nGenerated passwords:")
    for password in passwords:
        print(password)

if __name__ == "__main__":
    main()
