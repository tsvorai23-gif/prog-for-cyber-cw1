# B01888101 Tristan Svorai
# Lab exercise 2
# Task 8
# 02/10/2026

"""This program implements a security tool with three main functions"""

CORRECT_USERNAME = "admin"
CORRECT_PASSWORD = "Pa$$w0rd"


"""1. Security Event Counter: Counts correct and incorrect password attempts
and calculates the percentage of incorrect attempts."""

def security_event_counter():
    """This function counts correct and incorrect password attempts
    and calculates the percentage of incorrect attempts."""

    correct = 0
    incorrect = 0

    print("\n--- Security Event Counter ---")

    for attempt in range(10):

        password = input("Enter password: ")

        if password == CORRECT_PASSWORD:
            correct += 1
        else:
            incorrect += 1

    percentage = (incorrect / 10) * 100


    print("\nCorrect passwords:", correct)
    print("Incorrect passwords:", incorrect)
    print("Incorrect percentage:", percentage, "%")

    if percentage > 50:
        print("ALERT: More than 50% of passwords were incorrect!")


"""2. Brute-Force Simulation: Simulates a brute-force attack by allowing
the user to guess a password up to a maximum number of attempts."""

def brute_force_simulation():
    """This function simulates a brute-force attack by allowing the user
    to guess a password up to a maximum number of attempts."""

    password = "secret123"
    max_attempts = 5
    attempts = 0

    print("\n--- Brute-Force Simulation ---")

    while attempts < max_attempts:

        guess = input("Enter password guess: ")
        attempts += 1

        if guess == password:
            print("Password found!")
            print("Attempts used:", attempts)
            return

        print("Incorrect password.")

    print("Maximum attempts reached.")
    print("Brute-force simulation stopped.")


"""3. Login Authentication: Authenticates users by checking their
credentials against the correct username and password."""

def login_authentication():
    """This function authenticates users by checking their credentials
    against the correct username and password."""

    max_attempts = 3
    failed_attempts = 0

    print("\n--- Login Authentication ---")

    while failed_attempts < max_attempts:

        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
            print("Authentication successful!")
            return True

        failed_attempts += 1

        print("Authentication failed.")

        if failed_attempts < max_attempts:
            print("Please try again.")

    print("Account frozen for 24 hours.")
    return False


"""This function displays the security menu and allows the user to
select different functionalities of the security tool."""

def security_menu():
    """This function displays the security menu and allows the user
    to select different functionalities of the security tool."""

    while True:
        """This loop displays the security menu and handles user input
        for selecting different functionalities."""

        print("\n===== SECURITY MENU =====")
        print("1. Security Event Counter")
        print("2. Brute-Force Simulation")
        print("3. Login Authentication")
        print("4. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            security_event_counter()

        elif choice == "2":
            brute_force_simulation()

        elif choice == "3":
            login_authentication()

        elif choice == "4":
            print("Thank you for using the security tool")
            break

        else:
            print("Invalid choice. Please select 1-4.")


"""This is the main function that starts the security tool program."""

def main():

    print("===== SECURITY TOOL =====")

    if login_authentication():
        security_menu()


main()