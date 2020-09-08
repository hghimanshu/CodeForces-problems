from LinkedList import LinkedList
from LinkedList import Node


def reverseLinkedList(node,finish):
    if node ==None or node.getNext()==None or node.getData() == finish:
        return node

    new_node = reverseLinkedList(node.next,finish)
    lastNode = node.getNext().getNext()
    node.getNext().setNext(node)
    node.setNext(lastNode)
    return new_node


def reverseSubList(head,start,finish):
    if not head:
        return None
    
    if head.getData()!=start:
        temp=head
        while temp.getNext().getData()!=start:
            temp = temp.getNext()
    else:
        temp = Node(None)
        temp.setNext(head)
    
    temp.setNext(reverseLinkedList(temp.getNext(),finish))

    if not temp.getData():
        return temp.getNext()
    return head
    

if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.addEnd(5)
    ll1.addEnd(10)
    ll1.addEnd(15)
    ll1.addEnd(40)
    ll1.addEnd(12)
    ll1.addEnd(13)
    ll1.addEnd(50)

    reversedHead = reverseSubList(ll1.getHeadNode(),15,12)
    ll1.traverseWithHead(reversedHead)


