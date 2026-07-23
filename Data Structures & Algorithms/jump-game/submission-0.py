class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = len(nums) - 1

        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= reach:
                reach = i
        return reach == 0