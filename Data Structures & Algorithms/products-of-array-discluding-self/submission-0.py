class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        这道题，double for loop On2

        prefix [1,2,8,48]
        postfix[1,48,24,6]

        对于1来说，就是1后面的，也就是48
        2： 2前面的1 * 24 idx[1]前后
        4： 4前面的2 * 4后面的6 idx[2]前后
        6： 6前面的48 * 1
        '''

        prefix = [1]*len(nums)
        postfix = [1]*len(nums)
        res = [1]*len(nums)

        # [1,1,1,1]
        # [1,1,1,1]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]
        
        for i in range(len(nums)-2, -1, -1):
            postfix[i] = postfix[i+1]*nums[i+1]

        for i in range(len(nums)):
            res[i] = prefix[i]*postfix[i]
        
        return res

