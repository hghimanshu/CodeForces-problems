from LinkedList import LinkedList

def mergeSortedLists(L1,L2):
    temp1 = L1.getHeadNode()
    temp2 = L2.getHeadNode()
    while temp1 and temp2:
        print("Current list is::: ")
        # L2.traverse()
        if temp1.getData() < temp2.getData():
            tempNext = temp1.getNext()
            temp1.setNext(temp2)
            temp1 = tempNext
            if temp2.getNext() and temp1:
                if temp2.getNext().getData() < temp1.data:
                    temp2 = temp2.getNext()
        else:
            tempNext = temp2.getNext()
            temp2.setNext(temp1)
            temp2 = tempNext
            if temp1.getNext() and temp2:
                if temp1.getNext().getData() < temp2.data:
                        temp1 = temp1.getNext()
            
        
    

if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.addEnd(1)
    ll1.addEnd(5)
    ll1.addEnd(7)
    ll1.addEnd(8)
    ll1.addEnd(12)
    ll1.addEnd(13)

    ll2 = LinkedList()
    ll2.addEnd(2)
    ll2.addEnd(3)
    ll2.addEnd(6)
    ll2.addEnd(11)
    ll2.addEnd(14)
    ll2.addEnd(17)

    ll1.traverse()
    print("\n")
    ll2.traverse()

    mergeSortedLists(ll1,ll2)
    print("\n")
    ll1.traverse()

    # print("\n")
    # ll2.traverse()