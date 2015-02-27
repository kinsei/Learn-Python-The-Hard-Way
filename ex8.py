formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter %("one", "two", "three", "four")
print formatter %(formatter, formatter, formatter, formatter)
print formatter %(
    "I had ths thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)  

# A few of the mistakes i made on this was the last print statement
# I missed one of the ',' 
# I also left out ')' on the second to last print statement
# And I also left out the '(' on the last print statement
# I had miss read the exercise and combined the last two statements
