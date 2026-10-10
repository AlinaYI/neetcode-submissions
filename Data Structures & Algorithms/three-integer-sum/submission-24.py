class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # duplicate = set()
        # res = set()
        # hashmap = {}

        # # first number
        # for i in range(len(nums)):

        #     if nums[i] in duplicate:
        #         continue
        #     duplicate.add(nums[i])
        #     target = - nums[i]

        #     # second
        #     for j in range(i+1, len(nums)):
        #         third = target - nums[j]
        #         if third in hashmap and hashmap[third] == i:
        #             res.add( tuple(sorted((nums[i], nums[j], third) )) )
        #         hashmap[nums[j]] = i
        # return [list(x) for x in res]


        # On^2 O1
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            #second number + third number
            left, right = i+1, len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append( [nums[i], nums[left], nums[right]] )
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
                
                
        return res
