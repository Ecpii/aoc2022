from functools import cmp_to_key

from first import parse_list

with open("input.txt") as inp:
    packets = inp.readlines()


def packet_less(l, r):
    if l == r:
        return 0
    if not l:
        return -1
    if not r:
        return 1
    if type(l[0]) is list and type(r[0]) is list:
        res = packet_less(l[0], r[0])
    elif type(l[0]) is list and type(r[0]) is not list:
        res = packet_less(l[0], [r[0]])
    elif type(l[0]) is not list and type(r[0]) is list:
        res = packet_less([l[0]], r[0])
    else:
        if l[0] < r[0]:
            return -1
        if l[0] > r[0]:
            return 1
        return 0
    if res != 0:
        return res
    return packet_less(l[1:], r[1:])


sorted_packets = [[[2]], [[6]]]
for packet in packets:
    if packet != "\n":
        sorted_packets.append(parse_list(packet[:-1]))

sorted_packets.sort(key=cmp_to_key(packet_less))
print((sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1))
