from LinkedList import LinkedList
from LinkedList import Node

def sortedMerge(head_A,head_B):
    temp1 = head_A
    temp2 = head_B
    dummyHead = tail = Node()

    while temp1 and temp2:
        if temp1.data < temp2.data:
            tail.next = temp1
            temp1 = temp1.next
        else:
            tail.next = temp2
            temp2 = temp2.next
        tail = tail.next

    tail.next = temp1 or temp2
    return dummyHead.next

        
if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.addEnd(5)
    ll1.addEnd(10)
    ll1.addEnd(15)
    ll1.addEnd(40)
    # ll1.addEnd(12)
    # ll1.addEnd(13)

    ll2 = LinkedList()
    ll2.addEnd(2)
    ll2.addEnd(3)
    ll2.addEnd(20)
    # ll2.addEnd(11)
    # ll2.addEnd(14)
    # ll2.addEnd(17)

    ll1.traverse()
    print("\n")
    ll2.traverse()

    returnedHead=sortedMerge(ll1.getHeadNode(),ll2.getHeadNode())
    print("\n")
    ll1.traverseWithHead(returnedHead)
    # ll2.traverse()

    # print("\n")
    # ll2.traverse()