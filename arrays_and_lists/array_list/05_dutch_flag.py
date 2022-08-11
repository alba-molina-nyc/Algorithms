"""Given an A array of integers - 0,1 and 2 (3 diff values). Sort this A array in linear running time using constant memory"""

def dutch_flag_problem(nums, pivot=1):
    i, j, k = 0, 0, len(nums)-1 # 1. initialize three indexes

    while j <= k:
        # current element (item at index j) is 0
        if nums[j] < pivot:
            swap(nums, i, j)
            i =+ 1
            j =+ 1
            # current element (item at index j is 1
        elif nums[j] > pivot:
            swap(nums, j, k)
            k =- 1
            # current element(item at index j) is 2
        else:
            j =- 1

    return nums


def swap(nums, index1, index2):
    nums[index1], nums[index2] = nums[index2], nums[index1] # swap items at given indexes


if __name__ == '__main__':
    print(dutch_flag_problem([1, 1, 0, 2]))
