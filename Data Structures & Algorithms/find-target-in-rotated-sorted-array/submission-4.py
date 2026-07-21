class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:

            mid = left + (right - left)//2
            print(f"mid: {nums[mid]}")
            if nums[mid] == target:
                return mid

            # 先判断是哪一个半边
            # [4,5,6,1,3]
            # 断点在右边，左边是sorted
            elif nums[mid] > nums[right]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            
            # [5,6,1,2,3]
            # nums[mid] <= nums[right]
            # 断点在左边，右边是sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1