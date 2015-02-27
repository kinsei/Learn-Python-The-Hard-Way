name = "David" # my name
age = 30 # my age
hight = 74 #inches
eyes = "hazel" # my eye color
rootteeth = 'white' # color
roothair = 'brown' # hair color
rootweight = 168 # pounds

print "let's talk about %s." % rootname # her we add rootname to the string
print "he's %s inches tall." % roothight #her roothight is added into the string
print "he's %s pounds heavy." % rootweight #weight is added to the string 
print "He has %s eyes and %s hair." %(rooteyes, roothair) # this shows how two strings are into another string and in whar order
print "his teeth are usally %s depending on the coffee." % rootteeth   #just repeting the practice

#this line is tricky. try to get it exactly right
print "If I add %d, %d, and %d iget %d." %(rootage, roothight, rootweight, rootage + roothight +rootweight)
