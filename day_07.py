# Python program to get average of a list
def Average(lst):
    return sum(lst) / len(lst)

def calculate_fuel_cost(dest_spot, crab_spots):
    fuel = 0
    # look into making this a reduce
    for spot in crab_spots:
        difference = abs(spot-dest_spot)
        fuel += int(difference*(difference+1)/2)

    return fuel

crab_spots = []
with open('day_07_puzzle_input.txt') as f:
    lines = f.readlines()
    # Read Bingo  numbers
    crab_spots = [int(number) for number in lines[0].split(",")]

average = Average(crab_spots)
from statistics import mode
import math
mode = mode(crab_spots)   # Returns all unique items and their counts

print(average)
print(mode)

distance_fuel_dictionary = {}

lower_start = min(math.floor(average), mode)
end = max(math.ceil(average), mode)
index = lower_start
lowest_fuel = float('inf')
best_spot = index
print(index)
print(end)
while index <= end:
    fuel = calculate_fuel_cost(index, crab_spots)
    distance_fuel_dictionary[index] = fuel
    if fuel <= lowest_fuel:
        lowest_fuel = fuel
        best_spot = index
    index += 1

print(best_spot)
print(lowest_fuel)