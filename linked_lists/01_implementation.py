class Node: 

    def __init__(self, data):
        self.data = data 
        self.next_node = None # reference to next node


class LinkedList:

    def __init__(self):
        self.head = None # this is the first node of the LL, we have access to this node exclusively

