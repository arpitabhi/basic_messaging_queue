
class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None  
class LinkedList: 
    def __init__(self):
        self.head = None

    def last_node(self):
        hd = self.head
        if hd is not None:
            nxt = hd.next
            while True:
                if nxt is None:
                    return hd
                else:
                    hd = hd.next
                    nxt = hd.next

