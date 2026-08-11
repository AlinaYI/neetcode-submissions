class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # 就是要找到左右两边
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right-left)//2

            # 如果是有序的，那么这个情况不可能发生，
            # 所以就知道这里的右边是小的部分
            if nums[mid] > nums[-1]:
                left = mid + 1
            
            # 要不然就是找右边
            else:
                right = mid
        return nums[left]