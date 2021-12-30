'''
Return float value of median between two sorted arrays nums1 and nums2.
Time | Space = O(N), O(N) 
'''
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        q = []
        p1, p2 = 0, 0
        while p1 < len(nums1) and p2 < len(nums2): 
            if nums1[p1] > nums2[p2]: 
                q.append(nums2[p2])
                p2 += 1
            else: 
                q.append(nums1[p1])
                p1 += 1
        q.extend(nums1[p1:])
        q.extend(nums2[p2:])
        
        if len(q) % 2:  # odd
            return float(q[len(q)//2])
        else: 
            return float((q[len(q)//2] + q[len(q)//2-1])/2) 
