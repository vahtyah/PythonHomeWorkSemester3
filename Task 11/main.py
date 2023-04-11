import struct


def main(data):
    format_A = '>BfH4b'
    format_B = '>dHdhB8h'
    format_C = '>Bi8Hf'
    format_D = '>HIII'

    signature = struct.unpack_from('>4B', data)
    if signature != (0x1f, 0x47, 0x5a, 0x4f):
        return None

    a_data = struct.unpack_from(format_A, data, offset=4)
    a = {"A1": a_data[0],
         "A2": a_data[1],
         "A3": {},
         "A4": list(a_data[3:])
         }
    b_data = struct.unpack_from(format_B, data, offset=a_data[2])
    b = {
        "B1": b_data[0],
        "B2": {},
        "B3": b_data[2],
        "B4": b_data[3],
        "B5": b_data[4],
        "B6": list(b_data[5:])
    }
    a["A3"] = b
    c_data = struct.unpack_from(format_C, data, offset=b_data[1])
    c = {
        "C1": c_data[0],
        "C2": c_data[1],
        "C3": [],
        "C4": c_data[10]
    }
    b["B2"] = c
    i = 2
    while i < 10:
        x = struct.unpack_from(format_D, data, offset=c_data[i])
        andress = x[3]
        elem = {
            "D1": x[0],
            "D2": x[1],
            "D3": []
        }
        for j in range(x[2]):
            elem["D3"].append(
                struct.unpack_from('> h', data, offset=andress)[0])
            andress += struct.calcsize('> h')

        c["C3"].append(elem)
        i += 1
    return a
