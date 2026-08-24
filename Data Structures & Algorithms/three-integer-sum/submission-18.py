class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        for loop找第一个，然后第二个和第三个就跟twosum一样
        hashmap 记录数字和 第一个数字的idx，用来去除掉不是这个level的数字
        防止拿错
        tc: On^2， 两个for loop？
        sc: On

        sorted
        for loop找第一个，用left，right找剩下两个
        tc: sort: O(n log n)
            for + two pointers: O(n²)
            overall: O(n²)
        sc:O1
        '''
        
        nums.sort()
        res = []
        for i in range(len(nums)):
            # 提前剪枝，后面就不用看了
            # 因为sort过，所以后面的数字肯定也大于1
            # 三个大于0的数字不可能组成0，直接剪枝
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i+1, len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total > 0:
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right-= 1

        return res
