class Solution:
    def solve(self, n, friends):
        people_set = set()
        for friend1, friend2 in friends:
            people_set.add(friend1)
            people_set.add(friend2)
        return len(people_set) == n
