from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        mySet = set()
        for each in nums:
            mySet.add(each)
        nums[:] = list(mySet)
        nums.sort()
        return len(nums)