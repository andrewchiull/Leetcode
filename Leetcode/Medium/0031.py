from itertools import permutations
from typing import List
# from pprint import pprint as print

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        print(list(permutations(nums,)))
        flag = False
        for perm in permutations(nums):
            if nums == list(perm):
                flag = True
            elif flag:
                print(perm)
                break
        # nextIndex = allPermutation.index(tuple(nums)) + 1
        # if nextIndex == len(allPermutation):
        #     nextIndex = 0
        # nums.clear()
        # nums.extend(list(allPermutation[nextIndex]))
        # print(nums)
        
        
        # allPermutation = sorted(list(set(permutations(nums))))
        # print(allPermutation, width=20)
        
'''        print(nums)
        for i in range(2, len(nums)+1):
        # i = -2
            print(nums[-i], nums[-i+1])
            if nums[-i] < nums[-i+1]:
                nums.insert(-i+1, nums.pop(-i+1))
            print(nums)'''
        
sol = Solution()
sol.nextPermutation([3, 2 ,1])
# sol.nextPermutation([1, 3, 2])
