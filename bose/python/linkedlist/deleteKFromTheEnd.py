from LinkedList import LinkedList
from LinkedList import Node



def deleteKFromEnd(head,k):
    first = second = head
    while k:
        first = first.next
        k-=1
    while first.next and second.next:
        first,second = first.next, second.next
    

    second.next = second.next.next

    return head


if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.addEnd(5)
    ll1.addEnd(10)
    ll1.addEnd(15)
    ll1.addEnd(40)
    ll1.addEnd(12)
    ll1.addEnd(13)
    ll1.addEnd(14)
    ll1.addEnd(19)

    k=2
    head = ll1.getHeadNode()
    newHead = deleteKFromEnd(head,k)
    print(ll1.traverseWithHead(newHead))
