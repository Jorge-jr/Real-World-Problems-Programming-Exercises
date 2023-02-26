def encoder(data, full_size=7, data_size=4):
    
    data = list(data)
    if len(data) % data_size != 0:
        data += [0] * (len(data) % data_size)
    encoded_data = [[None] * full_size] * (len(data)//data_size)
    parity_indexes = [(2**x)-1 for x in range(full_size-data_size)]
    for index, packet in enumerate(encoded_data):
        for i in range(full_size-data_size):  # this loop fills with 0's all the parity bit positions
            packet[(2**i)-1] = "0"
        for j in range(len(packet)):  # this loop places the data bits on its positions
            if j not in parity_indexes:
                encoded_data[index][j] = data.pop(0)
    result = []
    for packet in encoded_data:
        result += fill_parity(packet)

    return result


def check(data, parity_size=3):
    data = list(data)
    parity_indexes = [(2**x) for x in range(parity_size)]
    parity_checker = 0b1
    indexes_with_errors = []   
    for parity_index in parity_indexes:
        check_indexes = [x-1 for x in range(parity_index, len(data)+1) if parity_checker & x != 0]
        check_sum = 0
        for check_index in check_indexes:
            check_sum += int(data[check_index])

        indexes_with_errors += [check_sum % 2]
        parity_checker = parity_checker << 1

    if 1 in indexes_with_errors:
        error_index = sum([bit*(2**index) for index, bit in enumerate(indexes_with_errors)]) - 1
        if data[error_index] == '0':
            data[error_index] = "1"
        else:
            data[error_index] = "0"

    return ''.join(data)


def fill_parity(data, parity_size=3):
    data = list(data)
    parity_indexes = [(2**x) for x in range(parity_size)]
    parity_checker = 0b1
    for parity_index in parity_indexes:
        check_indexes = [x-1 for x in range(parity_index, len(data)+1) if parity_checker & x != 0]
        check_sum = 0
        for check_index in check_indexes:
            check_sum += int(data[check_index])
        data[parity_index-1] = str(check_sum % 2)
        parity_checker = parity_checker << 1

    return data


def decoder(packet, full_size=7, data_size=4):

    if len(packet) % full_size != 0:
        raise ValueError("Packet size error")
    
    data_parity = []

    for chunk in range(0, len(packet), full_size):
        data_parity += [(packet[chunk:chunk+data_size], packet[chunk+data_size:chunk+full_size])]
    
    print(data_parity)


print(encoder("110011001100"))
print(check("0111000")=="0111100")
