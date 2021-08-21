class Wing(object):
    def __init__(self, ratio):
        self.ration = ratio

    def fly(self):
        if self.ration > 1:
            print("Weeee this is fun")
        elif self.ration == 1:
            print("This is hard work, but im flying")
        else:
            print("I think I will just walk")


class Duck(object):
    def __init__(self):
        self._wing = Wing(1.8)

    def walk(self):
        print("Waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the waters lovely")

    def quack(self):
        print("Quack, Quack, Quack")

    def fly(self):
        self._wing.fly()


class Penguin(object):
    def __init__(self):
        self.fly = self.aviate

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but its a bit chilly this far south")

    def quack(self):
        print("Are you 'avin' a laugh? Im a penguin")

    def aviate(self):
        print("I won the lottery and bought a learjet")


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()


class Mallard(Duck):
    pass


class Flock(object):
    def __init__(self):
        self.flock = []

    def add_duck(self, duck: Duck) -> None:
        fly_method = getattr(duck, "fly", None)
        # if isinstance(duck, Duck):
        if callable(fly_method):
            self.flock.append(duck)
        else:
            raise TypeError("Cannot add duck, are you sure its not a " + str(type(duck).__name__))

    def migrate(self):
        problem = None
        for duck in self.flock:
            try:
                duck.fly()
                raise AttributeError("Testing exception handler in migrate") # TODO remove this before release
            except AttributeError as e:
                print("One duck down")
                problem = e
            if problem:
                raise problem


if __name__ == "__main__":
    donald = Duck()
    donald.fly()


