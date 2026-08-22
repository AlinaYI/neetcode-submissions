class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # TC On^2
        # SC On
        # hashmap = {}
        # duplicated = set()
        # res = set()
        
        # # first num : nums[i]
        # for i in range(len(nums)):
        #     if nums[i] in duplicated:
        #         continue
        #     duplicated.add(nums[i])
        #     diff = 0 - nums[i]

        #     # second: nums[j]
        #     for j in range(i+1, len(nums)):
        #         # third diff - nums[j]
        #         third = diff - nums[j]
        #         if third in hashmap and hashmap[third] == i:
        #             res.add(tuple(sorted((nums[i], nums[j], third))))
        #         hashmap[nums[j]] = i
        
        # return list(res)


        # TC On^2
        # SC O1
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            
            if i >0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i+1, len(nums)-1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left +=1
                elif total > 0:
                    right -= 1
                else:
                    res.append( [nums[i], nums[left], nums[right]] )
                    left += 1
                    right -=1

                    while left < right and nums[left] == nums[left -1]:
                        left +=1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
        return res