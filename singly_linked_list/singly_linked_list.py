class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    
        
class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.size = 0


    def __str__(self):
        return str(value)

    def add_to_head(self, value):
        new_node = Node(value)

        #check if empty list
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # new node should point to current head
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            
    
    def add_to_tail(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1
            

    def contains(self, value):
       pass

    def remove_head(self):
        if self.head is None:
            return None
        
        if self.head == self.tail:
            current_head = self.head
            self.head = None
            self.tail = None
            self.size += 1
            return current_head.value

    def remove_tail(self):
        if self.tail is None:
            return
        if self.head == self.tail:
            current_tail = self.tail
            self.tail = None
            self.head = None
            self.size -= 1
            return current_tail.value
                
        

    def get_max(self):
        if self.size == 0:
            return None
        if self.size == 1:
            return self.head.value
        current_max = self.head.value
        current_node = self.head
        while current_node is not None:
            if current_max < current_node.value:
                current_max = current_node.value

            current_node = current_node.next
        return current_max
        
