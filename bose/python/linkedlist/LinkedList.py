class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def getNext(self):
        returnValue = self.next if self.next is not None else None
        return returnValue

    def getData(self):
        return self.data

    def setNext(self,next):
        self.next = next
    

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __len__(self):
        count = 0
        temp = self.head
        while temp:
            count+=1
            temp = temp.getNext()
        return count

    def addFront(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp
    
    def addEnd(self,value):
        if not self.head:
            self.head = Node(value)
        else:
            temp = self.head
            while temp.getNext():
                temp = temp.getNext()
            newNode = Node(value)
            temp.setNext(newNode)

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.getData())
            temp = temp.getNext()

    

if __name__ == "__main__":
    ll = LinkedList()
    ll.addEnd(1)
    ll.addEnd(2)
    ll.addEnd(3)
    ll.addEnd(4)
    ll.addEnd(5)
    ll.addEnd(6)
    print("Length of the linked list is::: ",len(ll))
    ll.traverse()
