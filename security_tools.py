# B01888101 Tristan Svorai
# Lab exercise 5
# # Task 5
# 20/10/2026

import random
import string

"""This function checks if the password follows the password policy."""
def check_password(password: str) -> bool:

    if len(password) < 10:
        return False

    if " " in password:
        return False

    uppercase = 0
    lowercase = 0
    numbers = 0
    symbols = 0

    allowed_symbols = "!@#$%"

    for char in password:
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1
        elif char.isdigit():
            numbers += 1
        elif char in allowed_symbols:
            symbols += 1
        else:
            return False

    return (uppercase >= 1 and
            lowercase >= 1 and
            numbers >= 2 and
            symbols >= 1)


"""This function validates an IPv4 address."""
def validate_ip(ip):

    ip = ip.strip()

    if "." not in ip or ip.count(".") != 3:
        return False

    parts = ip.split(".")

    if len(parts) != 4:
        return False

    for part in parts:

        if not part.isdigit():
            return False

        number = int(part)

        if number < 0 or number > 255:
            return False

    return True


"""This function generates a random password that meets the password policy."""
def generate_password() -> str:

    length = random.randint(10, 16)

    # Guarantee the minimum password requirements
    password_chars = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.digits),
        random.choice("!@#$%")
    ]

    # Fill the remaining password length
    all_chars = string.ascii_letters + string.digits + "!@#$%"

    for i in range(length - 5):
        password_chars.append(random.choice(all_chars))

    # Shuffle characters so requirements aren't always in the same positions
    random.shuffle(password_chars)

    password = "".join(password_chars)

    return password

#main function to test the functions in the module
def main():
    generated_password = generate_password()

    print("\nYour randomly generated password is:")
    print(generated_password)

    print("\nPassword valid:", check_password(generated_password))

    print("\nValid IP:", validate_ip("192.168.10.15"))
    print("Invalid IP:", validate_ip("192.168.10.300"))


if __name__ == "__main__":
    main()
