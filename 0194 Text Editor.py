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

class Solution:
    def solve(self, s):
        stack = []
        i = 0
        while i < len(s):
            if i+1 < len(s) and s[i:i+2] == '<-':
                if stack: stack.pop()
                i += 1
            else:
                stack.append(s[i])
            i += 1
        return  ''.join(stack)
