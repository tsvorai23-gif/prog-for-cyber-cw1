# B01888101 Tristan Svorai
# Lab exercise 5
# # Task 5
# 20/10/2026

import getpass
import security_tools

def main():
    #ask the user to input a password
    password = getpass.getpass("Enter a password: ")

    #ask the user to input an IP address
    ip_address = input("Enter an IP address: ")

    #. Check if the password and IP address are valid. If the password provided by the user is not strong, suggest a randomly generated strong password
    if not security_tools.check_password(password):
        print("The password is not strong enough.")
        strong_password = generate_strong_password()
        print(f"Suggested strong password: {strong_password}")
    else:
        print("The password is strong.")

    if not security_tools.validate_ip(ip_address):
        print("The IP address is not valid.")
    else:
        print("The IP address is valid.")
    # Call the functions from the module and display the results.
    print("\nPassword valid:", security_tools.check_password(password))
    print("IP address valid:", security_tools.validate_ip(ip_address))

    input("Press Enter to exit...")

#generate a strong password using the function from security_tools.py
def generate_strong_password():
    return security_tools.generate_password()

if __name__ == "__main__":
    main()