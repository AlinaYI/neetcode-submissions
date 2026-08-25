from functools import cache
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        这里的decision tree
        这里有一个问题就是，有负数，那么就是如果负数又遇到一个负数，
        就会变得很大，所以还有一个option就是接前面最小的

                    nums[i]
            /           |           \
 自己重新开始  接上前面的subarray     接前面的最小值
    nums[i]           preMax            preMin

        那这里的就是要记录idx，然后就是要看max(nums[i], nums[i]*nums[i-1])
        '''

        @cache
        def dfs(i):
            if i == 0:
                return nums[0], nums[0]
            
            prevMax, prevMin = dfs(i-1)
            currMax = max(nums[i], nums[i]*prevMax, nums[i]*prevMin)
            currMin = min(nums[i], nums[i]*prevMax, nums[i]*prevMin)
            return currMax, currMin
        res = nums[0]
        for i in range(len(nums)):
            currMax, _ = dfs(i)
            res = max(res, currMax)
        return res

        
        # bottom up
        # 因为有两个status，所以用两个dp list来维护
        n = len(nums)
        maxDp = [0]*n
        minDp = [0]*n

        maxDp[0] = nums[0]
        minDp[0] = nums[0]

        res = nums[0]

        for i in range(1, n):
            maxDp[i] = max(nums[i], nums[i]*maxDp[i-1], nums[i]*minDp[i-1])
            minDp[i] = min(nums[i], nums[i]*maxDp[i-1], nums[i]*minDp[i-1])

            res = max(res, maxDp[i])
        return res

        # 优化
        # On O1
        n = len(nums)
        prevMax = nums[0]
        prevMin = nums[0]
        res = nums[0]
        for i in range(1, n):
            currMax = max(nums[i], nums[i]*prevMax, nums[i]*prevMin)
            currMin = min(nums[i], nums[i]*prevMax, nums[i]*prevMin)

            prevMax = currMax
            prevMin = currMin

            res = max(res, currMax)
        return res

