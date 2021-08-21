# Create a script that lets the user submit a password until they have satisfied three conditions:
# Password contains atleast one numbers
# contains an uppercase letter
# it is atleast 5 characters long
# Print out message "Password is not fine" if the user didnt create a correct password
# Before asking for password, ask for a username

def UsernameAndPasswordChecker():
    while True:
        username = input("Please type in a username: ")
        with open("users.txt", "r") as file:
            users = file.readlines()
            users = [i.strip("\n") for i in users]
        if username in users:
            print("Username exists")
            continue
        else:
            print("Username is fine")
            break

    while True:
        notes = []
        password = input("Please enter a password: ")
        if not any(i.isdigit() for i in password):
            notes.append("You dont have a digit character")
        if not any(i.isupper for i in password):
            notes.append("You dont have an upper case character")
        if not len(password) < 5:
            notes.append("Your password is not long enough")
        if len(password) > 5:
            print("Password is fine")
            break
        else:
            print("Your sign in had the next problems")
            for note in notes:
                print(note)


UsernameAndPasswordChecker()
