from LinkedList import LinkedList
from LinkedList import Node

def removeDuplicates(head):
    curr = head
    next_node = curr.getNext()
    while next_node:
        if next_node.getData()!=curr.getData():
            next_node = next_node.getNext()
            curr = curr.getNext()
        else:
            curr.setNext(next_node.getNext())
            next_node = curr.getNext()

    return head




if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.addEnd(2)
    ll1.addEnd(2)
    ll1.addEnd(3)
    ll1.addEnd(3)
    ll1.addEnd(11)
    ll1.addEnd(11)
    ll1.addEnd(14)
    head = removeDuplicates(ll1.getHeadNode())
    if head:
        ll1.traverseWithHead(head)