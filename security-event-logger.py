# B01888101 Tristan Svorai
# Lab exercise 4
# Task 2
# 09/10/2026

from datetime import datetime
import getpass

"""This function checks if the username and password are correct."""
def check_login(username: str, password: str) -> bool:
    correct_username = "admin"
    correct_password = "admin123"

    return username == correct_username and password == correct_password

"""This function logs login events."""
def log_event(username: str, event: str) -> None:
    timestamp = datetime.now()

    print("\n--- Login Event Log ---")
    print(f"Username: {username}")
    print(f"Event: {event}")
    print(f"Timestamp: {timestamp}")
    print("-----------------------\n")

"""This function runs the login checking loop."""
def main():
    print("Login")
    print("==================")

    while True:
        try:
            username = input("Enter username: ").strip()

            if not username:
                print("Error: Username cannot be empty. Please try again.")
                continue

            password = getpass.getpass("Enter password: ")

            if not password:
                print("Error: Password cannot be empty. Please try again.")
                continue

            if check_login(username, password):
                log_event(username, "Successful login")
                print("Access granted!")
                break
            else:
                log_event(username, "Failed login")
                print("Incorrect username or password. Please try again.")

        except Exception as error:
            print(f"An unexpected error occurred: {error}")
            print("Please try again.")

    input("Press Enter to exit...")


if __name__ == "__main__":
    main()