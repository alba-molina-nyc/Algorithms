"""Write an efficient algorithm that reverses a given integer --- EX:  if input of algo is 1234 then output is 4321"""

def reverse_integer(n):
    reversed_integer = 0
    remainder = 0 

    while n > 0:
        remainder = n % 10
        reversed_integer = reversed_integer * 10 + remainder
        n = n // 10
        print(reversed_integer, 'this is the reversed inside the while')


    print(reversed_integer, 'this is the reversed')

    return reversed_integer


if __name__ == '__main__': 
    print(reverse_integer(1234))
    print(reverse_integer(5678))

