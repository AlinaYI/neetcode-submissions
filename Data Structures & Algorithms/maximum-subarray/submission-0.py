class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = nums[0]
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            res = max(res, temp)
            if temp < 0 :
                temp = 0
        return res