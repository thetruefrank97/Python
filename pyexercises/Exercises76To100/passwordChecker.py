# Create a script that lets the user submit a password until they have satisfied three conditions:
# Password contains atleast one numbers
# contains an uppercase letter
# it is atleast 5 characters long
# Print out message "Password is not fine" if the user didnt create a correct password


def passwordValidator():
    notes = []
    while True:
        password = input("Please enter a password: ")
        if not any(i.isdigit() for i in password):
            notes.append("Your password doesnt have a digit")
        if not any(i.isupper() for i in password):
            notes.append("Your password doesnt have an uppercase letter")
        if not len(password) >= 5:
            notes.append("Your password is not longer than 5 characters")
        if len(notes) == 0:
            print("Your password is fine my friend")
            break
        else:
            print("Your password has the next problems")
            for note in notes:
                print(note)


passwordValidator()
