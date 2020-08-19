class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def __str__(self):
        return str(value)
    
    def add_to_tail(self, value):
        if self.tail is None:
            new_tail = Node(value, None)
            self.head = new_tail
            self.tail = new_tail
        else:
            new_tail = Node(value, None)
            old_tail = self.tail
            old_tail.next = new_tail
            
            self.tail = new_tail
        self.size += 1
        
        
