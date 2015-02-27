from sys import argv

script, filename = argv

#to see what would happen i added 'w+r' to the line below
#it worked rather well, keep this in minde it will be usefull
txt = open(filename)  

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again."
file_again = raw_input("> ")

# if you add 'w+r' to the first you might need to add here as well
#although i did not try it
text_again = open(file_again)

print text_again.read()
