from math import ceil


with open("day16.txt", "r") as f:
    txt = bin(int(f.read().strip(), 16))[2:]
    txt = txt.zfill(ceil(len(txt)/8) * 8)
version_numbers = set()

def packet(bits, sub):
    print(bits)
    version = int(bits[:3], 2)
    type_id = int(bits[3:6], 2)
    bits = bits[6:]
    size = 6

    if type_id == 4:
        value = ""
        while(bits[0] == "1"):
            value += bits[1:5] 
            size += 5
            bits = bits[5:]
        value += bits[1:5]
        size += 5
        bits = bits[5 + 8 - size%8:] if not sub else bits[5:]
        value = int(value, 2)
        print(value)
        if sub: return version, bits
        else: version_numbers.add(version)
    elif bits[0] == "0":
        print("1-")
        size += 16
        sub_length = int(bits[1:16], 2)
        bits = bits[16:]
        rest = bits[:sub_length]
        while rest:
            ver, rest =  packet(rest, True)
            version += ver
        bits = bits[sub_length:]
        if sub: return version, bits
        else: version_numbers.add(version)
    else:
        print("2-")
        size += 12
        sub_packets = int(bits[1:12], 2)
        bits = bits[12:]
        for i in range(int(sub_packets)):
            ver, bits = packet(bits, True)
            version += ver
        if sub: return version, bits
        else: version_numbers.add(version)


packet(txt, False)
print(version_numbers)