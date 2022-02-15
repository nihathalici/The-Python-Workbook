
"""
Exercise 34: Day Old Bread

A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
percent. Write a program that begins by reading the number of loaves of day old
bread being purchased from the user. Then your program should display the regular
price for the bread, the discount because it is a day old, and the total price. Each of
these amounts should be displayed on its own line with an appropriate label. All of
the values should be displayed using two decimal places, and the decimal points in
all of the numbers should be aligned when reasonable values are entered by the user.
"""

BREAD_PRICE = 3.49
DISCOUNT_RATE = 0.60

num_loaves = int(input("Enter the number of day old loaves: "))

regular_price = num_loaves * BREAD_PRICE
discount = regular_price * DISCOUNT_RATE
total = regular_price - discount

print("Regular price: %5.2f" % regular_price)
print("Discount:      %5.2f" % discount)
print("Total:         %5.2f" % total)


"""
# Solution by Aldo Telese
# https://github.com/aldotele

unit_of_old_bread = int(input('enter number of bought pieces: '))
unit_price = 3.49
discount_rate = 0.60

regular_price = unit_of_old_bread * unit_price
tot_discount = regular_price * discount_rate
final_price = regular_price - tot_discount

print("regular price: %5.2f" % regular_price)
print("discount:      %5.2f" % tot_discount)
print("final price:   %5.2f" % final_price)

'''
NOTA: 
%5.2f makes sure the value will take up exactly 5 spaces, 2 of which for decimals, 1 for the dot and 2 
for the integers. This is useful to keep a column in line when the number of digits that are present in prices
and discounts is variable.
'''
"""
