class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # 这道题就是找左右哪个部分小
        # 因为要找minmum
        left  = 0
        right = len(nums)-1

        while left <= right:

            mid = left + (right-left)//2

            # 如果中间的值比右边的大，就是说明minmum在右边
            if nums[mid] <= nums[-1]:
                right = mid - 1
            else:
                left = mid + 1

        return nums[left]