# Module 4
#   Programming Assignment 5
#       Prob-1.py

# Esther Pisano

# IPO
# Inputs: user enters a number from 1 to 10
# Processes: the function finds the assigned roman numeral for that number
# Output: function returns a string saying what that inputed number translates to.
# function can also tell user if input is out of valid range


def main(number):
    '''
    number = int(input(
        "Enter a number between 1 and 10 to find the Roman numeral of that number. :"))
    '''
    if number == 1:
        return buildResponse(number, "I")
    elif number == 2:
        return buildResponse(number, "II")
    elif number == 3:
        return buildResponse(number, "III")
    elif number == 4:
        return buildResponse(number, "IV")
    elif number == 5:
        return buildResponse(number, "V")
    elif number == 6:
        return buildResponse(number, "VI")
    elif number == 7:
        return buildResponse(number, "VII")
    elif number == 8:
        return buildResponse(number, "VIII")
    elif number == 9:
        return buildResponse(number, "IX")
    elif number == 10:
        return buildResponse(number, "X")
    else:
        return 'Error: input value outside valid range'


def buildResponse(number, roman):
    return "Input number " + str(number) + " translates to " + roman + " in Roman Numerals."


def unitTest():
    print("number: 1\tmain:", main(1))
    print("number: 2\tmain:", main(2))
    print("number: 2\tmain:", main(3))
    print("number: 2\tmain:", main(4))
    print("number: 2\tmain:", main(5))
    print("number: 2\tmain:", main(6))
    print("number: 2\tmain:", main(7))
    print("number: 2\tmain:", main(8))
    print("number: 2\tmain:", main(9))
    print("number: 2\tmain:", main(10))
    print("number: 2\tmain:", main(11))
    print("number: 2\tmain:", main(-4))


unitTest()
main()
