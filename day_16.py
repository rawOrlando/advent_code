from binascii import hexlify
import math

def hex_to_bin(s):
    return format(int(s.strip(), 16), f"0{len(s.strip()) * 4}b")

# leading 0's until the length is a multiple of 4
def leading_zeros(a):
    return "0" * ((4 - len(a) % 4) % 4) + a

def parse_header(s):
    # to do whats up with to_decimal
    #       Version_Number  Packet_Type
    return (int(s[:3], 2), int(s[3:6], 2))

def parse_literal(packet):
    # 10110000111
    # literal value
    remaining = packet[6:]
    parsed_literal = ""

    while True:
        break_bit = remaining[0]
        parsed_literal += remaining[1:5]
        remaining = remaining[5:]

        if break_bit == "0":
            break

    return int(parsed_literal, 2), remaining


def parse_operator(packet):
    length_type_id = packet[6]
    length_of_bits = 0

    numbers = []

    remaining_packet = packet[7:]

    if length_type_id == "0":
        length_of_bits = int(remaining_packet[:15],2)
        remaining_packet = remaining_packet[15:]
        length_moved=0
        while remaining_packet and length_moved < length_of_bits:
            result, remaining = parse_packet(remaining_packet)
            # TODO this feels bad
            length_moved += (len(remaining_packet) - len(remaining))
            remaining_packet = remaining
            numbers.append(result)
    elif length_type_id == "1":
        number_of_sub_packets = int(remaining_packet[:11],2)
        remaining_packet = remaining_packet[11:]

        for _ in range(number_of_sub_packets):
            result, remaining = parse_packet(remaining_packet)
            remaining_packet = remaining
            numbers.append(result)


    return numbers, remaining_packet
def parse_packet(packet):

    packet_version, type_id = parse_header(packet)

    global version_counter
    version_counter += packet_version

    if type_id == 4:
        return parse_literal(packet)
    else:
        #print("Passing in:",packet)
        numbers, remaining = parse_operator(packet)

    print(numbers)
    if type_id in OPERATORS.keys():
        return OPERATORS[type_id](numbers), remaining

    return None, None

OPERATORS = {
    0: sum,
    1: math.prod,
    2: min,
    3: max,
    5: lambda x: int(x[0] > x[1]),
    6: lambda x: int(x[0] < x[1]),
    7: lambda x: int(x[0] == x[1]),
}

with open('day_16_puzzle_input.txt') as f:
    data = f.read()

data_bin = hex_to_bin(data)
version_counter = 0

print("evaluated expression:", parse_packet(data_bin)[0])
#print(version_counter)