import unittest
from hamming import encode_hamming_code, decode_hamming_code
from hamming import check_hamming_code

"""
    encoder 7, 4

    000100000101 -> 110100100000000100101  -- multiple blocks, correct size
    0001 -> 1101001  --  single block, correct size
    00011 -> 11010011110000   -- single block, wrong size
    00011001100101001101010101 -> 1101001001100100110011001100101010101001011001100 -- multiple blocks, wrong size


    check 7, 4

    1101001 0001000 0100101 -> 1101001 0000000 0100101  -- multiple blocks, 1 wrong block
    1001001 -> 1101001  --  single block
    11010001110001 -> 11010011110000   -- 2 wrong blocks
    1101101001110100100011011100100010101101011001000 -> 1101001001100100110011001100101010101001011001100 -- multiple wrong blocks


    decoder 7, 4

    110100100000000100101 -> 000100000101
    1101001 -> 0001
    11010011110000 -> 00011000
    1101001001100100110011001100101010101001011001100 -> 0001100110010100110101010100

"""


class TestHamming(unittest.TestCase):
    def test_encode_hamming_code(self):
        self.assertEqual(encode_hamming_code('0001'), "1101001")
        self.assertEqual(encode_hamming_code('000100000101'), "110100100000000100101")
        self.assertEqual(encode_hamming_code('00011'), "11010011110000")
        self.assertEqual(encode_hamming_code('00011001100101001101010101'),
                         "1101001001100100110011001100101010101001011001100")

    def test_check_hamming_code(self):
        self.assertEqual(check_hamming_code('110100100010000100101'), "100100100000000100101")
        self.assertEqual(check_hamming_code('1001001'), "1101001")
        self.assertEqual(check_hamming_code('11010001110001'), "11010011110000")
        self.assertEqual(check_hamming_code('1101101001110100100011011100100010101101011001000'),
                         "1101001001100100110011001100101010101001011001100")

    def test_decode_hamming_code(self):
        self.assertEqual(decode_hamming_code('110100100000000100101'), "000100000101")
        self.assertEqual(decode_hamming_code('1101001'), "0001")
        self.assertEqual(decode_hamming_code('11010011110000'), "00011000")
        self.assertEqual(decode_hamming_code('1101001001100100110011001100101010101001011001100'), "0001100110010100110101010100")


if __name__ == '__name__':
    unittest.main()
