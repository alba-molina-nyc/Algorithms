class Node: 

    def __init__(self, data):
        self.data = data 
        self.next_node = None # reference to next node


class LinkedList:

    def __init__(self):
        self.head = None # this is the first node of the LL, we have access to this node exclusively
        self.num_of_nodes = 0 

    #insert data to beginning of LL
    def insert_start(self, data):
        self.num_of_nodes  =+ 1     #increment number of nodes by 1
        new_node = Node(data)         #instantiate new node with data

        # if head is null aka the list is empty, then this will be the first node
        if self.head is None:
            self.head = new_node
        # when ll is not empty
        else:
            new_node.next_node = self.head # have to update teh references, new_node pointing to previous first_node
            self.head = new_node #now the new node is the head 

#TODO: come back
    def insert_end(self, data):
        self.num_of_nodes =+ 1
        new_node = Node(data)

        # if head is null aka the list is empty, then this will be the first node and the last node
        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

            



    
    def size_of_list(self):
        return self.num_of_nodes

