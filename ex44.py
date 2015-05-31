# This is ecercise 44 in learn python the hard way
# the focus on this exercise is inheritance vs. composition
# there are three ways thay the parent and child classes can interact
# 1. Actions on the child imply an action on the parent
# 2. Actions on the child override the actionson the parent
# 3. Actions on the child alter the actions on the parent

class Parent(object):
    
    def implicit(self):
        print "Parent implicit()"

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
