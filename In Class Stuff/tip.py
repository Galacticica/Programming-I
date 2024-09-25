'''
File: tip.py
Author: Reagan Zierke
Date: 9/25/24
Description:
A Program that calculates the total price based on user input of meal cost and tip percentage'''

#Takes user input for the cost of the meal and the tip percentage
#Converts tip percentage into a decimal to multiply by
cost = float(input("What is the cost of the meal? "))
tip_percent = 0.1*float(input("What percent would you like to tip? "))

new_cost = cost * 1+tip_percent
print(f"\nThe total cost is{new_cost: .2f}")
