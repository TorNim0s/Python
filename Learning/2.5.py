class Animal:
    def __init__(self, name, hunger = 0, zoo_name = "Hayaton", talksound = "None"):
        """
        :param name: name of the animal -- for example dog named Fluffy
        :param hunger: amount of hunger the animal currently on
        :param talksound: the talk sound that the animal has
        _zoo_name: the name of the zoo the animal is on
        """
        self._name = name
        self._hunger = hunger
        self._talksound = talksound
        self._zoo_name = zoo_name

    def get_name(self):
        """
        :return: the name of the animal
        """
        return self._name

    def is_hungry(self):
        """
        :return: the amount of hunger
        """
        return self._hunger > 0

    def feed(self):
        """
        :return: reduce the amount of hunger by 1
        """
        self._hunger -= 1

    def talk(self):
        """
        :return: the talk sound of the animal
        """
        return self._talksound

    def special_method(self):
        """
        :return: used as a method to other instances as a special method to call there unique once
        """
        pass

    def __str__(self):
        """
        :return: the name of the zoo when the instance is called without any method.
        """
        return self._zoo_name

class Dog(Animal):
    def __init__(self, name, hunger = 0):
        """
        :param name: name of the dog
        :param hunger: amount of hunger
        """
        Animal.__init__(self, name, hunger, "woof woof")

    def special_method(self):
        """
        :return: get the method from the superclass and forward it to the unique method fetch_stick
        """
        return self.fetch_stick()

    def fetch_stick(self):
        """
        :return: return the unique word when the method called
        """
        return "There you go, sir!"

### other class has the same explain as the dog ###

class Cat(Animal):
    def __init__(self, name, hunger = 0):
        Animal.__init__(self, name, hunger, "meow")

    def special_method(self):
        return self.chase_laser()

    def chase_laser(self):
        return "Meeeeow"


class Skunk(Animal):
    def __init__(self, name, hunger = 0, stink_count = 6):
        Animal.__init__(self, name, hunger, "tsssss")
        self._stink_count = stink_count

    def special_method(self):
        return self.stink()

    def stink(self):
        return "Dear lord!"

class Unicorn(Animal):
    def __init__(self, name, hunger = 0):
        Animal.__init__(self, name, hunger, "Good day, darling")

    def special_method(self):
        return self.sing()

    def sing(self):
        return "I’m not your toy..."

class Dragon(Animal):
    def __init__(self, name, hunger = 0, color = "Green"):
        Animal.__init__(self, name, hunger, "Raaaawr")
        self._color = color

    def special_method(self):
        return self.breath_fire()

    def breath_fire(self):
        return "$@#$#@$"

def main():
    zoo_lst = [] # create a list of the zoo animals
    zoo_lst.append(Dog("Brownie", 10))
    zoo_lst.append(Cat("Zelda", 3))
    zoo_lst.append(Skunk("Stinky"))
    zoo_lst.append(Unicorn("Keith", 7))
    zoo_lst.append(Dragon("Lizzy", 1450))

    zoo_lst.append(Dog("Doggo", 80))
    zoo_lst.append(Cat("Kitty", 80))
    zoo_lst.append(Skunk("Stinky Jr.", 80))
    zoo_lst.append(Unicorn("Clair", 80))
    zoo_lst.append(Dragon("McFly", 80))
    """
        adding to the list the animals by the class there suppose to be in
    """

    for animal in zoo_lst: # loop on the animals on the zoo list
        if animal.is_hungry(): # check if the animal is hungery
            print("{} {}".format(animal.__class__.__name__, animal.get_name())) # print the animal class and his name
            while animal.is_hungry(): # loop until the animal is not hungery any more
                animal.feed() # feed the animal
            print(animal.talk()) # print animal talk
            print(animal.special_method()) # print animal special method

    print(zoo_lst[0]) # print the name of the zoo

if __name__ == "__main__":
    main()

