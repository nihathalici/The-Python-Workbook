"""
Exercise 92: Ordinal Date to Gregorian Date

Create a function that takes an ordinal date, consisting of a year and a day within in
that year, as its parameters. The function will return the day and month corresponding
to that ordinal date as its results. Ensure that your function handles leap years
correctly.

Use your function, as well as the ordinalDate function that you wrote previously,
to create a program that reads a date from the user. Then your program should
report a second date that occurs some number of days later. For example, your program
could read the date a product was purchased and then report the last date that
it can be returned (based on a return period that is a particular number of days), or
your program could compute the due date for a baby based on a gestation period of
280 days. Ensure that your program correctly handles cases where the entered date
and the computed date occur in different years.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

from greg_to_ord import is_leap, days_in_month, greg_to_ord_date

def ord_to_greg_date(day, year):
    days_count = 0
    for m in range(1, 13):
        month_days = days_in_month(m, year)
        days_count += month_days

        if days_count >= day:
            dd = month_days - (days_count - day)
            mm = m
            break
    
    res_date = '%.2d-%.2d-%.4d' % (dd, mm, year)
    return res_date

def dates_addition(starting_ordinal, starting_year, days_to_add):
    """
    the function adds a number of days to a starting date and returns the future date
    :param starting_ordinal: integer representing a starting ordinal day (1-366) or (1-365)
    :param starting_year: integer
    :param days_to_add: number of days to add to the starting ordinal
    :return: the future date in dd-mm-yyyy format
    """
    future_ordinal = starting_ordinal + days_to_add

    res_year = starting_year
    # handling case when the future date is across different years
    while True:
        if is_leap(res_year):
            tot_days = 366
        else:
            tot_days = 365
        
        if future_ordinal > tot_days:
            future_ordinal -= tot_days
            res_year += 1
        else:
            break
    
    # invoking the ordinal to gregorian conversion by passing the future ordinal day and future year
    future_date = ord_to_greg_date(future_ordinal, res_year)
    return future_date

def main():
    # computing the due date for a baby
    # considering 280 days away from current date
    gestation = 280
    print('Please write today\'s date ...')
    today_d = int(input('Enter current day: '))
    today_m = int(input('Enter current month: '))
    today_y = int(input('Enter current year: '))
    this_year_ordinal = greg_to_ord_date(today_d, today_m, today_y)

    due_date = dates_addition(this_year_ordinal, today_y, gestation)
    print('Your baby\'s due date will be {}'.format(due_date))

if __name__ == '__main__':
    main()
