from LinkedList import LinkedList
from LinkedList import Node


def reverse_linked_list(node):
    if node is None or node.getNext() is None:
        return node
    new_node = reverse_linked_list(node.getNext())
    node.getNext().setNext(node)
    node.setNext(None)
    return new_node

def getMid(node):
    slow = fast = node
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

def is_palindrome(head):
    second_half = getMid(head)
    reverse_linked_list_head = reverse_linked_list(second_half)
    temp1 = head
    temp2 = reverse_linked_list_head
    while temp1 and temp2:
        if temp1.data !=temp2.data:
            return False
        temp1, temp2 = temp1.getNext(), temp2.getNext()
    return True

if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.addEnd(1)
    ll1.addEnd(2)
    ll1.addEnd(2)
    ll1.addEnd(4)
    ll1.addEnd(3)
    ll1.addEnd(2)
    ll1.addEnd(1)
    # test_reverse_head = reverse_linked_list(ll1.getHeadNode())
    # if test_reverse_head:
    #     ll1.traverseWithHead(test_reverse_head)
    
    if is_palindrome(ll1.getHeadNode()):
        print("Is a palindrome")
    else:
        print("Not a palindrome")
