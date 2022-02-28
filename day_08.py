import math


def map_number_codes(options):
	code_values = {}
	value_codes_sets = {}

	for number_code in list(options):
		if len(code_values) >= 4:
			break

		length = len(number_code)

		# non unique values
		if length < 7 and length > 4:
			continue
		# look for one
		elif length == 2:
			code_values[frozenset(number_code)] = 1
			value_codes_sets[1] =  set(number_code)
			options.remove(number_code)
		# look for seven
		elif length == 3:
			code_values[frozenset(number_code)] = 7
			value_codes_sets[7] =  set(number_code)
			options.remove(number_code)
		# look for four
		elif length == 4:
			code_values[frozenset(number_code)] = 4
			value_codes_sets[4] =  set(number_code)
			options.remove(number_code)
		# look for eight
		elif length == 7:
			code_values[frozenset(number_code)] = 8
			value_codes_sets[8] =  set(number_code)
			options.remove(number_code)

	# figure out A value
	a_value = value_codes_sets[7].difference(value_codes_sets[1]).pop()

	nines_values = list(value_codes_sets[4])
	nines_values.append(a_value)

	for number_code in options:
		if len(number_code) == 6 and all(x in number_code for x in nines_values):
			code_values[frozenset(number_code)] = 9
			value_codes_sets[9] =  set(number_code)
			options.remove(number_code)
			break

	e_value = value_codes_sets[8].difference(value_codes_sets[9]).pop()

	for number_code in options:
		if len(number_code) == 5 and e_value in number_code:
			code_values[frozenset(number_code)] = 2
			value_codes_sets[2] =  set(number_code)
			options.remove(number_code)
			break

	c_value = value_codes_sets[1].difference(value_codes_sets[4].difference(value_codes_sets[2])).pop()

	for number_code in list(options):
		if len(number_code) == 6:
			if c_value in number_code:
				code_values[frozenset(number_code)] = 0
				value_codes_sets[0] =  set(number_code)
				options.remove(number_code)
			elif not c_value in number_code:
				code_values[frozenset(number_code)] = 6
				value_codes_sets[6] =  set(number_code)
				options.remove(number_code)


	for number_code in options:
		diff_len = len(value_codes_sets[6].difference(set(number_code)))
		if diff_len == 2:
			code_values[frozenset(number_code)] = 3
		elif diff_len == 1:
			code_values[frozenset(number_code)] = 5

	print(code_values)

	return code_values


number_count = [0,0,0,0,0,0,0,0,0,0]
total = 0
with open('day_08_puzzle_input.txt') as f:

    lines = f.readlines()
    for line in lines:
    	# what is the difference between these two?
    	temp = line.split("|")
    	front_part = temp[0]
    	back_part = temp[1]
    	codes = map_number_codes(front_part.split())

    	# decode
    	digit_place = 3
    	big_number = 0
    	for number_code in back_part.split():
    		big_number += codes[frozenset(number_code)] * math.pow(10, digit_place)
    		number_count[codes[frozenset(number_code)]] += 1
    		digit_place -= 1

    	total += big_number

print(number_count)
print(total)


