#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 15:43:52 2020

@author: josephmendezona
"""

# Finding the minimum constant to pay off debt in a year for a credit card assuming no minimum monthly payments using recursion
def getBalance(balance, annualInterestRate, timePeriod):
    
    if timePeriod == 0:
        return balance
    
    else:
        unpaidBalance = balance - testPayment
        interest = annualInterestRate/12 * unpaidBalance
        return getBalance(balance - testPayment + interest, annualInterestRate, timePeriod-1)

balance = 320000
annualInterestRate = 0.2

testPayment = 10
timePeriod = 12

while getBalance(balance, annualInterestRate, timePeriod) > 0:
    testPayment += 10
    print(testPayment, round(getBalance(balance, annualInterestRate, timePeriod), 2))

print('Lowest Payment: ', round(testPayment, 2))