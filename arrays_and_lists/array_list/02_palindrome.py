""" design an optimal algorithm for checking whether a given string is a palindrome or not"""
# -------------------------------------------------Pythonic Way----------------------------------------------------------------------------
def palindrome_python(s):
    if s == s[::-1]: # string slicing, strings are array of character
        return True
    
    return False
# palindrome_python(s='madam')


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

if __name__ == '__main__':
    # print(palindrome_python('madam'))
    # print(palindrome_python('car'))
    print(is_palindrome('madam'))
    print(is_palindrome('car'))

