class Solution:
    def solve(self, relations):
        if not relations: return []
        following = defaultdict(list)
        uniq = set()

        for a, b in relations:
            following[a].append(b)
            if a in following[b]:
                uniq.add(a)
                uniq.add(b)

        return sorted(list(uniq))
