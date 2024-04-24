class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        maxi = -1
        key = -1
        for e in nums:
            if e in dic:
                dic[e] = dic[e] + 1
            else:
                dic[e] = 1
            if dic[e] > maxi:
                maxi = dic[e]
                key = e
        
        return key