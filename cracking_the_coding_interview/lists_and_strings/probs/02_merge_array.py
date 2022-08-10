"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
"""

def mergeSortedArrays(nums1, nums2, m, n):
    print(f'{nums1} this is nums1')
    print(f'{nums2} this is nums2')

    for i in range(len(nums1), -1):
        for j in range(len(nums2), 0):
            nums1.append(j)
            print(nums1)


mergeSortedArrays(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)