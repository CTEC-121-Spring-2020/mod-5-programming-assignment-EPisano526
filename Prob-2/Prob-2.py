# Module 4
#   Programming Assignment 5
#       Prob-2.py

# Esther Pisano

# IPO
# input: user inputs cost of item, amount tendered.
# process: computer processes change
# given back which is then specified in different bills and coins.
# Outputs: gives amout of change given back to customer in
# ten dollar bills, five dollar bills, one dollar bills, quarters, dimes,
# nickles, and pennies.
# input amount of cost and change back


def main():
    cost = float(input("Enter the cost of the item you are buying: $"))
    tendered = float(
        input("Enter the amount you are giving to pay for this item: $"))
    change = tendered - cost
    total_change = round(change, 2)
    print("Cost: ", cost, "Tendered: ", tendered, "Change: ", total_change)

    # converts change to an int
    print("rounded change:", round(change * 100))
    changeDue = int(round(change * 100))
    print("change due:", changeDue)

    # calculate number of tens
    tens = changeDue // 1000
    if tens >= 1:
        print("tens:", tens)

    # adjust changeDue to reflect change given
    changeDue = changeDue - (tens * 1000)

    # calculate number of fives
    fives = changeDue // 500
    if fives >= 1:
        print("fives:", fives)
    # adjust changeDue
    changeDue = changeDue - (fives * 500)

    # ones
    ones = changeDue // 100
    if ones >= 1:
        print("ones:", ones)
    changeDue = changeDue - (ones * 100)

    # quarters
    quarters = changeDue // 25
    if quarters >= 1:
        print("quarters:", quarters)
    changeDue = changeDue - (quarters * 25)

    # dimes
    dimes = changeDue // 10
    if dimes >= 1:
        print("dimes:", dimes)
    changeDue = changeDue - (dimes * 10)

    # nickels
    nickels = changeDue // 5
    if nickels >= 5:
        print("nickels:", nickels)
    changeDue = changeDue - (nickels * 5)

    # pennies
    pennies = changeDue // 1
    if pennies >= 1:
        print("pennies:", pennies)
    changeDue = changeDue - (pennies * 1)


main()
