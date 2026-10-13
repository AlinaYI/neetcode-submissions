class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # 这里要找到的是break 点
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = left + (right-left)//2

            # normally, nums[mid] > nums[right]
            # 也就是意味着，最小的值在左半边
            if nums[mid] <= nums[-1]:
                right = mid - 1
            else:
                left = mid + 1
        return nums[left]