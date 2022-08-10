# Lists and Arrays

every single item is associated with an index.

- Main advantage of arrays is the random access of items based on idndex
- Static -> size does not change
- Dynamic -> size does change

## Operations

1. Search

2. Add

3. Remove

```python
# -------------------------------------------------Creating Array------------------------------------------------------
array = [10, 3, 7, 5]
```

### Random Indexing

- you are able to access a given item based on the index of the item

- indexes start with 0
  
```python
#-------------------------------------------------Indexing an Array--------------------------------------------------------
array = [10, 3, 7, 5]

array[0] # first index 
```

SLICE OPERATOR - Fetch `all` items in one dimmesional array

```python
#-------------------------------------------------Fetch all items in Array --------------------------------------------------------

array = [10, 3, 7, 5]
array[:] # to get all the items in an array
```

SLICE OPERATOR - Fetch `first three items` in the array, starting index 0

```python
# -------------------------------------------------Get certain items in array------------------------------------------------------

array = [10, 3, 7, 5]
array[0:2] # to get all the items starting with index 0 and up to index 2 to get first three items
```

SLICE OPERATOR - `negative indexing`

```python
# -------------------------------------------------Negative Indexing in Arrays (starting from end of array)-----------------------------------------------------------------------------

array = [10, 3, 7, 5]
array[0:-2] # gets everything except for last two 
```

### Update

```python
# -------------------------------------------------Updating an Array---------------------------------------------------------

array = [10, 42, 'Adam', 2, 1]
array[2] = 'Kevin' # to update Adam to Kevin 
```

### Linear Search o(n)

- iterate through items one by one to find max

```python
# -------------------------------------------------MAX Linear Search-------------------------------------------------------
array1 = [10, 42, 55, 2, 1, 0]
max = array1[0] # 1 define maximum - suppose it is first item of array 

for i in array1:  # 2 iterate through and define a given varibale in the array 
    if i > max:
        max = i
print(f'{max}, this is the max number')
```

- iterate through items one by one to find min
  
```python
# -------------------------------------------------MIN Linear Search---------------------------------------------------------------
array2 = [10, 42, 55, 2, 1, 0]

min = array2[0] # 1 define minimum - suppose it is first item of array 

for i in array2:  # 2 iterate through and define a given varibale in the array 
    if i < max:   # 3 if the number less than max 
        min = i   # 4 then we update them
print(f'{min}, this is the min number')
```

```python
```