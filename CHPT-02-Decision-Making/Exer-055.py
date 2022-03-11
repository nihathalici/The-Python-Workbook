"""
Exercise 55: Wavelengths of Visible Light

The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the
spectrum is continuous, it is often divided into 6 colors as shown below:

--------------------------------
Color     Wavelength (nm)
--------------------------------

Violet    380 to less than 450
Blue      450 to less than 495
Green     495 to less than 570
Yellow    570 to less than 590
Orange    590 to less than 620
Red       620 to 750
--------------------------------

Write a program that reads a wavelength from the user and reports its color. Display
an appropriate error message if the wavelength entered by the user is outside of the
visible spectrum.
"""

# Solution by Micheal O'Dwyer
# https://github.com/michealodwyer26

wavelength = int(input("Enter a value for a wavelength of visible light in nanometers: "))
colour = ""

if wavelength >= 350 and wavelength < 450:
    colour = "violet"
elif wavelength >= 450 and wavelength < 495:
    colour = "blue"
elif wavelength >= 495 and wavelength < 570:
    colour = "green"
elif wavelength >= 570 and wavelength < 590:
    colour = "yellow"
elif wavelength >= 590 and wavelength < 620:
    colour = "orange"
elif wavelength >= 620 and wavelength <= 750:
    colour = "red"

if colour != "":
    print("This wavelength is the colour {}.".format(colour))
else:
    print("This wavelength is outside the spectrum of visible light.")





