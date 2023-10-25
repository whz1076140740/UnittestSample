###########################################

#
# 1. In this exercise we will make a "Patient" class
#
# The Patient class should store the state of
# a patient in our hospital system.
#
#
# 1.1)
# Create a class called "Patient".
# The constructor should have two parameters
# (in addition to self, of course):
#
# 1. name (str)
# 2. symptoms (list of str)
#
# the parameters should be stored as attributes
# called "name" and "symptoms" respectively


class Patient:
    def __init__(self, name, symptoms):
        self.name = name

        self._symptoms = []
        if symptoms != None:
            self._symptoms = symptoms
        
        self._test = []
        self._result = []

#
# 1.2)
# Create a method called "add_test"
# which takes two paramters:
# 1. the name of the test (str)
# 2. the results of the test (bool)
#
# This information should be stored somehow.

    def add_test(self, test, result):
        self._test.append(test)
        self._result.append(result)
        #it's sort by add sequence, 
        #if add "covid" with true at beginning and add "covid" with false at later time
        #probability is taken by later added time
        

#
# 1.3)
# Create a method called has_covid()
# which takes no parameters.
#
# "has_covid" returns a float, between 0.0
# and 1.0, which represents the probability
# of the patient to have Covid-19
#
# The probability should work as follows:
#
# 1. If the user has had the test "covid"
#    then it should return .99 if the test
#    is True and 0.01 if the test is False
# 2. Otherwise, probability starts at 0.05
#    and ncreases by 0.1 for each of the
#    following symptoms:
#    ['fever', 'cough', 'anosmia']
    def has_covid(self):
        #create initial probaility
        covidProbability = 0.05;

        #each count add each symptom possibility by 0.1
        feverCount = 0.1;
        coughCount = 0.1;
        anosmiaCount = 0.1;

        covid_Index = -1
        for t in self._test:
            if t == "covid":
                covid_Index = self._test.index("covid")
                if self._result[covid_Index]:
                    covidProbability = .99
                else:
                    covidProbability = 0.01

        #check not-tested patient possibility
        #for each symptom, add possibility by 0.1
        #and only count once
        if covid_Index == -1:
            for s in self._symptoms:
                if s == "fever":
                    covidProbability += feverCount
                    feverCount = 0
                elif s == "cough":
                    covidProbability += coughCount
                    coughCount = 0
                elif s== "anosmia":
                    covidProbability += anosmiaCount
                    anosmiaCount = 0
        return covidProbability


p1 = Patient("saly",['fever', 'cough', 'anosmia','fever', 'cough', 'anosmia'])
print("covid probability:", p1.has_covid())
p1.add_test("x_ray",True)
print("covid probability:", p1.has_covid())
p1.add_test("covid",False)
print("covid probability:", p1.has_covid())

######################

# 2. In this exercise you will make an English Deck class made of Card classes
# 
# the Card class should represent each of the cards
#
# the Deck class should represent the collection of cards and actions on them

# 2.1) Create a Card class called "Card".
# The constructor (__init__ ) should have two parameters the "suit" and the "value" and the suit of the card.
# The class should store both as attributes.


# 2.2) Create a Deck class called "Deck".
# The constructor will create an English Deck (suits: Hearts, Diamonds, Clubs, Spades 
# and values: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K). 
# It will create a list of cards that contain each of the existing cards in an English Deck.
# Create a method called "shuffle" that shuffles the cards randomly. 
# Create a method called "draw" that will draw a single card and print the suit and value. When a card is drawn, the card should be removed from the deck.


import random

#seed will create each compile, random choose in exact same sequences
#even after recompile
#random.seed(42)

class Card:
    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    def accessSuit(self):
        suit = str(self._suit)
        return suit
    def accessValue(self):
        value = str(self._value)
        return value
        
class EnglishDeck():

    def __init__(self):
        #cards: 4 suits* 13 values
        self._cards = []
        #create card and append by 13 times loops.
        #each append 4 suits
        for i in range(1,14):
            #after we append Card, A,J,Q,K, we append card by numeric value
            if i == 1:
                self._appendCards("A")
            elif i == 11:
                self._appendCards("J")
            elif i == 12:
                self._appendCards("Q")
            elif i == 13:
                self._appendCards("K")
            else:
                #in Card class, we can access card Value by public function
                #and it only return string of value
                self._appendCards(i)

        ######TEST####################
        for c in self._cards:
            print("Creation: suits:",c.accessSuit(),"value:",c.accessValue())

    #append four suits type of cards by input Value
    def _appendCards(self, suitValue):
        HeartsCard = Card("Hearts",suitValue)
        DiamondsCard = Card("Diamonds",suitValue)
        ClubsCard = Card("Clubs",suitValue)
        SpadesCard = Card("Spades",suitValue)

        self._cards.append(HeartsCard)
        self._cards.append(DiamondsCard)
        self._cards.append(ClubsCard)
        self._cards.append(SpadesCard)

    def shuffle(self):
        random.shuffle(self._cards)
        
        ######TEST####################
        print("After shuffle")
        for c in self._cards:
            print("Creation: suits:",c.accessSuit(),"value:",c.accessValue())

    def draw(self):
        if self._cards.__len__() != 0:
            print("Draw Current Card,Suits: ", self._cards[0].accessSuit(), " Value: ", self._cards[0].accessValue())
            self._cards.pop(0)
        else:
            print("No Card to Draw.")
        ######TEST####################
        print("After draw")
        for c in self._cards:
            print("Creation: suits:",c.accessSuit(),"value:",c.accessValue())


#test
deck = EnglishDeck()
deck.shuffle()
deck.draw()




###################

# 3. In this exercise you will create an interface that will serve as template 
# for different figures to compute their perimeter and surface. 

# 3.1Create an abstract class (interface) called "PlaneFigure" with two abstract methods:
# compute_perimeter() that will implement the formula to compute the perimiter of the plane figure.
# compute_surface() that will implement the formula to compute the surface of the plane figure.

# 3.2 Create a child class called "Triangle" that inherits from "PlaneFigure" and has as parameters in the constructor "base", "c1", "c2", "h". ("base" being the base, "c1" and "c2" the other two sides of the triangle and "h" the height). Implement the abstract methods with the formula of the triangle.

# 3.3 Create a child class called "Rectangle" that inherits from "PlaneFigure" and has as parameters in the constructor "a", "b" (sides of the rectangle). Implement the abstract methods with the formula of the rectangle.

# 3.3 Create a child class called "Circle" that inherits from "PlaneFigure" and has as parameters in the constructor "radius" (radius of the circle). Implement the abstract methods with the formula of the circle.

from math import pi
from abc import ABCMeta, abstractmethod
#abstract class
class PlaneFigure(metaClass = ABCMeta):
    def __init__(self) -> None:
        pass
    
    #compute total length
    @abstractmethod
    def compute_perimeter():
        return NotImplementedError

    def compute_surface():
        return NotImplementedError
    
class Triangle(PlaneFigure):
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)

    def compute_perimeter(self):
        return (self.a+self.b)*2
    
    def compute_surface(self):
        return self.a*self.b


class Rectangle(PlaneFigure):
    def __init__(self,base,c1,c2,h):
        self.base = int(base)
        self.c1 = int(c1)
        self.c2 = int(c2)
        self.h = h

    def compute_perimeter(self):
        return self.base + self.c1 + self.c2
    
    def compute_surface(self):
        return self.base*self.h/2
    


class Circle(PlaneFigure):
    def __init__(self,radius):
        self.radius = int(radius)

    def compute_perimeter(self):
        return 2*pi*self.radius
    
    def compute_surface(self):
        return pi*self.radius^2

