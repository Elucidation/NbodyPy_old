import random

random.seed(42969249)

consonents = "bcdfghjklmnpqrstvwxyz" # includes y
vowels = "aeiou" # not including y

def randShortName():
    " Returns 3 letter word w/ consonent+vowel+consonent format"
    return (random.choice(consonents) + \
    			random.choice(vowels) + \
    			random.choice(consonents)  ).capitalize()

def randArr3(a,b):
    "Returns random pos/vel in box (a,a,a) - (b,b,b)"
    return array([random.randrange(a,b),\
    					random.randrange(a,b),\
    					random.randrange(a,b)])

def randRGB(minVal=0,maxVal=1):
    "(0,0,0) black to (1,1,1) white"
    return (random.randrange(minVal,maxVal),\
    			random.randrange(minVal,maxVal),\
    			random.randrange(minVal,maxVal))
