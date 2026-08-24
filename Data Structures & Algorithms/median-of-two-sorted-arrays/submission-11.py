class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        totalLen = len(nums1) + len(nums2)
        halfLen = (totalLen+1)//2

        # 目标就是找到前半部分
        # part nums1 + part nums2 == halfLen
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        left, right = 0, len(nums1)
        while left <= right:
            nums1Cut = left + (right-left)//2
            nums2Cut = halfLen - nums1Cut

            # [1, 5|]
            # [2| 3, 4, 6]
            if nums1Cut > 0 and nums2Cut < len(nums2) and nums1[nums1Cut-1] > nums2[nums2Cut]:
                right = nums1Cut - 1
            elif nums2Cut > 0 and nums1Cut < len(nums1) and nums2[nums2Cut-1] > nums1[nums1Cut]:
                left = nums1Cut + 1
            else:
                maxLeft = 0
                if nums1Cut == 0:
                    maxLeft = nums2[nums2Cut-1]
                elif nums2Cut == 0:
                    maxLeft = nums1[nums1Cut-1]
                else:
                    maxLeft = max(nums1[nums1Cut-1], nums2[nums2Cut-1])

                if totalLen%2 == 1:
                    return maxLeft

                minRight = 0
                if nums1Cut == len(nums1):
                    minRight = nums2[nums2Cut]
                elif nums2Cut ==  len(nums2):
                    minRight = nums1[nums1Cut]
                else:
                    minRight = min(nums1[nums1Cut], nums2[nums2Cut])

                return (maxLeft+minRight)/2