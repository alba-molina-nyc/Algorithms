"""
Convert a num from decimal to binary using recursion

STEP
1 divide num by 2
2 get integer quotient for next iteration
3 get remainder for bin digit
4 repeat steps until quotient is 0 
ex: 13 to bin num
13/2 
quotient 6 remainder 1 (keep doing until remainder is 0)
quotient 3 remainer 0
quotient 1 remainder 1
quotient 0 remainder 1

the binary number is ging to be the quotients aka 1101
"""



"""
def recursionMethod(parameters):
    if statement:                                 if the condition is satisfied exit code
        return something
    else:
        return recursionMethod(parameters modified)                    do the recursive portion

recursionMethod(parameters=)
"""

def decimalToBinary(n):
    if n == 0:
        return 0
    else:
        return n%2 + 10 * decimalToBinary(n//2)

# print(decimalToBinary(10))
print(decimalToBinary(13))