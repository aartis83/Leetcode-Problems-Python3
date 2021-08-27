# O(N) TIME | O(N) SPACE
class Solution:
    def isValid(self, s):
        stack = []
        pairs = {'{': '}', '[': ']', '(' : ')'}

        for char in s:
            if char in pairs:
                stack.append(char)
            elif len(stack) == 0 or pairs[stack.pop()] != char:
                return False
        return len(stack) == 0




