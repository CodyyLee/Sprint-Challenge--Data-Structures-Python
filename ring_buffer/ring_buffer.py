from doubly_linked_list import DoublyLinkedList, ListNode

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = DoublyLinkedList()
        self.curr = None

    def append(self, item):
        if not self.items.head:
            #emtpy ring
            self.items.add_to_head(item)
            self.curr = self.items.head
        elif self.items.length < self.capacity:
            #ring less than max
            self.items.add_to_tail(item)
        else:
            #ring at max
            if self.curr == self.items.tail:
                self.items.remove_from_tail()
                self.items.add_to_tail(item)
                self.curr = self.items.head
            elif self.curr == self.items.head:
                old_next = self.items.head.next
                self.items.remove_from_head()
                self.items.add_to_head(item)
                self.curr = old_next
            else:
                new_node = ListNode(item)

                new_prev = self.curr.prev
                new_next = self.curr.next
                new_node.next = new_next
                new_node.prev = new_prev
                new_node.prev.next = new_node
                new_node.next.prev = new_node
                self.curr = new_next



    def get(self):
        myList = []
        node = self.items.head
        
        while node:
            myList.append(node.value)
            node = node.next

        return myList
