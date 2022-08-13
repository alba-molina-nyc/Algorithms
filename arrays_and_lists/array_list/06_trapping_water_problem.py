# Find the maximum amount of water that can be trapped within a given set of bars where each bar's width is 1 unit

def trapping_water_problem(heights):
    # if have less than 3 index then cannot hold water
    if len(heights) < 3:
        return 0


    left_max = [0 for _ in range(len(heights))] #initialize left
    right_max = [0 for _ in range(len(heights))] #initialize right

    # deal with left_max values
    for i in range(1, len(heights)): # skip first item bc first item has 0 by default
        left_max[i] = max(left_max[i - 1], heights[i - 1]) #make sure the max left item is the maximum aka storing maximum value so far

    
    # deal with right_max values
    for i in range(len(heights) -2, -1, -1): # skip first item bc first item has 0 by default
        right_max[i] = max(right_max[i + 1], heights[i + 1]) #make sure the max left item is the maximum aka storing maximum value so far

    # consider all the items in 0(N) and sump up the trapped rain water units
    trapped = 0

    for i in range(1, len(heights) - 1):
        if min(left_max[i], right_max[i]) > heights[i]:
            trapped += min(left_max[i], right_max[i]) - heights[i]

    return trapped

if __name__ == '__main__':
    # print(trapping_water_problem([1, 0, 2, 1, 3, 1, 2, 0, 3]))
    print(trapping_water_problem([1, 2, 3, 4]))