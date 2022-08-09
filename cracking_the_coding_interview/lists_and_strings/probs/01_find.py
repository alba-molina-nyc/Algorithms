"""
find the zeros in a number array
"""

def findZero(list):
    print(list)

    for i in list: 
        if i == 0:
            print(i)
# findZero(list=[1,2,3,0,1,2,3,0,0,5,6,0,0])

"""
use [i] for index """
def findZero(list):
    # print(list)
    indices = []
    
    for i in range(len(list)):
        if list[i] == 0:
            indices.append(i)
    print(indices, 'indices')
   
    
    
    # insert beginning
       
     

    # insert middle

    # insert end 
        

      
findZero(list=[1,2,3,0,1,2,3,0,0,5,6,0,0])