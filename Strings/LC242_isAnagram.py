class Solution:
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        s_count = {}

        for s_char in s:
            if s_char not in s_count:
                s_count[s_char] = 0
            s_count[s_char] += 1

        for t_char in t:
            if t_char not in s_count or s_count[t_char] == 0:
                return False
            s_count[t_char] -= 1

        return True

