class Solution:
    def solve(self, nums):
        term_1 = min(nums)
        term_n = max(nums)
        n = len(nums)
        d = (term_n-term_1)//(n-1)
        lst = [term_1 + i*d for i in range(n)]
        return set(lst) == set(nums)
        
#Time: O(n)
#Space: O(n)
#with the min, max, and len of nums, we can find the expected common difference (d) and generate the expected list. 
#then we can check if the list is identical with nums using set. 

class Solution:
    def solve(self, nums):
        return len(set(num2-num1 for num1, num2 in zip(sorted(nums),sorted(nums)[1:]))) == 1
				
#Time: O(nlogn)
#Time: O(n)
