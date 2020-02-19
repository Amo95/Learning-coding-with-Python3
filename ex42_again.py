# an animals properties
class Animals(object):

    def __init__(self, name):
        self.name = name
        print(f"{self.name} is an animal")


# what type of animal is this?
    def mammal(self):
        print("Therefore, {} is a mammal".format(self.name))

    def reptile(self):
        print(self.name, "is a reptile")

# it can be a cat too
class Cats(Animals):

    def __init__(self, name):
        super(Cats, self).__init__(name)
        print(self.name, "is a cat")

class Dogs(Animals):

    def __init__(self, name):
        super().__init__(name)
        print(f"{self.name}, is a dog")

class Fish(Animals):

    def __init__(self, name):
        Animals.__init__(self, name) # implicitly calling the super class
        print(f"{self.name} is a fish")

class Snake(Fish):

    def __init__(self, name, length):
        super(Fish, self).__init__(name)
        self.length = None
        print("{} is a snake with length {}".format(self.name, length))
try:
    import os
    def main():
        # do the animal have a name?
        anime = input("Enter animal here (cat/dog/fish/snake)>> ")
        anime_name = input("Enter animal name (eg. Joe)>> ")

        if anime == "cat":
            cat = Cats(anime_name)
            cat.mammal()

        elif anime == "dog":
            dog = Dogs(anime_name)
            dog.mammal()

        elif anime == "fish":
            fish = Fish(anime_name)
            fish.reptile()

        elif anime == "snake":
            snake = Snake(anime_name, 220)
            snake.reptile()

        else:
            pass

    if __name__ == '__main__':
        main()

except KeyboardInterrupt:
    print("\n\nThank you for using...")
    exit(1)
