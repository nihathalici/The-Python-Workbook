"""
Exercise 57: Cell Phone Bill

A particular cell phone plan includes 50 minutes of air time and 50 text messages
for $15.00 a month. Each additional minute of air time costs $0.25, while additional
text messages cost $0.15 each. All cell phone bills include an additional charge of
$0.44 to support 911 call centers, and the entire bill (including the 911 charge) is
subject to 5 percent sales tax.

Write a program that reads the number of minutes and text messages used in a
month from the user. Display the base charge, additional minutes charge (if any),
additional text message charge (if any), the 911 fee, tax and total bill amount. Only
display the additional minute and text message charges if the user incurred costs in
these categories. Ensure that all of the charges are displayed using 2 decimal places.
"""

minutes = int(input("Enter the number of minutes: "))
text_messages = int(input("Enter the number of text messages: "))

base_charge = 15.00
additional_text_messages_charge = (text_messages - 50) * 0.15
additional_minutes_charge = (minutes - 50) * 0.25
call_centre_charge = 0.44

subtotal = base_charge + additional_text_messages_charge + additional_minutes_charge + call_centre_charge

tax = subtotal / 100 * 5
total = subtotal + tax

print()
print("Base charge = ${}".format(round(base_charge, 2)))

if additional_minutes_charge > 0:
    print("Additional minutes charge = ${}".format(round(additional_minutes_charge, 2)))
elif additional_text_messages_charge > 0:
    print("Additional text messages charge = ${}".format(round(additional_text_messages_charge, 2)))

print("Call centre charge = ${}".format(round(call_centre_charge, 2)))
print("Tax = ${}".format(round(tax, 2)))
print()
print("Grand Total = ${}".format(round(total, 2)))
    



