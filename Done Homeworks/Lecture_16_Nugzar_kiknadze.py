class Human:
    number_of_hands = 2
    name = "Levani"

    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    @staticmethod
    def say_hi():
        print("Hello!")

    def represent(self):
        print(f"Hello, My Name is {self.name}")

human1 = Human("Nika", "Tsitskishvili", 28)
human2 = Human("Elene", "Sixarulidze", 25)

human1.represent()
human2.represent()

