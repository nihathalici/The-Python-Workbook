"""
Exercise 9: Compound Interest

Pretend that you have just opened a new savings account that earns 4 percent interest
per year. The interest that you earn is paid at the end of the year, and is added to the
balance of the savings account. Write a program that begins by reading the amount of
money deposited into the account from the user. Then your program should compute
and display the amount in the savings account after 1, 2, and 3 years. Display each
amount so that it is rounded to 2 decimal places.
"""


INT_RATE = 0.04

amt_money = int(input("Enter the amount of money: "))
amt_money_first = (amt_money * INT_RATE) + amt_money
amt_money_second = (amt_money_first * INT_RATE) + amt_money_first
amt_money_third = (amt_money_second * INT_RATE) + amt_money_second

print("After 1 year %.2f, 2 years %.2f, 3 years %.2f." % (amt_money_first, amt_money_second, amt_money_third))


"""
# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

amount = float(input("How much money is initially deposited into the savings account: $"))

interestRate = 0.04 # Interest for this savings A/C is 4%

interest = amount * interestRate
amount += interest
print("Balance as of end of Year 1: ${0:0.2f}.".format(amount))

interest = amount * interestRate
amount += interest
print("Balance as of end Year 2: ${0:0.2f}.".format(amount))

interest = amount * interestRate
amount += interest
print("Balance as of end of Year 3: ${0:0.2f}.".format(amount))
"""
