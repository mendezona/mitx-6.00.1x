#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 15:43:52 2020

@author: josephmendezona
"""

# Checks unpaid balance of a credit card after 12 months if only minimum payment is met
balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

count = 0
minimumPayment = balance * monthlyPaymentRate
unpaidBalance = balance - minimumPayment
interest = annualInterestRate/12 * unpaidBalance
    
while count < 12:
    balance = balance - minimumPayment + interest
    minimumPayment = balance * monthlyPaymentRate
    unpaidBalance = balance - minimumPayment
    interest = annualInterestRate/12 * unpaidBalance
    count += 1
    
print('Remaining balance: ', round(balance,2))