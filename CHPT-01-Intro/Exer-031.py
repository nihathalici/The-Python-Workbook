
"""
Exercise 31: Units of Pressure

In this exercise you will create a program that reads a pressure from the user in kilo-
pascals. Once the pressure has been read your program should report the equivalent
pressure in pounds per square inch, millimeters of mercury and atmospheres. Use
your research skills to determine the conversion factors between these units.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

pressure_KPa = float(input('enter pressure in kilopascals: '))

KPa_to_psi = 0.145038
KPa_to_Torr = 7.50062
KPa_to_atm = 0.00986923

pressure_psi = pressure_KPa * KPa_to_psi
pressure_Torr = pressure_KPa * KPa_to_Torr
pressure_atm = pressure_KPa * KPa_to_atm

print('a pressure of %.4f kilopascals equals a pressure of %.4f pounds per square inch, %.4f millimeters\
 of mercury and %.4f atmospheres' % (pressure_KPa, pressure_psi, pressure_Torr, pressure_atm))



"""

# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

kiloPascals = float(input("Please enter a pressure in kilo-pascals: "))

PSI = kiloPascals * 0.145037738
mmOfMercury = kiloPascals * 7.50062
atmospheres = kiloPascals / 101.3

print()
print("In Pounds Per Square Inch (PSI): {}".format(PSI))
print("In Millimetres Of Mercury (mmHg): {}".format(mmOfMercury))
print("In Atmospheres (atm): {}".format(atmospheres))
"""
