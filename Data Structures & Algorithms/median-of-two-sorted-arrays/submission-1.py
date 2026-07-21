class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        brute force
        nums3 = nums1 + nums2
        mid number --> if odd return
                       if enev, calculate the median
        
        tc : Om+n
        sc : Om+n

        find mid --> two mid
        num1 = [1,      3]
                pointer
        num2 = [2,      4]
                     pointer
        '''

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left = 0
        right = m
        half_len = (n+m+1)//2 # find break point

        while left <= right:
            '''
            [1, 2, 3]

            [4, 5, 6]
            '''
            
            # mid of the nums1
            i = left + (right - left)//2
            # actual break point we want -->even/odd
            j = half_len - i

            # mid of nums1 in range, too big
            if i > 0 and nums1[i-1] > nums2[j]:
                right = i - 1
            # too small
            elif i < m and nums2[j-1] > nums1[i]:
                left = i + 1
            else:
                max_of_left = 0
                if i == 0:
                    max_of_left = nums2[j-1]
                elif j == 0:
                    max_of_left = nums1[i-1]
                else:
                    max_of_left = max(nums1[i-1], nums2[j-1])
                
                # odd
                if (m+n)%2 == 1:
                    return max_of_left
                
                min_of_right = 0
                if i == m:
                    min_of_right = nums2[j]
                elif j == n:
                    min_of_right = nums1[i]
                else:
                    min_of_right = min(nums1[i], nums2[j])
                return (max_of_left + min_of_right)/2
                