class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # 思路就是在两个list各切一刀
        # 然后让list1 和list2的左边可以组成 合并之后整个的左边
        # 只要找到中间的位置就行

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        totalLen = len(nums1)+len(nums2)
        halfLen = (totalLen+1)//2

        left = 0
        right = len(nums1)

        while left <= right:
            list1CutIdx = left + (right-left)//2
            list2CutIdx = halfLen - list1CutIdx

            # list1: [1, 5 |] 
            # list2: [2| 3,4,6]
            if list1CutIdx > 0 and list2CutIdx < len(nums2) and nums1[list1CutIdx-1] > nums2[list2CutIdx]:
                right = list1CutIdx - 1
            elif list2CutIdx > 0 and list1CutIdx < len(nums1) and nums1[list1CutIdx] < nums2[list2CutIdx-1]:
                left = list1CutIdx + 1
            
            # find the cur place right
            else:
                maxLeft = 0
                if list1CutIdx == 0:
                    maxLeft = nums2[list2CutIdx-1]
                elif list2CutIdx == 0:
                    maxLeft = nums1[list1CutIdx - 1]
                else:
                    maxLeft = max(nums1[list1CutIdx - 1],  nums2[list2CutIdx-1])


                if (totalLen)%2 == 1:
                    return maxLeft
                
                minRight = 0
                if list1CutIdx == len(nums1):
                    minRight = nums2[list2CutIdx]
                elif list2CutIdx == len(nums2):
                    minRight = nums1[list1CutIdx]
                else:
                    minRight = min(nums1[list1CutIdx],  nums2[list2CutIdx])

                return (maxLeft+minRight)/2   