class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # 找break point
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = left +(right-left)//2

            # normal nums[mid] < nums[-1]
            # increasing 
            if nums[mid] <= nums[-1]:
                # 说明rotate点在左边
                right = mid - 1
            else:
                left = mid + 1
        return nums[left]