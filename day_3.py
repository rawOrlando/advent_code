import math

bytes_list = list()

with open('day_3_puzzle_input.txt') as f:
    lines = f.readlines()
    for line in lines:
        bytes_list.append(line)


# Calculate gamma, ane epsilon
gamma = 0
epsilon = 0
index = 0
byte_length = len(bytes_list[0]) #note should be 8 but example given was 5
while index < byte_length:
    zero_count = 0
    one_count = 0
    for byte_str in bytes_list:
        if byte_str[index:index+1] == "0":
            zero_count += 1
        if byte_str[index:index+1] == "1":
            one_count += 1

    if one_count > zero_count:
        gamma += math.pow(2, byte_length - index - 2)
    elif one_count < zero_count:
        epsilon += math.pow(2, byte_length - index - 2)

    index += 1

print(gamma)
print(epsilon)
print(gamma * epsilon)


# Figure out oxygen rating.
possible_oxygen_rating = bytes_list
possible_C02_scrub_rating =  bytes_list
index = 0
while index < byte_length:
    zero_count = 0
    one_count = 0
    for byte_str in possible_oxygen_rating:
        if byte_str[index:index+1] == "0":
            zero_count += 1
        if byte_str[index:index+1] == "1":
            one_count += 1

    possible_oxygen_rating = (
        [x for x in possible_oxygen_rating if
            (one_count >= zero_count and x[index:index+1] == "1") or
            (one_count < zero_count and x[index:index+1] == "0")]
        )

    if len(possible_oxygen_rating) < 2:
        break

    index += 1

possible_C02_scrub_rating =  bytes_list
index = 0
while index < byte_length:
    zero_count = 0
    one_count = 0
    for byte_str in possible_C02_scrub_rating:
        if byte_str[index:index+1] == "0":
            zero_count += 1
        if byte_str[index:index+1] == "1":
            one_count += 1

    possible_C02_scrub_rating = (
        [x for x in possible_C02_scrub_rating if
            (one_count < zero_count and x[index:index+1] == "1") or
            (one_count >= zero_count and x[index:index+1] == "0")]
        )

    if len(possible_C02_scrub_rating) < 2:
        break

    index += 1
oxy_rating = int(possible_oxygen_rating.pop(), 2)
co2_rating = int(possible_C02_scrub_rating.pop(), 2)
print(oxy_rating)

print(co2_rating)
print("Life Supprrt")
print(co2_rating * oxy_rating)
print()




