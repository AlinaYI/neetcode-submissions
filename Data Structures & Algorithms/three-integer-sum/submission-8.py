class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        duplicated = set()
        hashmap = {}
        res = set()

        # nums[i]
        for i in range(len(nums)):
            if nums[i] in duplicated:
                continue
            
            duplicated.add(nums[i])
            diff = 0 - nums[i]

            for j in range(i+1, len(nums)):
                third = diff - nums[j]
                if third in hashmap and hashmap[third] == i:
                    res.add( tuple(sorted((nums[i], nums[j], third))) )
                
                hashmap[nums[j]] = i
        return list(res)