class Solution:
    def solve(self, dictionary, s):
        if not s or not dictionary: return True

        d = defaultdict(int)
        for i, char in enumerate(dictionary):
            d[char] += i+1

        last_char = s[0]
        for curr_char in s:
            if d[curr_char] == 0:
                continue
            elif d[curr_char] < d[last_char]:
                return False
            last_char =  curr_char        
        
        return True
            
