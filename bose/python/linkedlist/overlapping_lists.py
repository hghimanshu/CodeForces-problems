from LinkedList import LinkedList
from LinkedList import Node



def checkifOverlapExists(head1,head2):

    def getLength(node):
        step = 0
        while node:
            step+=1
            node = node.next
        return step
    
    l1 = getLength(head1)
    l2 = getLength(head2)

    if l1 > l2:
        temp1 = head1
        temp2 = head2
    else:
        temp1 = head2
        temp2 = head1

    diff = abs(l1-l2)

    for _ in range(diff):
        temp1 =temp1.next
    
    while temp1 and temp2 and temp1 is not temp2:
        temp1,temp2 = temp1.next, temp2.next
    
    return temp2

def createOverlap(head1,head2,index):
    temp1 = head1
    while index:
        temp1 = temp1.next
        index-=1
    temp2 = head2
    while temp2.next:
        temp2 = temp2.next
    temp2.next = temp1
    return head1


if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.addEnd(1)
    ll1.addEnd(2)
    ll1.addEnd(3)
    ll1.addEnd(4)
    ll1.addEnd(5)
    ll1.addEnd(6)
    ll1.addEnd(7)
    ll1.addEnd(8)

    head1 = ll1.getHeadNode()

    ll2 = LinkedList()
    ll2.addEnd(10)
    ll2.addEnd(11)
    ll2.addEnd(12)

    head2 = ll2.getHeadNode()

    head1 = createOverlap(head1,head2,4)
    if(checkifOverlapExists(head1,head2)):
        print("Overlap exists")

    