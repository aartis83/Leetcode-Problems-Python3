# O(N) TIME | O(1) SPACE
class Solution:
    def isPalindrome(self, s):

        import re
        s = re.sub(r'[\W_]', '', s).lower()

        left , right = 0, len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True



