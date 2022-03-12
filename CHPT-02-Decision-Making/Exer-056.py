"""
Exercise 56: Frequency to Name

Electromagnetic radiation can be classified into one of 7 categories according to its
frequency, as shown in the table below:

-------------------------------------------------------------------------
Name                         Frequency Range (Hz)
-------------------------------------------------------------------------

Radio Waves                 Less than 3 * 10 ** 9
Microwaves                  3 * 10 ** 9 to less than 3 * 10 ** 12
Infrared Light              3 * 10 ** 12 to less than 4.3 * 10 ** 14
Visible Light               4.3 * 10 ** 14 to less than 7.5 * 10 ** 14
Ultraviolet Light           7.5 * 10 ** 14 to less than 3 * 10 ** 17
X-Rays                      3 * 10 ** 17 less than 3 * 10 ** 19
Gamma Rays                  3 * 10 ** 19 or more

-------------------------------------------------------------------------

Write a program that reads the frequency of some radiation from the user and
displays name of the radiation as part of an appropriate message.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

frequency = float(input('enter frequency of radiation: '))

if frequency >= 3 * 10**19:
    name = 'gamma rays'
elif frequency >= 3 * 10**17:
    name = 'X-rays'
elif frequency >= 7.5 * 10**14:
    name = 'Ultraviolet light'
elif frequency >= 4.3 * 10**14:
    name = 'Visible light'
elif frequency >= 3 * 10**12:
    name = 'Infrared light'
elif frequency >= 3 * 10**9:
    name = 'microwaves'
else:
    name = 'radio waves'

print('that frequency corresponds to %s' % name)






