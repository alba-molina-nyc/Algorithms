# -------------------------------------------------Creating Array-----------------------------------------------------------------------------
array = [10, 3, 7, 5]

# -------------------------------------------------Indexing an Array-----------------------------------------------------------------------------

array[0] # first index 

# -------------------------------------------------Get ALL items in Array-----------------------------------------------------------------------------

array = [10, 3, 7, 5]
array[:] # to get all the items in an array

# -------------------------------------------------Get certain items in array-----------------------------------------------------------------------------


array = [10, 3, 7, 5]
array[0:2] # to get all the items starting with index 0 and up to index 2 to get first three items

# -------------------------------------------------Negative Indexing in Arrays (starting from end of array)-----------------------------------------------------------------------------

array = [10, 3, 7, 5]
array[0:-2] # gets everything except for last two 

# -------------------------------------------------Updating an Array-----------------------------------------------------------------------------


array = [10, 42, 'Adam', 2, 1]
array[2] = 'Kevin' # to update Adam to Kevin 

# -------------------------------------------------MAX Linear Search-----------------------------------------------------------------------------
array1 = [10, 42, 55, 2, 1, 0]
max = array1[0] # 1 define maximum - suppose it is first item of array 

for i in array1:  # 2 iterate through and define a given varibale in the array 
    if i > max:
        max = i
print(f'{max}, this is the max number')

# -------------------------------------------------MIN Linear Search-----------------------------------------------------------------------------
array2 = [10, 42, 55, 2, 1, 0]

min = array2[0] # 1 define minimum - suppose it is first item of array 

for i in array2:  # 2 iterate through and define a given varibale in the array 
    if i < max:   # 3 if the number less than max 
        min = i   # 4 then we update them
print(f'{min}, this is the min number')
