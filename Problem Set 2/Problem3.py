#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 15:43:52 2020

@author: josephmendezona

Finding the minimum constant to pay off debt in a year for a credit card assuming no minimum monthly payments using recursion and bisection search

"""

def getBalance(balance, annualInterestRate, timePeriod, testPayment):
    if timePeriod == 0:
        return balance
    
    else:
        unpaidBalance = balance - testPayment
        interest = annualInterestRate/12 * unpaidBalance
        return getBalance(balance - testPayment + interest, annualInterestRate, timePeriod-1, testPayment)
    

def newTestPayment(testPayment, monthlyLowerBound, monthlyUpperBound):
  
    if getBalance(balance, annualInterestRate, timePeriod, testPayment) < 0:
        if getBalance(balance, annualInterestRate, timePeriod, testPayment-0.01) > 0:
            return testPayment
        else:
            return newTestPayment((monthlyLowerBound + testPayment)/2, monthlyLowerBound, testPayment)
    
    if getBalance(balance, annualInterestRate, timePeriod, testPayment) > 0:
        if getBalance(balance, annualInterestRate, timePeriod, testPayment+0.01) < 0:
            return testPayment  
        else:
            return newTestPayment((testPayment + monthlyUpperBound)/2, testPayment, monthlyUpperBound)

#variables provided
balance = 320000
annualInterestRate = 0.2

#variables created
monthlyLowerBound = balance/12
monthlyUpperBound = (balance * ((1 + (annualInterestRate/12))**12))/12
timePeriod = 12
testPayment = (monthlyLowerBound + monthlyUpperBound)/2

print('Lowest Payment: ', round(newTestPayment(testPayment, monthlyLowerBound, monthlyUpperBound), 2))