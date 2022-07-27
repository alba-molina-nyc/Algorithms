"""
Recursion - a function that calls itself and in turn, it makes the problem smaller and smaller because it performs the SAME task with DIFF inputs(based on the previous task)
(can also be solved by iterations)

You need a BASE CONDITION in order to stop and avoid the infinite loop
- either you found your answer OR the answer does not exist

IF you can divide the problem into smaller sub problems then use recursion
TREES and GRAPHS use a lot of recursion but you can use them in other data structures too

IT is used in many algorithms(divide and conquer, greedy, and dynamic programming)
so without knowledge of recursion, the above topics are very difficult to learn
"""

from multiprocessing.sharedctypes import Value


def openRussianDoll(doll):
    if doll == 1:
        print('All dolls are opened') #good palce for breakpoint
    else: 
        print(openRussianDoll(doll-1), 'else statement') # good place for a breakpoint

openRussianDoll(doll=10)


"""
HOW recursion works --> 2 conditions
1. method calls itself
2. exit from inifite loop
"""

"""
def recursionMethod(parameters):
    if exit from condition satisfied:
        return some value
    else:
        recursionMethod(modified parameters)
"""