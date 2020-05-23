# Module 4
#   Programming Assignment 5
#       Prob-3.py

# Esther Pisano

# IPO
# Inputs: cost of gallon of paint and how many square feet are to be painted
# Processes: Calculates cost of paint and labor through subtraction of square feet.
# Outputs: Gives estimate for how much total cost of paint job will be.

import math


def estimate(squareFeet, gallonPrice):

    # make function that has cost of one time set up fee
    # 112 sq/ft = 1 gallon of paint = 8 hours of labor

    # Find how much paint we will need
    totalGallons = math.ceil(squareFeet / 112)
    print("Total amount of paint gallons needed:", totalGallons)
# find total cost of paint
    totalCost_paint = totalGallons * gallonPrice
    print("Total cost of paint: $", totalCost_paint)

# find total amount of hours
    totalHours = totalGallons * 8
    print("Total amount of hours needed: ", totalHours, "hours")
# find total cost of labor
    laborCost = totalHours * 35
    print("Total cost of labor: $", laborCost)

# find total cost of all job with one time set up fee
    Total_Cost = 99 + laborCost + totalCost_paint
    print("Total estimate of job: $", Total_Cost)


def main():
    # Get cost of paint per gallon from customer
    # Find how many square feet will be painted

    gallonPrice = eval(input("Input cost of one gallon of paint: $"))
    squareFeet = eval(input("How many square feet do you need painted?: "))
    estimate(squareFeet, gallonPrice)


main()
