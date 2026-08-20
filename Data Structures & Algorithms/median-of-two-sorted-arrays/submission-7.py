class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # cut 两个list
        
        totalLen = len(nums1) + len(nums2)
        halfLen = (totalLen+1)//2
        # nums1一半 + nums2一半 == halfLen

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # 对nums1 binary search
        left, right = 0, len(nums1)
        while left <= right:
            nums1Cut = left + (right-left)//2
            nums2Cut = halfLen - nums1Cut

            # 就是要对比两个cut点的数字大小
            # 如果nums1cut的数字 > nums2cut的点
            #   就说明nums2Cut可以往右移动，就是看还能不能再多切一点nums2
            #   如果nums2Cut要往右移动，那么nums1Cut就要往左移动
            
            # list1 = [1, 5 |]
            # list2 = [2 | 3, 4, 6]
            if nums1Cut > 0 and nums2Cut < len(nums2) and nums1[nums1Cut-1] > nums2[nums2Cut]:
                right= nums1Cut - 1
            elif nums2Cut > 0 and nums1Cut < len(nums1) and nums1[nums1Cut] < nums2[nums2Cut-1]:
                left = nums1Cut + 1
            # 找到了cut点
            else:
                maxLeft = 0
                # 就是不要整个list1, 那么最大的就是list2cut的位置
                if nums1Cut == 0:
                    maxLeft = nums2[nums2Cut - 1]
                # 不要整个list2， 那最大的就是list1Cut的位置
                elif nums2Cut == 0:
                    maxLeft = nums1[nums1Cut - 1]
                else:
                    maxLeft = max(nums1[nums1Cut - 1], nums2[nums2Cut - 1])
                
                if totalLen%2 == 1:
                    return maxLeft
                
                minRight = 0
                # 如果看右边的话，主要就是看是不是cut了全部的
                # 所以这里就是看是不是全要
                # 如果list1全要, 那么就是list2后面的比list2的要大
                if nums1Cut == len(nums1):
                    minRight = nums2[nums2Cut]
                elif nums2Cut == len(nums2):
                    minRight = nums1[nums1Cut]
                else:
                    minRight = min(nums1[nums1Cut], nums2[nums2Cut])
                
                return (minRight + maxLeft)/2