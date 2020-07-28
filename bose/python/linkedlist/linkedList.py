class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def get_data(self):
        return self.data

    def set_data(self,new_data):
        self.data = new_data
    
    def set_next(self,new_next):
        self.next = new_next

    def get_next(self):
        return self.next


class LinkedList:
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        size = 0
        while current!=None:
            size+=1
            current = current.get_next()
        return size

    def traverse(self):
        current = self.head
        while current!=None:
            print(current.get_data())
            current = current.get_next()

    def delete_value(self,value):
        if self.head.get_data() == value:
            self.head = self.head.get_next()
        else:
            current = self.head
            while current.get_next().get_data() !=value:
                current = current.get_next()
            tempNode = current.get_next()
            current.set_next(current.get_next().get_next())

    def reverseList(self,head):
        if head==None or head.get_next() ==None:
            return head
        rest = self.reverseList(head.get_next())
        head.get_next().set_next(head)
        head.set_next(None)
        return rest



    # temp = Node(89)
# print(temp.get_data())

ll = LinkedList()
# print(ll.head)

ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)
ll.add(6)
ll.add(7)
ll.add(8)

# print(ll.he

rest = ll.reverseList(ll.head)
ll.head = rest

print("Linked list after reversal")
ll.traverse()