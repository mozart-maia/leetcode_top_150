from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        last = 99999
        count = 0
        myDic = {}
        for i in range(len(nums)):
            if nums[i] in myDic:
                if myDic[nums[i]] == 2:
                    nums[i] = last
                    count += 1
                    continue
                else:
                    myDic[nums[i]] = myDic[nums[i]] + 1
            else:
                myDic[nums[i]] = 1

        nums.sort()
        return len(nums) - count
