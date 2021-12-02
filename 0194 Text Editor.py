class Solution:
    def solve(self, s):
        stack = []
        for i, char in enumerate(s):
            if i-1 >= 0 and char == '-' and s[i-1] == '<':
                stack.pop()
                if stack: stack.pop()
            else:
                stack.append(char)
        return  ''.join(stack)
