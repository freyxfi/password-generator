import json
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def save_password(social_media, password):
    try:
        with open('passwords.json', 'r') as file:
            passwords = json.load(file)
    except FileNotFoundError:
        passwords = {}

    passwords[social_media] = password

    with open('passwords.json', 'w') as file:
        json.dump(passwords, file, indent=4)

def main():
    social_media = input("Enter the name of the social media platform: ")
    length = int(input("Enter the desired length of the password: "))

    password = generate_password(length)
    save_password(social_media, password)

    print(f"Generated password for {social_media}: {password}")

if __name__ == "__main__":
    main()
