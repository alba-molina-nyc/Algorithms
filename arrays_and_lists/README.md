# Lists and Arrays

every single item is associated with an index.

- Main advantage of arrays is the random access of items based on idndex
- Static -> size does not change
- Dynamic -> size does change
  
---

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

---

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

---

## Numpy (the library used for handling arrays)

- The problem with `lists-python's built in ds` data structures is that list (built in data structures to python) stores references to the integer objects
  - stored in different memory locations
  - so storing a lot of items in lists has a huge memory complexity
- And `numpy arrays` are stored in a continuous block in the memory
  - AKA the items are next to each other
  
------_

[Interview Question 1](/array_list/01_reverse_in_place.py)

### Reverse Arrays in Place

Given an A array of integers - reverse this A array in linear running time using constant memory

```python
# EXPLANATION
array = [12, 6, 2, 1, 9, 10, 3]
         ⬆️                  ⬆️
         lowIndex            highIndex

# 1 store ref to first item and the last 
# 2 keep running the algorithm while the lowIndex < highIndex
# 3 keep swapping items
# 4 in every iteration increment the lowIndex (move up the list) and decrement highIndex (move down the list)

array = [3, 6, 2, 1, 9, 10, 12]
          # ⬆️            ⬆️
            # lowIndex    highIndex

array = [3, 10, 9, 1, 2, 6, 12]
            #   ⬆️    ⬆️
        # lowIndex    highIndex

array = [3, 10, 9, 1, 2, 6, 12]
                  #⬆️    
                  #⬆️
          #lowIndex  highIndex
# CRUCIAL : terminate the algorithm when lowIndex == highIndex 
```

[The code](/array_list/01_reverse_in_place.py)

---

### Palindrome Problem

[Interview question 2](/array_list/02_palindrome.py)

a palindrome is a string that reads the same forward and backward

- radar

- madam

EXPLANATION

```python
# -------------------------------------------------Understanding Under the Hood-----------------------------------------------------------------------------
def is_palindrome(s):
    original_string = s
    reversed_string = reverse(s) # this is what we have implemented in the previous lecture in O(n), so we pass in that function and make minor changes to fit for string case 

    if original_string == reversed_string: # check if the original string = reverse then return True else False
        return True 
    return False

def reverse(data):
    data = list(data) # 1. convert string into list of characters 
    # 1o- set pointers to first and last items
    start_index = 0 # point to first item ...
    end_index = len(data)-1 # point to last item ...  -1 bc index start at zero
    
    # 2o- while end > start 
    while end_index > start_index: 
        data[start_index], data[end_index] = data[end_index], data[start_index] # 3o swap two items in the list data structures 
        start_index = start_index + 1 # increment start index by 1
        end_index = end_index - 1 # decrement end index by 1

    return ''.join(data) # transforms list of letter into a string
```

- the solution uses the solution from [reverse in place solution](array_list/01_reverse_in_place.py) but refactored for string case

---

### Reverse integer (Integer Version)

[interview question 3](/array_list/03_reverse_integer.py)

- Given 1234 -> you want to end up with 4321
- bc it is an integer we have to use a different operator

```python
integer = 1234

# ➡️ we are after the last digit in every iteration 
#     ~ we can get this via modulo operator: the last digit is the remainer when dividing by 10

while (n < 0):
    remainder = n % 10
    n = n / 10 
    reversed = reversed * 10 + remainder

# ➡️ we have to make sure we remove that digit from the original number
#     ~ so we just have to divide the original number by 10

""" ⭐️ Iteration 1: 
remainder = 1234 / 10 = 4
n = 123
reversed = 0 * 10 + 4 = 4 

⭐️ Iteration 2: 
remainder = 123 / 10 = 3
n = 12
reversed = 4 * 10 + 3 = 43

⭐️ Iteration 3: 
remainder = 12 / 10 = 2
n = 1
reversed = 43 * 10 + 2 = 432 

⭐️ Iteration 4: 
remainder = 12 / 10 = 1
n = 0
reversed = 432 * 10 + 2 = 4321  """
```

[reverse integer solution](/array_list/03_reverse_integer.py)

---

### Anagrams

[Interview question 4](/array_list/04_anagram.py)

Construct an algorithm to check whether two words (or phrases) are anagrams or not

- an anagram is a word or a phrase formed by re-arranging the letters of a different word or phrase, typically using all the original letters exactly once
  - ex: restful ➡️ fluster

to check if it is an anagram:

1. if the words do not have the same amount of letters then it is not an anagram
2. sort the letters
3. then iterate through the strings and check whether the characters are matching or not by comparing on a one by one basis

```python
    # 1. if length of string differ -> not anagram -> return False
    if len(str1) != len(str2):
        return False

    # 2. sort the letters of the strings (this is the bottle neck)
    str1 = sorted(str1)
    str2 = sorted(str2)

    # 3. and then compare the letters with the same indexes 
    for i in range(len(str1)):
        print(str1[i], 'str1')
        print(str2[i], 'str2')
        if str1[i] != str2[i]:
            return False
    return True

```

---

### Dutch National Flag

[Interview question 5](/array_list/05_dutch_flag.py)

Given an A array of integers - 0,1 and 2 (3 diff values). Sort this A array in linear running time using constant memory

- constant memory -> not allowed to use additional data structures in order to store the items

```python

starting_container = [0, 1, 2, 1, 2, 0, 0] # you start with thi

[0, 0, 0, 1, 1, 2, 2] # the aim is to end up this
```

Explanation

because there are `three possible colors(values)`, so `use three indexes` i,j -> share the same value and k -> points to last value in the array

i ⬅️ 0
j ⬅️ 0
k ⬅️ size of array - 1 (last value in array)

(k is set to the index of the last item)
while j <= k: you have three options
if j < mid
if j > mid
else j = mid

the `middle` item or the `pivot` item is the integer 1, because we have three items 0, 1, 2 so 1 ➡️ is the middle or pivot number

```python
starting_container = [0, 1, 2, 1, 2, 0, 0]
                      ⬆️                ⬆️
                     i,j                k

# keep running the algorithm until while j <= k (so j essentially tracks the actual item)

# in every iteration we have to compate the j item with the pivot (middle) item which is 1 

[0, 1, 2, 1, 2, 0, 0]
 ⬆️                ⬆️
i,j                k
```

0 < `pivot item` (1)
so swap index i and j and then increment both indexes

```python
[0, 1, 2, 1, 2, 0, 0]
    ⬆️             ⬆️
    i,j            k
```

1 = `pivot item` (1)
so increment j by 1

```python
[0, 1, 2, 1, 2, 0, 0]
    ⬆️ ⬆️          ⬆️
    i  j           k
```

2 > `pivot item` (1)
so swap j with k
and decrement k by one
meaning the last item is in its sorted order

```python
[0, 1, 0, 1, 2, 0, 2]
    ⬆️ ⬆️       ⬆️
    i  j        k
```

0 < `pivot item` (1)
so swap j with i
and increment  indexes by 1

etc. etc.

[Dutch National Problem Implementation](/array_list/05_dutch_flag.py)