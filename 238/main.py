from typing import List

class Solution:   

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        aux_arr = [1] * len(nums)
        right_to_left = 1
        for i in range(len(nums)):
            aux_arr[i] *= right_to_left
            right_to_left *= nums[i]
        left_to_right = 1
        for i in range(len(nums)-1, -1, -1):
            aux_arr[i] *= left_to_right
            left_to_right *= nums[i]
        return aux_arr
                    