# This script creates a simple username and password login system.

# Stores usernames and passwords in separate lists
users = []
passwords = []

def set_credentials():
    # Ask user to create an ID and password
    user = input("Please create a user ID: ")
    users.append((user))

    password = input("Please create a password: ")
    passwords.append((password))

def start_login():
    # Prompts user to enter previously set credentials
    start = input("Would you like to login?(y/n): ")
    if start.lower() == "y":
        login_id = input("Please enter your user ID: ")
        login_pass = input("Please enter your password: ")
        if login_id == users[0] and login_pass == passwords[0]:
            print("Access Granted!")
        else:print("Invalid credentials.")
    if start.lower() == "n":
        print("Goodbye.")

# --- Run the program ---
set_credentials()
start_login()