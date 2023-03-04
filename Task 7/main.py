def main(hex_str):
    bin_str = bin(int(hex_str, 16))[2:]
    bin_str = bin_str.zfill(len(bin_str) + (4 - len(bin_str) % 4) % 4)
    a = hex(int(bin_str[-3:], 2))
    b = hex(int(bin_str[-7:-3], 2))
    c = hex(int(bin_str[:-7], 2))
    return (a, b, c)


print(main('0x192f7'))  # Output: ('0x7', '0xe', '0x325')
print(main('0x8f36'))   # Output: ('0x6', '0x6', '0x11e')
print(main('0x1cdab'))  # Output: ('0x3', '0x5', '0x39b')
print(main('0x9f71'))   # Output: ('0x1', '0xe', '0x13e')