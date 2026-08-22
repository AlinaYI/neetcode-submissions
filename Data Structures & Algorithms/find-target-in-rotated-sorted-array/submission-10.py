class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # 这里就是要优先在顺序的part找
        left = 0
        right = len(nums)-1

        while left <= right:
            mid = left + (right-left)//2

            if nums[mid] == target:
                return mid
            
            # 正常，就是右边是有序的
            elif nums[mid] < nums[-1]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                
            else:
                # left is order
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1