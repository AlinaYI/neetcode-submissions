class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # 这里就是要找最小的数字
        # 那就是要找到这个split的点
        left, right = 0, len(nums)-1

        while left <= right:
            mid = left + (right-left)//2

            # nomarlly, mid < rightest
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[left]