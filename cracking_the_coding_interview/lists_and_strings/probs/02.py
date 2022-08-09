""" 
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.
Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling
Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

"""


def duplicateZeros(arr):
    # loop through to find instances of zero
   
        i = 0

        while i < len(arr) -1:
            if arr[i] == 0:
                arr.insert(i+1,0)
                del arr[len(arr)-1]
                i = i +2
            else:
                i = i +1
        
        print(arr)
duplicateZeros(arr=[1,2,3,0,1,2,3,0])