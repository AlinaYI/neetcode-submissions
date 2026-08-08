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
            # 两端list， 分别cut
            cut1 = (left + right)//2
            cut2 = leftSize - cut1

            # 如果都在bound里面，然后list1 cut最末尾的数字大于list2cut末尾的数字
            # list1: [1, 5 |] --> cutIdx = 2
            # list2: [2,| 3, 4, 6] --> cutIdx = 1
            # 左边切多了，所以右边要多切一点
            # 那就把切左边的 变成cut1-1
            if cut1 > 0 and cut2 < nums2Len and nums1[cut1-1] > nums2[cut2]:
                right = cut1-1
            elif cut2 > 0 and cut1 < nums1Len and nums2[cut2-1] > nums1[cut1]:
                left = cut1+1
            else:
                maxOfLeft = 0 
                # 如果不需要list1， 那就直接取list2的值
                if cut1 == 0:
                    maxOfLeft = nums2[cut2-1]
                elif cut2 == 0:
                    maxOfLeft = nums1[cut1 - 1]
                else:
                    maxOfLeft = max(nums1[cut1-1], nums2[cut2-1])

                # 如果是奇数字
                if (nums1Len + nums2Len)%2 == 1:
                    return maxOfLeft
                
                # 如果是偶数
                minOfRight = 0
                # 如果list1整条都要
                # 那最小的就是cut2的值
                if cut1 == nums1Len:
                    minOfRight = nums2[cut2]
                elif cut2 == nums2Len:
                    minOfRight = nums1[cut1]
                else:
                    minOfRight = min(nums1[cut1], nums2[cut2])
                
                return (maxOfLeft + minOfRight)/2