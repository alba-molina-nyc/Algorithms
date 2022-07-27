"""
Recursion - a function that calls itself and in turn, it makes the problem smaller and smaller because it performs the SAME task with DIFF inputs(based on the previous task)
(can also be solved by iterations)

You need a BASE CONDITION in order to stop and avoid the infinite loop
- either you found your answer OR the answer does not exist
"""

def openRussianDoll(doll):
    if doll == 1:
        print('All dolls are opened') #good palce for breakpoint
    else: 
        print(openRussianDoll(doll-1), 'else statement') # good place for a breakpoint

openRussianDoll(doll=10)
