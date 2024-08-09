class Node:
    def __init__(self, data=None, prev=None, next=None) -> None:
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.end = None

    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data,None,None)
            self.end = self.head
            return 
        
        itr = self.end
        new_node = Node(data,itr,None)
        itr.next = new_node
        self.end = new_node

    def insert_values(self, data_list):
        for i in data_list:
            self.insert_at_end(i)

    def print_forward(self):
        itr = self.head
        dllstr = ''
        while itr:
            dllstr += itr.data + ' --> '
            itr = itr.next
        print(dllstr)

    def print_backward(self):
        itr = self.end
        dllstr = ''
        while itr:
            dllstr += itr.data + ' <-- '
            itr = itr.prev
        print(dllstr)

ll = DoublyLinkedList()
ll.insert_values(['4','5','6','7'])
ll.print_forward()
ll.print_backward()
