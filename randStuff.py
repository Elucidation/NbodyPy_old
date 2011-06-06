from numpy import * # http://numpy.scipy.org/ v1.5.1
import random # Must come after numpy
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
    return array([random.uniform(a,b),\
    					random.uniform(a,b),\
    					random.uniform(a,b)])

def randRGB(minVal=0,maxVal=1):
    "(0,0,0) black to (1,1,1) white"
    return (random.uniform(minVal,maxVal),\
    			random.uniform(minVal,maxVal),\
    			random.uniform(minVal,maxVal))
