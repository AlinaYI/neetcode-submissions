class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = set()
        hashmap = {} # num:idx
        duplicated = set()
        # first num
        for i in range(len(nums)):
            if nums[i] in duplicated:
                continue
            
            duplicated.add(nums[i])
            diff = 0 - nums[i]
            
            # second
            for j in range(i+1, len(nums)):
                
                # third
                third = diff - nums[j]
                if third in hashmap and hashmap[third] == i:
                    res.add( tuple(sorted( (nums[i], nums[j], third) )) )
                hashmap[nums[j]] = i
        return list(res)