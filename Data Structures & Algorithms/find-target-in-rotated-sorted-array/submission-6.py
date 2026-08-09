class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums)-1

        while left<=right:
            
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid

            # 说明rotated了，然后断点在右边
            elif nums[mid] > nums[right]:
                # 那么左边就是sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            # 断点在左边
            else:
                # 那右边就是sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
            