"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        if self.length == 0:
            new_head = ListNode(value)
            self.head = new_head
            self.tail = new_head
            self.length = self.length + 1
        else:
            old_head = self.head
            self.head = ListNode(value)
            self.head.next = old_head
            old_head.prev = self.head
            self.length = self.length + 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        old_head = self.head

        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return old_head.value
        else:
            self.head = self.head.next
            self.head.prev = None
            self.length = self.length - 1
            return old_head.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        if self.length == 0:
            new_node = ListNode(value)
            self.head = new_node
            self.tail = new_node
            self.length = 1
        else:
            old_tail = self.tail
            self.tail = ListNode(value)
            old_tail.next = self.tail
            self.tail.prev = old_tail
            self.length = self.length + 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        old_tail = self.tail

        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return old_tail.value
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            self.length = self.length - 1
            return old_tail.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.length == 0:
            return None
        elif self.length == 1:
            return
        else:
            old_head = self.head

            if node.next == None:
                current_prev = node.prev
                current_prev.next = None
                self.tail = current_prev
            else:
                current_prev = node.prev
                current_next = node.next

                current_prev.next = current_next
                current_next.prev = current_prev

            self.head = node
            self.head.prev = None
            self.head.next = old_head
            old_head.prev = self.head
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.length == 0:
            return None
        elif self.length == 1:
            return
        else:
            old_tail = self.tail

            if node.prev == None:
                self.head = self.head.next
                self.head.prev = None
                self.tail = node
                self.tail.next = None
                self.tail.prev = old_tail
            else:
                current_prev = node.prev
                current_next = node.next

                current_prev.next = current_next
                current_next.prev = current_prev

            self.tail = node
            self.tail.prev = old_tail
            self.tail.next = None
            old_tail.next = self.tail

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            if node.prev == None:
                self.head = self.head.next
                self.head.prev = None
            elif node.next == None:
                self.tail.prev = self.tail
                self.tail.next = None
            else:
                current_next = node.next
                current_prev = node.prev
                current_prev.next = current_next
                current_next.prev = current_prev

            self.length = self.length - 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.length == 0:
            return None
        elif self.length == 1:
            return self.head.value
        else:
            myMax = self.head.value
            current = self.head.next

            while current:
                if current.value > myMax:
                    myMax = current.value
                current = current.next
            return myMax