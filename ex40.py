# This lesson is the difference between classes modules and objects
# These are very important to understand not just in python but for all OOP languages


# Modules are like dictionaries

# a dictionary is created and used to map one thing to another
# So the basic idea of a module is "get x from y"
# 1. a module is a python file with a function or variable
# 2. you then import that file example: import socket
# 3. you can access the functions and variables in that module with the '.' operator example: socket.socket
# there is a very common pattern in python
# 1. take a key=value style container
# 2. get something out of it by the keys name

# Classes are like Modules

# A class is a way to take a group of functions and data and place them inside a container so you can access them with the '.' opperator
# an example of a simple class

# class MyStuff(object):
#    def __init__(self):
#        self.tangerine = "and now a thousand years between"
#    def apple(self):
#        print "I am classy apples"

# WHY USE CLASSES OVER MODULES
# classes should be used over modules because when you import a module you can only use it ONCE! With a class you can use it
# multiple times in your code.

# Objects are like mini imports

# there has to be a similar concept to import but for classes.
# this is called "instantiate"
# "instantiate" just means create
# when you instantiate a class you get an object

# to do this call the class like its a function
# example:

# thing = MyStuff()
# thing.apple()
# print thing.tangerine

# the first line is the instantiate
# there is a sequence of events in Python when you do this
# 1. Python looks for MyStuff() and sees that its a class you have defined
# 2. Python crafts an empty object with all the functions you have specified in the class using def.
# 3. Python then looks to see if you made a __init__ function, if you have, it calls that function to
#    initialise your newly created empty object
# 4. The MyStuff function __init__ gets an extra variable self, which is the empty object python made
#    it can be set just like you would a module, dict, or other object
# 5. In this case, I set self.tangerine to a song lyric and then initialized the object
# 6. Python then takes this newly minted object and assigns it to the thing variable for me to work with

# remember tis not giving you the class, but instead using the class like a blueprint

# in all honesty classes work like this
# classes are like blueprints of definitions for creating new mini-modules
# the resulting created mini-module is called an object and you then assign it to a variable to work with it

# getting things from thing
# there are three ways to get things from things
# 1. dict style
#    mystuff['apples']
# 2. modules
#    mystuff.apples()
#    print mystuff.tangerine
# 3. class style
#    thing = MyStuff()
#    thing.apples()
#    print thing,tangerine

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print (line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
print (" ")
bulls_on_parade.sing_me_a_song()

