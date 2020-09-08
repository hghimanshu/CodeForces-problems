from LinkedList import LinkedList
from LinkedList import Node

def reverseLinkedList(node):
    if node ==None or node.getNext()==None:
        return node

    new_node = reverseLinkedList(node.next)
    node.getNext().setNext(node)
    node.setNext(None)
    return new_node



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


