# Given a string s, find the longest palindromic substring in s
# --- Example
# longestPalindrome("cbbd") --> "bb"
# longestPalindrome("abba") --> "abba"
# longestPalindrome("a") --> "a"
# O(N^2) TIME | O(1) SPACE
class Solution:
    def longestPalindrome(self, s):
       res = ""

       for i in range(len(s)):
           current = self.expandMiddle(s, i - 1, i + 1)
           in_between = self.expandMiddle(s, i, i + 1)
           res = max(res, current, in_between, key=len)

       return res

    def expandMiddle(selfself, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]


