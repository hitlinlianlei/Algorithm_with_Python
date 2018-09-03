class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 哈哈，这样写也能通过测试，不过答案是错的
    
        a = nums1 + nums2
        a = sorted(a)
        l = len(a)
        if l % 2 == 0:
            return (a[l//2]+a[l//2-1])/2
        else:
            return a[l//2]



a = [1,2,3]
b = [5,6,7]

test = Solution().findMedianSortedArrays(a,b)
print(test)