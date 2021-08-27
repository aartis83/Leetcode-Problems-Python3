class Solution:
    def backspaceCompare(self, S, T):

        s_stack = []
        t_stack = []

        for s_char in S:
            if s_char == '#':
                if s_stack:
                    s_stack.pop()

            else:
                s_stack.append(s_char)

        for t_char in T:
            if t_char == '#':
                if t_stack:
                    t_stack.pop()

            else:
                t_stack.append(t_char)

        return s_stack == t_stack