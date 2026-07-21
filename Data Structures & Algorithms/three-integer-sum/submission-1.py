class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        '''
        brute force, three while loop, On^3
        two pointer + while loop, On^2, Onlogn * n --> On^2, On^2
        set , hashmap -> store On^2 On^2
        '''

        hashmap = {}
        res = set()
        duplicates = set()

        for i in range(len(nums)):
            # difference = target - nums[i]
            # 0 - nums[i]
            if nums[i] not in duplicates:
                duplicates.add(nums[i])
                difference = -nums[i]

                for j in range(i+1, len(nums)):
                    diff = difference - nums[j]
                    if diff in hashmap and hashmap[diff] == i:
                        res.add( tuple(sorted((nums[i], nums[j], diff))) )
                    hashmap[nums[j]] = i
        return list(res)


