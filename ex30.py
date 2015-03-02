# Define variables
people = 30 
cars = 40 
buses = 15

# if cars are greater than people print "We should take the cars". If cars are 
# less than people print "We should not take the cars". If nither is True or
# if  bouth are True print "We cant decide"
if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

# If buses are greater than cars print "thats to many buses", if buses are less
# than cars print "Maybe we should takemthe buses". if nither is True or if both are True print "We cant decide"
if buses > cars:
    print "hats too many buses."
elif buses < cars:
    print "Maybe we could take the buses"
else:
    print "We still cant decide"

# if people are greater than the buses print "Alright, lets take the buses". if
# anything else print"Fine lets stay home then"
if people > buses:
    print "Alright, let's just take the buses"
else:
    print "Fine, let's stay home then"
