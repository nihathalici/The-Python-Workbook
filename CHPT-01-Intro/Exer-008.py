"""
Exercise 8: Widgets and Gizmos

An online retailer sells two products: widgets and gizmos. Each widget weighs 75
grams. Each gizmo weighs 112 grams. Write a program that reads the number of
widgets and the number of gizmos from the user. Then your program should compute
and display the total weight of the parts.
"""
WID_WT = 75
GIZ_WT = 112

amt_wid = int(input("How many widget? "))
amt_giz = int(input("How many gizmo? "))

t_wid = amt_wid * WID_WT
t_giz = amt_giz * GIZ_WT

print("The widgets weight {} gr., the gizmos weight {} gr. Total weight is {} gr.".format(t_wid, t_giz, (t_wid + t_giz)))


"""
# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

noOfWigets = int(input("Please enter the amount of widgets: "))
noOfGizmos = int(input("Please enter the amount of gizmos: "))

widgetWeight = 75
gizmoWeight = 112

totalWeight = (noOfWigets * widgetWeight) + (noOfGizmos * gizmoWeight)

print("The total weight of all these widgets and gizmos is {} grams.".format(totalWeight))

"""
