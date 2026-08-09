class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums)-1
        while left <= right:

            mid = left + (right-left)//2

            # 如果中间的数字，比最右边的小
            # 如果右边这部分是升序，那么最小的在左边
            if nums[mid] <= nums[-1]:
                right = mid -1
            else:
                left = mid + 1

        return nums[left]