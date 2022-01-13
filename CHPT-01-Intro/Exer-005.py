"""
Exercise 5: Bottle Deposits

In many jurisdictions a small deposit is added to drink containers to encourage people
to recycle them. In one particular jurisdiction, drink containers holding one liter or
less have a $0.10 deposit, and drink containers holding more than one liter have a
$0.25 deposit.
Write a program that reads the number of containers of each size from the user.
Your program should continue by computing and displaying the refund that will be
received for returning those containers. Format the output so that it includes a dollar
sign and two digits to the right of the decimal point.
"""

ten_depo_bot = int(input("Enter the number of one lt. bottles: "))
twentyfive_depo_bot = int(input("Enter the number of more then one lt. bottles: "))

total = float(ten_depo_bot * 0.10) + float(twentyfive_depo_bot * 0.25)

print( "You get ${} deposit.".format(round(total, 2)) )

"""
Author's solution:
LESS_DEPOSIT = 0.10
MORE_DEPOSIT = 0.25

less = int(input("How many containers 1 litre or less? "))
more = int(input("How many containers more than 1 litre? "))

refund = less * LESS_DEPOSIT + more * MORE_DEPOSIT

print("Your total refund will be $%.2f." % refund)
"""
