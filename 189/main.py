from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        rotate = len(nums) + k
        aux = [0] * len(nums)

        for i in range(len(nums)):
            aux[(i+k)%len(nums)] = nums[i]

        nums[:] = aux