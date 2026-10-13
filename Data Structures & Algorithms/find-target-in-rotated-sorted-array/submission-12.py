class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right= len(nums)-1

        while left <= right:
            mid = left + (right-left)//2

            if nums[mid] == target:
                return mid
            #  nums[mid] < nums[-1], no rotated
            elif nums[mid] < nums[-1]:
                if nums[mid] < target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1