# This is written for python 2.7
# This is exercise 18 in Learn Python The Hard Way

# this on is like your scripts with argv
 
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# Ok, that *arg is actually pointless, we can justn do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" %  (arg1, arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

#this takes no arguments
def print_none():
    print "I got nothin'."

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
