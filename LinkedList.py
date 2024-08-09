class Node:
    def __init__(self, data=None, next=None) -> (None): #intialising a node
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next 
        return count
    
    def insert_values(self, data_list): #create a LL from a list
        for i in data_list:
            self.insert_at_end(i)
    
    def insert_at_beg(self, data): #insert data at beginning of LL
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data): #insert data at end of LL
        if self.head == None:
            self.head = Node(data, None)
            return 
        
        itr = self.head
        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)

    def insert_at(self, index, data): #insert element at given index
        if index<0 or index>=self.get_length():
            raise Exception("invalid index")
        
        if index==0:
            self.insert_at_beg(data)
            return 
        
        count = 0 
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = Node(data,itr.next)
                break
            count += 1
            itr = itr.next 

    def insert_after_value(self, data_after, data): #insert data after given data
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data, itr.next)
                break
            itr = itr.next 

    def remove_at(self, index): #remove element at given index 
        if index<0 or index>=self.get_length():
            raise Exception("invalid index")
        
        if index==0:
            self.head = self.head.next
            return 
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break 
            itr = itr.next 
            count += 1
            
    def remove_by_value(self, value): #remove node by value 
        itr = self.head
        while itr.next:
            if itr.next.data == value:
                itr.next = itr.next.next
                break
            itr = itr.next 

    def print(self): #print the LL 
        if self.head is None:
            print("Linked list is empty")
            return 
        
        llstr = ""
        itr = self.head
        while itr:
            llstr += str(itr.data) + " --> "
            itr = itr.next
        print(llstr)

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beg(5)
    ll.insert_at_beg(6)
    ll.insert_at_end(76)
    ll.print()
    ll2 = LinkedList()
    ll2.insert_values(['mango', 'apple', 'orange'])
    ll2.print()
    ll2.remove_by_value('apple')
    ll2.print()
    ll2.insert_at(1,'papaya')
    ll2.print()
    ll2.insert_after_value('papaya','fig')
    ll2.print()
    print(ll2.get_length())