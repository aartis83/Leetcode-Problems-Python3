# O(N) TIME | O(MIN(M,N)) SPACE N IS THE STRING LENGTH AND M IS THE CHARACTERS IN DICTIONARY(MAX-26)
class Solution:
    def lengthOfLongestSubstring(self, s):
        char_map = {}
        max_length = 0
        start = 0

        for end, end_char in enumerate(s):
            if end_char in char_map and char_map[end_char] >= start:
                start = char_map[end_char] + 1
            char_map[end_char] = end
            current = end - start + 1
            max_length = max(max_length, current)

        return max_length

