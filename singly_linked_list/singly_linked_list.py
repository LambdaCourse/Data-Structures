class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


    def iter(self):
        current = self.tail
        while current:
            val = current.value
            current = current.next
            yield val

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

    def contains(self, value):
        for node in self.iter():
            if value == node:
                return True
        return False

    def remove_head(self):
        if self.head is None:
            return None
        if self.head == self.tail:
            
            current = self.head
            self.head = None
            self.tail = None
            self.size -= 1
            return current.value
        else:
            current = self.head
            self.head = current.next
            self.size -= 1
            return current.value
                
        

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
        
