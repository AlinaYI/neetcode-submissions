class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # 这道题就是要找到target
        left, right = 0, len(nums)-1
        while left <= right:

            mid = left + (right-left)//2

            if nums[mid] == target:
                return mid

            # 说明split的点在右边，左边是肯定是
            # [小->大]
            elif nums[mid] > nums[-1]:
                # 需要闭区间，target == nums[mid] 已经处理了
                # 所以另外一边需要闭区间
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 如果split的点在左边，那么右边就是顺序的
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
