class Solution:
    def solve(self, orders):
        picked_up, delivered = set(), set()

        for order in orders:
            letter, number = order[0], order[1:]

            if letter == 'P':
                if number in picked_up: return False
                picked_up.add(number)
            if letter == 'D':
                if number not in picked_up or number in delivered: return False
                delivered.add(number)
            
        return picked_up == delivered
