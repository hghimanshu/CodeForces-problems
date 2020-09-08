from LinkedList import LinkedList

def sortedMerge(head_A,head_B):
    temp1 = head_A
    temp2 = head_B
    while temp1 and temp2:
        if temp1.data < temp2.data:
            #do something
            if temp1.next:
                if temp1.next.data > temp2.data:
                    #swap and connect
                    tempNext = temp1.next
                    temp1.next = temp2
                    temp1 = tempNext
                else:
                    temp1 = temp1.next
            else:
                tempNext = temp1.next
                temp1.next = temp2
                temp1 = tempNext



        elif temp2.data < temp1.data:
            if temp2.next:
                if temp2.next.data > temp1.data:
                    #swap and connect
                    tempNext = temp2.next
                    temp2.next = temp1
                    temp2 = tempNext
                else:
                    temp2 = temp2.next

            else:
                #swap and connect
                tempNext = temp2.next
                temp2.next = temp1
                temp2 = tempNext
    if head_A.data < head_B.data:
        return head_A
    else:
        return head_B

        
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
    # ll1.traverseWithHead(returnedHead)
    ll2.traverse()

    # print("\n")
    # ll2.traverse()