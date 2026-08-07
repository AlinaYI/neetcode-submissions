class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        left = 0
        right = len(nums)-1

        while left < right:
            '''
            right 是参照点，用来判断 mid 到 right 之间有没有跨 rotation。
            '''
            
            mid = left + (right-left)//2

            # [3,4,5,1,2] 找 1
            if nums[mid] > nums[right]:
                left = mid + 1
            
            else:
                right = mid
        return nums[left]