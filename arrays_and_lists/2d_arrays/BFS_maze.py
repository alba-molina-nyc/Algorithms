"""
Interview question #2 - using BFS to find way out of maze
We have considered BFS and DFS graph traversal algorithms in the previous lectures. You task is to design an algorithms
with breadth-first search that is able to find the shortestpath from a given source to a given destination. 
The maze is represented by a two-dimensional list.

[
   [S, 1, 1, 1, 1],
   [0, 1, 1, 1, 1],
   [0, 0, 0, 0, 1],
   [1, 0, 1, 1, 1],
   [0, 0, 0, 1, D]
]
The (0,0) is the source and (4,4) is the destination. 0 represents walls or obstacles and 1 is the valid cells we can 
include in the solution.

Good luck!"""
# Using BFS
from tracemalloc import start


def shortestPath(maze):
    # 0 -> obstacles, 1 -> valid
    print(maze)

    
   #  0,0 = start
   #  4,4 = end

    pass

shortestPath([
   ['S', 1, 1, 1,  1],
   [0  , 1, 1, 1,  1],
   [0  , 0, 0, 0,  1],
   [1  , 0, 1, 1,  1],
   [0  , 0, 0, 1, 'D']
])

# answer 10? can go ^ V, < >