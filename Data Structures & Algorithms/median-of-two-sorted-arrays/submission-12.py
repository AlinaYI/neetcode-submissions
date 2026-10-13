class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        total = len(nums1)+len(nums2)
        
        # split total into half
        halfLen = (total+1)//2

        # 目标是找到前半部分，也就是两个nums分别由pointer
        # 
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        left, right = 0, len(nums1)
        while left <= right:
            nums1Cut = left + (right-left)//2
            nums2Cut = halfLen - nums1Cut
        
            # [1, 5|]
            # [2| 3, 4, 6]
            if nums1Cut > 0 and nums2Cut <  len(nums2) and nums1[nums1Cut-1] > nums2[nums2Cut]:
                right = nums1Cut - 1
            elif nums2Cut > 0 and nums1Cut < len(nums1) and nums2[nums2Cut -1] > nums1[nums1Cut]:
                left = nums1Cut + 1
            else:

                maxLeft = 0
                if nums1Cut == 0:
                    maxLeft = nums2[nums2Cut - 1]
                elif nums2Cut == 0:
                    maxLeft = nums1[nums1Cut - 1]
                else:
                    maxLeft = max(nums1[nums1Cut-1], nums2[nums2Cut-1])
                
                if total%2 == 1:
                    return maxLeft

                minRight = 0
                if nums1Cut == len(nums1):
                    minRight = nums2[nums2Cut]
                elif nums2Cut == len(nums2):
                    minRight = nums1[nums1Cut]
                else:
                    minRight = min(nums2[nums2Cut], nums1[nums1Cut])
                return (maxLeft + minRight) /2
