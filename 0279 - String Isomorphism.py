class Solution:
    def solve(self, s, t):
        map_dict1, map_dict2 = {}, {}

        for i in range(len(s)):
            if s[i] not in map_dict1:
                if t[i] in map_dict2: return False
                map_dict1[s[i]], map_dict2[t[i]] = t[i], s[i]

            elif map_dict1[s[i]] != t[i]:
                return False

        return True
        
