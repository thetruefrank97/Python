class Person:

    species = "Homo Sapiens"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name, self.age)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if 20 < new_age < 80:
            self._age = new_age
        else:
            raise ValueError("Age must be between 20 and 80")


if __name__ == "__main__":
    p = Person("Frank", 23)
    p.age = 34
    p.display()
    print(p.species)
