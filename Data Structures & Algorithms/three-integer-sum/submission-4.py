class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        hashmap = {} # nums-> idx
        res = set()
        duplicated = set()

        for i, n in enumerate(nums):
            # first
            if n not in duplicated:
                duplicated.add(n)
                diff = 0 - nums[i]
            
                # second = nums[j]
                for j in range(i+1, len(nums)):
                    
                    # third
                    third = diff - nums[j]
                    if third in hashmap and hashmap[third] == i:
                        res.add( tuple(sorted([nums[i], nums[j], third])) )
                    
                    hashmap[nums[j]] = i
        return list(res)