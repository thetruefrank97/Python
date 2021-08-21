import random


class User:
    def __init__(self, username):
        self.username = username
        self.password = ""
        self.phone = ""
        self.security_questions = {}
        self.blocked = False

    def sign_up(self):
        self._enter_pasword()
        self.phone = input("Enter your phone number: ")
        print("Answer these security questions that will help you login if you forget your password")
        with open("questions.txt", "r") as file:
            questions = file.readline()
        random.shuffle(questions)

        answer0 = input(questions[0])
        answer1 = input(questions[1])

        self.security_questions[questions[0]] = answer0
        self.security_questions[questions[1]] = answer1

    def log_in(self):
        if self.blocked:
            print("This account is blocked")
            return

        psswd_attempts = 1
        password = input("Enter password: ")
        while password != self.password:
            if psswd_attempts == 3:
                self.blocked = True
                print("Sorry, no more tries!!!!\n")
                break

            print("Wrong Password")
            password = input("Enter correct password: ")
            psswd_attempts += 1
        else:
            print(f"Welcome, {self.username}")

    def forgot_password(self):
        pass

    def _enter_password(self):
        while True:
            password = input("Enter password: ")
            if len(password) < 7:
                print("Password should have at least 7 characters")
                continue
            a = d = w = 0
            for ch in password:
                if ch.isalpha():
                    a += 1
                elif ch.isdigit():
                    d += 1
                elif ch.isspace():
                    w += 1

            if a < 2:
                print("Password should have at least 2 letters")
            if d == 0:
                print("Password should have at least one digit")
                continue
            if w > 0:
                print("Whitespace not allowed")
                continue

            if len(password) < 12:
                print("Weak password")
                response = input("Do you want to enter another password: (yes/no)")
                if response == "yes":
                    continue
                else:
                    break
            else:
                print("Strong password")
                break
        self.password = password