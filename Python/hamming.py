def encode_hamming_code(data, total_bits=7, data_bits=4):
    data = list(data)
    if len(data) % data_bits != 0:
        data += ["0"] * (data_bits - (len(data) % data_bits))
    encoded_data_template = [[None] * total_bits] * (len(data)//data_bits)
    parity_indexes = [(2**x)-1 for x in range(total_bits-data_bits)]
    encoded_data = []
    for index, block in enumerate(encoded_data_template):
        encoded_data_line = block[:]
        for i in range(total_bits-data_bits):
            # this loop fills with 0's all the parity positions
            encoded_data_line[(2**i)-1] = "0"
        for j in range(len(block)):
            # this loop places the data bits on their positions
            if j not in parity_indexes:
                encoded_data_line[j] = data.pop(0)
        encoded_data += [encoded_data_line]
    result = []

    for block in encoded_data:
        result += compute_parity_bits(block)

    return "".join(result)


def check_hamming_code(data, total_bits=7, data_bits=4):
    if len(data) % total_bits != 0:
        raise ValueError("Data size error")
    result = []
    for block_index in range(0, len(data), total_bits):
        result += [check_hamming_block(data[block_index:
                                            block_index+total_bits])]
    return "".join(result)


def check_hamming_block(data, total_bits=7, data_bits=4):
    data = list(data)
    parity_indexes = [(2**x) for x in range(total_bits-data_bits)]
    parity_checker = 0b1
    indexes_with_errors = []
    for parity_index in parity_indexes:
        check_indexes = [x-1 for x in range(parity_index, len(data)+1) if
                         parity_checker & x != 0]
        check_sum = 0
        for check_index in check_indexes:
            check_sum += int(data[check_index])

        indexes_with_errors += [check_sum % 2]
        parity_checker = parity_checker << 1

    if 1 in indexes_with_errors:
        error_index = sum([bit*(2**index) for index, bit in enumerate(
            indexes_with_errors)]) - 1
        if data[error_index] == '0':
            data[error_index] = "1"
        else:
            data[error_index] = "0"

    return ''.join(data)


def compute_parity_bits(data, parity_size=3):
    data = list(data)
    parity_indexes = [(2**x) for x in range(parity_size)]
    parity_checker = 0b1
    for parity_index in parity_indexes:
        check_indexes = [x-1 for x in range(parity_index, len(data)+1) if
                         parity_checker & x != 0]
        check_sum = 0
        for check_index in check_indexes:
            check_sum += int(data[check_index])
        data[parity_index-1] = str(check_sum % 2)
        parity_checker = parity_checker << 1

    return data


def decode_hamming_code(encoded_data, full_size=7, data_size=4):
    if len(encoded_data) % full_size != 0:
        raise ValueError("block size error")
    corrected = check_hamming_code(encoded_data, full_size, data_size)
    parity_indexes = [(2**x)-1 for x in range(full_size-data_size)]
    result = ""
    for block_index in range(0, len(corrected), full_size):
        for bit_index, bit in enumerate(
                corrected[block_index:block_index+full_size]):
            if bit_index not in parity_indexes:
                result += bit
    return result
