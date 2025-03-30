users = []
user = input("Please create a user ID: ")
users.append((user))

passwords = []
key = input("Please create a password: ")
passwords.append((key))

start = input("Would you like to login?(y/n): ")
if start == "y":
    login_id = input("Please enter your user ID: ")
    login_pass = input("Please enter your password: ")
    if login_id == users[0] and login_pass == passwords[0]:
         print("Access Granted!")
    else:print("Invalid credentials.")

if start == "n":
    print("Goodbye.")