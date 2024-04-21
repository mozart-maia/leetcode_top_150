from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0

        for i in range(len(nums)):
            if nums[i] == val:
                count += 1
        diff = len(nums) - count
        for i in range(lencount):
            nums.remove(val)       

        return diff