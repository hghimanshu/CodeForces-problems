from LinkedList import LinkedList
from LinkedList import Node

def reverseLinkedList(head):
    current = head
    prev = Node(None)
    prev.next = current
    while current:
        head = head.next
        current.next = prev
        prev = current
        current = head
    return prev

if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.addEnd(5)
    ll1.addEnd(10)
    ll1.addEnd(15)
    ll1.addEnd(40)
    ll1.addEnd(12)
    ll1.addEnd(13)

    reversedHead = reverseLinkedList(ll1.getHeadNode())
    ll1.traverseWithHead(reversedHead)


