class bankAccount:


    def set_details(self, name):
        self.name = name
        self.balance = 0

    def display(self):
        print(self.name)
        print(self.balance)

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount


account = bankAccount()
account.set_details("Frank")
account.deposit(200)
account.withdraw(10)
account.display()