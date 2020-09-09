from LinkedList import LinkedList
from LinkedList import Node

def cyclic_right_shift(head,k):
    if not head:
        return None
    tail = head
    n=1
    while tail.getNext():
        n+=1
        tail = tail.getNext()

    tail.setNext(head)
    k = k%n ##If K is a large number than k%n will essentially be the same number of cyclic repetitions
    steps_to_new = n-k
    new_tail = tail
    while steps_to_new:
        new_tail = new_tail.getNext()
        steps_to_new-=1
    
    new_head = new_tail.next
    new_tail.setNext(None)
    return new_head
 


if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.addEnd(5)
    ll1.addEnd(10)
    ll1.addEnd(15)
    ll1.addEnd(40)
    ll1.addEnd(12)
    k=3
    head = cyclic_right_shift(ll1.getHeadNode(),k)
    if head:
        ll1.traverseWithHead(head)
