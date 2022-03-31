from collections import Counter
from collections import defaultdict

def map_step_on_chain(chain, chain_map):
    new_chain = ""

    index = 0
    while index < len(chain)-1:
        key = chain[index:index+2]
        new_chain += chain[index]
        if key in chain_map.keys():
            new_chain += chain_map[key]
        pass
        index+=1
    new_chain += chain[index]
    return new_chain

def map_step_on_chain_2(pair_count, letter_count, chain_map):

    new_pair_count = defaultdict(lambda:0)
    index = 0
    for key in list(pair_count.keys()):
        amount = pair_count[key]
        if key in chain_map.keys():
            new_letter = chain_map[key]
            new_pair_count[key[0] + new_letter] += amount
            new_pair_count[new_letter + key[1]] += amount
            letter_count[new_letter] += amount

    return new_pair_count


starting_chain = ""
read_switch = False
chain_map = {}
pair_count = defaultdict(lambda:0)
letter_count = Counter()
# Read numbers
with open('day_14_puzzle_input.txt') as f:

    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if not line:
            read_switch = True
        elif not read_switch:
            starting_chain = line
        elif read_switch:
            info = line.split("->")
            chain_map[info[0].strip()] = info[1].strip()

for count in Counter(starting_chain).most_common():
    letter_count[count[0]] = count[1]

index = 0
while index < len(starting_chain) -1:
    pair = starting_chain[index:index+2]
    if pair in pair_count.keys():
        pair_count[pair] += 1
    else:
         pair_count[pair] = 1
    index += 1

for i in range(40):
     pair_count = map_step_on_chain_2(pair_count, letter_count, chain_map)

print("Question")
print(pair_count)
print(letter_count)

 #letter_count = Counter(letter_count)

most_common = letter_count.most_common(1)[0]
least_common = letter_count.most_common()[-1]

print(most_common)
print(least_common)
print(most_common[1] - least_common[1])


