#in this line i define the variable cars and asighn it the value of 100
cars = 100
# in this line i define the variable space in a car and give it a floating point value of 4.0
space_in_a_car = 4.0
#number of drivers
drivers = 30
#this line i define the variable passangers and give it the value of 90
passengers = 90
#cars not driven takes the cars and drivers and finds out how many cars are not driven
cars_not_driven = cars - drivers
#this line gives the amount of cars that can be driven 
cars_driven = drivers 
# in this line we find the capacity by multiplying the cars driven by the space in the car
carpool_capacity = cars_driven * space_in_a_car
#this line finds the average passanger in the car  
average_passengers_per_car = passengers / cars_driven

#the following lines prints all the above information
print"There are", cars, "caars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today"
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
