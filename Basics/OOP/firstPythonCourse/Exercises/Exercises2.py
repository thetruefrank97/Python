class SalesPerson:

    total_revenue = 0
    names = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sales_amount = 0
        SalesPerson.names.append(name)

    def make_sale(self, money):
        self.sales_amount = self.sales_amount + money
        SalesPerson.total_revenue += money

    def show(self):
        print(self.name, self.age, self.sales_amount)



if __name__ == "__main__":
    s1 = SalesPerson("Bob", 25)
    s2 = SalesPerson("Ted", 22)
    s3 = SalesPerson("Jack", 27)

    s1.make_sale(1000)
    s2.make_sale(1000)
    s3.make_sale(1000)

    s1.show()
    s2.show()
    s3.show()

    print(SalesPerson.total_revenue)
    print(SalesPerson.names)




