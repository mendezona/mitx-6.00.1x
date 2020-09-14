#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 17:12:48 2020

@author: josephmendezona
"""

# Checks unpaid balance of a credit card after 12 months if only minimum payment is met using recursion

def getBalance(balance, annualInterestRate, monthlyPaymentRate, timePeriod):
    
    if timePeriod == 0:
        return balance
    
    else:
        minimumPayment = balance * monthlyPaymentRate
        unpaidBalance = balance - minimumPayment
        interest = annualInterestRate/12 * unpaidBalance
        return getBalance(balance - minimumPayment + interest, annualInterestRate, monthlyPaymentRate, timePeriod-1)

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
timePeriod = 12

print('Remaining balance: ', round(getBalance(balance, annualInterestRate, monthlyPaymentRate, timePeriod), 2))