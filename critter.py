
class Critter(object):
    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "glad"
        elif 5 <= unhappiness <= 10:
            m = "happy"
        elif 11 <= unhappiness <= 15:
            m = "sad"
        else:
            m = "furious"
        return m

    def talk(self):
        print("My name is ", self.name, "and I'm", self.mood, "now.\n")
        self.__pass_time()

    def eat(self, food=4):
        print("Yummy, thank you!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        print("Hurrah!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    crit_name = input("Enter pet's name:")
    crit = Critter(crit_name)
    choice = None
    while choice != "0":
        print("""
        0-quit
        1-listen to pet
        2-feed the pet
        3-play with your pet     
        """)
        choice = input("What you choose?")

        if choice == "0":
            print("Goodbye")
        elif choice == "1":
            crit.talk()
        elif choice == "2":
            crit.eat()
        elif choice == "3":
            crit.play()
        else:
            print("Unfortunately", choice, "is not a valid choice")


main()
