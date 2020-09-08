from LinkedList import LinkedList
from LinkedList import Node


def reverseSubList(head,start,finish):
    sublistHead= head
    prev = Node(None)
    prev.next = sublistHead
    for _ in range(1,start):
        sublistHead = sublistHead.next
        prev = prev.next
    
    sublistHead = sublistHead.next
    prev1 = prev
    prev = prev.next
    current = sublistHead
    prev.next = current
    for _ in range(finish-start):
        sublistHead = sublistHead.next
        current.next = prev
        prev = current
        current = sublistHead
    
    temp = prev1.next
    temp.next = sublistHead
    prev1.next = prev
    return head


# def reverseLinkedList(head):
#     current = head
#     prev = Node(None)
#     prev.next = current
#     while current:
#         head = head.next
#         current.next = prev
#         prev = current
#         current = head
#     return prev

if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.addEnd(5)
    ll1.addEnd(10)
    ll1.addEnd(15)
    ll1.addEnd(40)
    ll1.addEnd(12)
    ll1.addEnd(13)
    ll1.addEnd(50)

    reversedHead = reverseSubList(ll1.getHeadNode(),2,5)
    ll1.traverseWithHead(reversedHead)


