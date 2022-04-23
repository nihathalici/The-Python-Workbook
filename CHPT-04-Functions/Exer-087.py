"""
Exercise 87: Shipping Calculator

An online retailer provides express shipping for many of its items at a rate of $10.95
for the first item in an order, and $2.95 for each subsequent item in the same order.
Write a function that takes the number of items in the order as its only parameter.
Return the shipping charge for the order as the function’s result. Include a main
program that reads the number of items purchased from the user and displays the
shipping charge.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

def shipping_cost(n):
    if n < 1:
        return 'Items must be at least 1'
    one_item_shipping = 10.95
    more_items_shipping = 2.95
    tot_shipping_cost = one_item_shipping + (n - 1) * more_items_shipping
    return 'Shipping will cost € %.2f' % tot_shipping_cost

def main():
    items = int(input('Enter number of purchased items: '))
    print(shipping_cost(items))

if __name__ == '__main__':
    main()

