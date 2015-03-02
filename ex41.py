# This is exercise 41 in Learn Python The Hard Way
# This was writen for Python 2.6

# Word Drills

# * Class - tell python to make a new kind of thing
# * Object - two meanings: 1) the most basic kind of thing. 2)an instance of something
# * Instance - what you get when you tell python to create a class
# * def - How to define a function in a class
# * self - inside the function of a class, self is a variable for the instance/object being accessed
# * inheritance - the concept that one class can inherit traits from another class, much like you and your parents
# * composition - the concept that a class can be composed of other classes as parts, much like how a car has wheels
# * attribute - a property classes have that are from composition and are usually variables
# * is-a - A phrase to say that something inherits from another, as in a "salmon" is-a "fish"
# * has-a - A phrase to say that something is composed of other things or has-a trait, as in "a salmon has-a mouth"


# Phrase Drill

# class X(Y) "Make a class named X that is a Y."
# class X(object):
#    def __init__(self, J) "class X has-a __init__ that takes self and J parameters"
# class X(object):
#    def M (self,J) " class X has a function named M that takes self and J parameters"
# foo = X() "set foo to an instance of class X"
# foo.M(J) "from foo get the M function, and call it with parameters self and J"
# foo.K = Q "From foo get the K attribute, and set to Q"

import random
from urllib import  urlopen
import sys

WORD_URL = "http://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%",
    "class %%%(object):\n\tdef __init__(self,***)":
        "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% hs-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
        "set *** to an  instance of class %%%",
    "***.***(@@@)":
        "From *** get the *** function, and call it with parameters self, @@@",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
PHRASE_FIRST = False
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True

# load up the words from the website
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())

def convert(snippet, phrase):
    class_name = [w.capitalize() for w in
                  random.sample(WORDS, snippet.count("%%%"))]
    other_names = random.sample(WORDS, snippet.count("***"))
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.appned(', '.join(random.sample(WORDS, param_count)))

    for sentence in snippet, phrase:
        results = sentence[:]

        # fake class name
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # fake parameter
        for word in param_names:
            result - result.replace("@@@", word, 1)

        results.append(result)

        #keep going untill they hit ctrl + d

try:
    while True:
        snippets = PHRASES.keys()
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question, answer = answer, question

                print (question)

                input("> ")
                print ("Answer: %s\n\n" % answer)
except EOFError:
    print ("\nGoodbye")
















