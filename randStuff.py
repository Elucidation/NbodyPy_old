from random import *
from visual import * # Vpython for 2.7 needed

consonents = "bcdfghjklmnpqrstvwxyz" # includes y
vowels = "aeiou" # not including y

random.seed(1)

def randShortName():
    " Returns 3 letter word w/ consonent+vowel+consonent format"
    return (choice(consonents)+ choice(vowels) + choice(consonents)).capitalize()

def randArr3(a,b):
    "Returns random pos/vel in box (a,a,a) - (b,b,b)"
    return array([randRange(a,b),randRange(a,b),randRange(a,b)])


def randRGB(minVal=0,maxVal=1):
    "(0,0,0) black to (1,1,1) white"
    return (randRange(minVal,maxVal),randRange(minVal,maxVal),randRange(minVal,maxVal))

def randRange(a,b):
    "Returns random value in range a to b including a & b"
    return random.random()*(b-a)+a
