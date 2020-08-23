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
