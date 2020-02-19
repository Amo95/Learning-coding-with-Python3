## Animal is-a class of type object (yes, sort of confuding) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a name
        self.name = name

## Person is-a class of type object (wierd) Person is-a type object
class Person(object):

    def __init__(self, name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

##??
class Employee(Person):

    def __init__(self, name, salary):
        ## super function used to call super class implicitly (without calling the super class)
        super(Employee, self).__init__(name)
        super().__init__(name)
        ## implicit method
        Person(self).__init__(name)
        ## ??
        self.salary = salary

## Fish is-a object type
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has-a pet named satan
mary.pet = satan

## frank is-a Employee with salary 120000
frank = Employee("Frank", 120000)

## frank has-a pet rover
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## henry is-a Halibut
henry = Halibut()
