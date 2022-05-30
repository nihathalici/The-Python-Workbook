"""
Exercise 128: Count the Elements

Python’s standard library includes a method named count that determines how
many times a specific value occurs in a list. In this exercise, you will create a new
function named countRange. It will determine and return the number of elements
within a list that are greater than or equal to some minimum value and less than some
maximum value. Your function will take three parameters: the list, the minimum
value and the maximum value. It will return an integer result greater than or equal to
0. Include a main program that demonstrates your function for several different lists,
minimum values and maximum values. Ensure that your program works correctly
for both lists of integers and lists of floating-point numbers.
"""
#
# Author's solution:
##
# Count the number of elements in a list that are greater than or equal to some minimum
# value and less than some maximum value.
#
## Determine how many elements in data are greater than or equal to mn and less than mx
# @param data the list of values to examine
# @param mn the minimum acceptable value
# @param mx the exclusive upper bound on acceptability
# @return the number of elements, e, such that mn <= e < mx
def countRange(data, mn, mx):
    # Count the number of elements within the acceptable range
    count = 0
    for e in data:
        # Check each element
        if mn <= e and e < mx:
            count = count + 1

    # Return the result
    return count

# Demonstrate the countRange function
def main():
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Test a case where some elements are within the range
    print("Counting the elements in [1..10] between 5 and 7...")
    print("Result: %d Expected: 2" % countRange(data, 5, 7))

    # Test a case where all elements are within the range
    print("Counting the elements in [1..10] between -5 and 77...")
    print("Result: %d Expected: 10" % countRange(data, -5, 77))

    # Test a case where no elements are within the range
    print("Counting the elements in [1..10] between 12 and 17...")
    print("Result: %d Expected: 0" % countRange(data, 12, 17))

    # Test a case where the list is empty
    print("Counting the elements in [] between 0 and 100...")
    print("Result: %d Expected: 0" % countRange([], 0, 100))

    # Test a case with duplicate values
    data = [1, 2, 3, 4, 1, 2, 3, 4]
    print("Counting the elements in", data, "between 2 and 4...")
    print("Result: %d Expected: 4" % countRange(data, 2, 4))

main()
    
    
    
    
    
