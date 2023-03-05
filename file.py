def encode_val(k, r, val):
    code_word = 0
    for i in range(r):
        if (val >> i) & 1:
            code_word |= (1 << (3 * i)) | (1 << (3 * i + 1)) | (1 << (3 * i + 2))
        else:
            code_word |= (0 << (3 * i)) | (0 << (3 * i + 1)) | (0 << (3 * i + 2))
    return code_word


def decode_val(k, r, code_word):
    val = 0
    for i in range(k):
        bit_triplet = ((code_word >> (3 * i)) & 7)
        if bit_triplet >= 4:
            val |= (1 << i)
    return val


def ham_dist(num1, num2):
    bin_num1 = bin(num1)[2:].zfill(max(len(bin(num1)), len(bin(num2))))
    bin_num2 = bin(num2)[2:].zfill(max(len(bin(num1)), len(bin(num2))))

    hamming_distance = 0
    for i in range(len(bin_num1)):
        if bin_num1[i] != bin_num2[i]:
            hamming_distance += 1

    return hamming_distance


def decode_and_correct(data):
    decoded_data = []
    for value in data:
        encoded_val = encode_val(4, 3, value)
        hamming_dist_1 = ham_dist(encoded_val, encode_val(4, 3, 0b001))
        hamming_dist_2 = ham_dist(encoded_val, encode_val(4, 3, 0b010))
        hamming_dist_3 = ham_dist(encoded_val, encode_val(4, 3, 0b100))

        if hamming_dist_1 <= 1:
            corrected_val = decode_val(4, 3, 0b001)
        elif hamming_dist_2 <= 1:
            corrected_val = decode_val(4, 3, 0b010)
        elif hamming_dist_3 <= 1:
            corrected_val = decode_val(4, 3, 0b100)
        else:
            corrected_val = decode_val(4, 3, encoded_val)

        decoded_data.append(corrected_val)

    return decoded_data


data = [815608, 2064837, 2093080, 2063879, 196608, 2067983, 10457031, 1830912, 2067455, 2093116, 1044928, 2064407,
        6262776, 2027968, 4423680, 2068231, 2068474, 1999352, 1019903, 2093113, 2068439, 2064455, 1831360, 1936903,
        2067967, 2068456]

decoded_data = decode_and_correct(data)
message = ''.join([chr(val) for val in decoded_data])

print(message)
