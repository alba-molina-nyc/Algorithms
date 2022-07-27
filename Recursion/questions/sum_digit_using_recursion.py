"""
Find the sum of digits of a positive integer number using recursion
ex1: given 10, separate the digits 1 and 0 then add them 1 + 0 
ex2: given 112, separate the digits 11 and remainder 1, 1 1 2

1. Find the recursive case
2. Find the Stopping Case
3. Keep it under control
"""

"""
def recursion(parameters):
    # potentially may need a while condition here
    if exit from condition satisfied:
        return some value
    else: 
        recursionMethod(modified parameters)

recursion(paramenters=)
"""



def SumofDigits(n):
    if n == 0: # base condition
        return 0
    else:
        print(int(n%10))
        print(SumofDigits(int(n//10)))
        return int(n%10) + SumofDigits(int(n//10)) #recursionMethod(modified parameters)
print(SumofDigits(n=1132))



# print(SumofDigits(n=10))
# SumofDigits(n=1122)
