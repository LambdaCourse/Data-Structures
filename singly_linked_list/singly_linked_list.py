class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

<<<<<<< HEAD
=======
    
        
>>>>>>> 0848068365771d4c113482e906b533f334b9a115
class LinkedList:
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.size = 0

<<<<<<< HEAD
    def __str__(self):
        return str(value)

    def remove_tail(self):
        if self.tail is None:
            return None
        if seld.head == self.tail:
            current_tail = self.tail

            self.tail = None
            self.head = None
            self.size = self.size - 1
            return current_tail.value
        else:
            curent_node = self.head
            while current_node.next != self.tail:
                current_node = current_node.next

            current_tail = self.new_tail
            self.tail = current_node
            current_node.next = None
            self.size = self.size - 1
            return current_tail.value


=======

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
            
    
>>>>>>> 0848068365771d4c113482e906b533f334b9a115
    def add_to_tail(self, value):
        new_node = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
<<<<<<< HEAD
            new_tail = Node(value, None)
            old_tail = self.tail
            old_tail.next = new_tail

            self.tail = new_tail
        self.size += 1

    def add_to_head(self, value):
        # if not head
        if self.head is None:
            head_node = Node(value, None)
            self.head = head_node
            self.tail = head_node
            self.size = self.size + 1

        else:
            head_node = Node(value, self.head)
            self.size = self.size + 1
=======
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
        
>>>>>>> 0848068365771d4c113482e906b533f334b9a115
