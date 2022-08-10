"""Reverse an array in place
i.e-> input is [1,2,3,4,5] output -> [5,4,3,2,1]"""

def reverseArray(nums):
    # 1- set pointers to first and last items
    start_index = 0 # point to first item ...
    end_index = len(nums)-1 # point to last item ...  -1 bc index start at zero
    
    # 2- while end > start 
    while end_index > start_index: 
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index] # 3 swap two items in the list data structures 
        start_index = start_index + 1 # increment start index by 1
        end_index = end_index - 1 # decrement end index by 1


# reverseArray(nums=[1,2,3,4,5])
if __name__ == '__main__':
    
    n = [1, 2, 3, 4]

    n.reverse()
    print(n)