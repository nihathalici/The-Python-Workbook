"""
Exercise 86: Taxi Fare

In a particular jurisdiction, taxi fares consist of a base fare of $4.00, plus $0.25
for every 140 meters travelled. Write a function that takes the distance travelled (in
kilometers) as its only parameter and returns the total fare as its only result. Write a
main program that demonstrates the function.

Hint: Taxi fares change over time. Use constants to represent the base fare and
the variable portion of the fare so that the program can be updated easily when
the rates increase.
"""

# Solution by Aldo Telese
# https://github.com/aldotele

def compute_taxi_fare(distance_km):
    base_fare = 4
    variable_fare = 0.25  # 0.25 every 140 mt
    distance_m = distance_km * 1000
    variable_cost = variable_fare * (distance_m // 140)
    tot_cost = base_fare + variable_cost
    return '%.2f €' % tot_cost

def main():
    distance_km = float(input("Enter distance in km: "))
    print(compute_taxi_fare(distance_km))

if __name__ == '__main__':
    main()
