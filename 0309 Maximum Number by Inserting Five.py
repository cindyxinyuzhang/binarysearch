class Solution:
    def solve(self, n):
        str_n = str(n)

        if n > 0:
            for i in range(len(str_n)):
                if str_n[i] < '5':
                    return int(str_n[:i] + '5' + str_n[i:])

        else:
            for i in range(1, len(str_n)):
                if str_n[i] > '5':
                    return int(str_n[:i] + '5' + str_n[i:])
        
        return int(str_n +'5')
