class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        # 让nums1永远保持长度最小
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        nums1Len, nums2Len = len(nums1), len(nums2)
        left = 0
        right = nums1Len

        # 要找的中位数的位置
        # 就是两个list 加起来中间的位置
        # total 除以 2，向上取整。
        leftSize  = (nums1Len + nums2Len+1)//2

        # 只 search 一个数组，因为另一个 cut 可以算出来；
        # search 短数组是为了 cut 不容易越界，而且复杂度最好。
        while left <= right:
            mid = (left + right)//2
            j = leftSize - mid

            if mid > 0 and j < nums2Len and nums1[mid-1] > nums2[j]:
                right = mid-1
            elif j > 0 and mid < nums1Len and nums2[j-1] > nums1[mid]:
                left = mid+1
            else:
                maxOfLeft = 0 
                if mid == 0:
                    maxOfLeft = nums2[j-1]
                elif j == 0:
                    maxOfLeft = nums1[mid - 1]
                else:
                    maxOfLeft = max(nums1[mid-1], nums2[j-1])

                if (nums1Len + nums2Len)%2 == 1:
                    return maxOfLeft
                
                minOfRight = 0
                if mid == nums1Len:
                    minOfRight = nums2[j]
                elif j == nums2Len:
                    minOfRight = nums1[mid]
                else:
                    minOfRight = min(nums1[mid], nums2[j])
                
                return (maxOfLeft + minOfRight)/2