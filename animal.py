class Animal:
    def __init__(self, name, sleep_duration):
        self.name = name
        self.sleep_time = sleep_duration

    def sleep(self):
        print(f"{self.name} sleeps for hours {self.sleep_time}")
    
    def eat(self):
        print(f"{self.name} is eating")

    def drink(self):
        print(f"{self.name} is drinking")


class Frog(Animal):
    def __init__(self, name, sleep_duration):
        super().__init__(name, sleep_duration)

    def jump(self):
        print(f"{self.name} is jumping")


class Dog(Animal):
    def __init__(self, name, sleep_duration):
        super().__init__(name, sleep_duration)

    def bark(self):
        print("Woof Woof!")


frog = Frog("froggie", 7)
mammal = Animal("silly goobber", 22)

frog.jump()
frog.eat()

mammal.drink()