#!/usr/bin/python3
# This module includes math functions and defines a class to handle functions.


# This function employs Newton's Method for estimation of square roots.
def squareroot(n):
    root = n/2
    for k in range(20):
        root = (1/2)*(root + (n / root))
    return root

# This function utilizes Euler's algorithm to calculate the GCD between
# two numbers.
def greatcommdiv(m,n,):
    while m % n != 0:
        oldm = m
        oldn = n
        m = oldn 
        n = oldm % oldn
    return n
        
class Fraction:
    
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom
    
    def __str__(self):
        return str(self.num)+"/"+str(self.den)

#    def show(self):
#        print(self.num,"/",self.den)
    
    def __add__(self,otherFraction):
        newnum = self.num * otherFraction.den + self.den * otherFraction.num
        newden = self.den * otherFraction.den
        common = greatcommdiv(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = self.den * other.num
        return firstnum == secondnum
