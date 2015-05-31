# Composition

class Other(object):
    
    def override(self):
        print "Other override()"

    def implicit(self):
        print "Other implicit()"

    def altered(self):
        print "Other altered"

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "Child override()"

    def altered(self):
        print "Child, before altered()"
        self.other.altered()
        print "Child after altered()"

son = Child()
son.implicit()
son.override()
son.altered()
