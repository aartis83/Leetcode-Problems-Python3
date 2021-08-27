# Design an algorithm to encode a list of strings to a string. The
# encoded string is then sent over the network and is decoded back to
# the original list of strings.

# Example
# encoded_string = encode(['kevin', 'is', 'great'])
#                  "5/kevin2/is5/great"

# decoded_array = decode("5/kevin2/is5/great")
#                 ['kevin', 'is', 'great']

# Notes
# - Do not use class member/global/static variables to store states. Your
#   encode and decode should be stateless
# - Do not use an library method such as eval or serialize methods. You
#   must implement your OWN encode and decode algorithm


class Solution:
    def encode(self, strs):
        encoded = ""

        for word in strs:
            length = len(word)
            encoded += str(length) + '/' + word
        return encoded

    def decode(self, str):
        decoded = []
        start_pos = 0
        while start_pos < len(str):
            slash_pos = str.index('/', start_pos)
            length = int(str[start_pos : slash_pos])
            start_pos = slash_pos + 1
            decoded. append(str[start_pos: start_pos + length])
            start_pos += length
        return decoded

