# So what is the difference between a class and an object?
# this is an important thing to understand in OOP languages.


# The way it is put in Learn Python The Hard Way is like this:
# fish is a class salmon is a class and if you had three salmon and named one joe, one john, and one marry.
# Marry would be an object.
# SO the way to think about it is like this, its a little backwards though.
# Marry is a type of salmon, salmon is a type of fish.
# in this book it is explained like this
# a fish is a class, meaning it is not a real thing, but rather a word we attach to instances of things
# with similar attributes.
#        does it have fins?
#                 |
#                 |
#     no _________|_________  yes
#     |                         |
#     |                  does it have gills?
#     |                         |
#     |                 no______|_______ yes
#     |                 |                  |
#     |                 |          does it live in water?
#     |                 |                  |
#     |                 |           no _____|______ yes
#     |                 |          |                 |
#     |_________________|______not a fish      then its a fish


# then lets say a professor comes along and classifies the fish further and says its a salmon
# the salmon is also a class because there is certain criteria that makes up a salmon
# now lest say some kid comes along and says that salmon there is names marry. now there is nothing that
# makes up a marry. to criteria that needs to be met to be a marry. there for it is an object not a class.
# to help you understand this there is are two phrases : is-a and has-a
# you use the phrase is-a when you talk about objects and classes being related to each other by a class
# relationship.
# you use the phrase has-a when you talk about objects and classes that are related only because they reference
# each other


## animal is-a object(yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

##dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ##dog has-a name
        self.name = name

    def barks():
        print ("Woof")

## cat is-a animal
class Cat(Animal):
    def __init__(self, name):
        ## cat has-a name
        self.name = name


## person is-a object
class Person(object):
    def __init__(self, name):
        ## person has-a name
        self.name = name

        ##person has a pet of some kind
        self.pet = None

## employee is-a person
class Employee(Person):
    def __init__(self, name, salary):
        ## ?? hum whats this strange magic?? this is how you run the __init__
        ## method of a parent class reliably
        super(Employee, self).__init__(name)
        ## employee has-a salary
        self.salary = salary

## fish is-a object
class Fish(object):
    pass

## salmon is-a fish
class Salmon(Fish):
    pass

## halibut is-a fish
class Halibut(Fish):
    pass

## rover is-a dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is a person
mary = Person("Mary")

## marry has-a pet
mary.pet = satan

## frank is-a employee
frank = Employee("Frank", 120000)

## frank has-a pet
frank.per = rover

## fliper is a fish
fliper = Fish()

## course is-a salmon
course = Salmon()

## harry is-a halibut
harry = Halibut





































