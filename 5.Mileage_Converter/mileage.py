#! /usr/bin/env python3

kms = input("How many kilometers of cycling you did? ")
miles = float(kms)/1.60934
miles = round(miles, 2)
print(f"Your {kms} kms cycling  ride is equivalent to {miles} miles")
