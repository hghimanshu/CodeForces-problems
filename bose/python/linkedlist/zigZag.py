from LinkedList import LinkedList
from LinkedList import Node




def zigzag(head_node):
    # Complete this function
    if not head_node:
        return None
    slow = head_node
    fast = head_node.next 
    if not fast:
        return head_node
    count=1
    while fast and slow:
        if not fast:
            break
        if count%2!=0:
            if slow.data > fast.data:
                temp = slow.data
                slow.data = fast.data
                fast.data = temp
        else:
            if slow.data<fast.data:
                temp = slow.data
                slow.data = fast.data
                fast.data = temp
                
        slow,fast = slow.next, fast.next
        count+=1
    return head_node



if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.addEnd(2)
    ll1.addEnd(95)
    ll1.addEnd(30)
    ll1.addEnd(11)
    ll1.addEnd(48)
    head = ll1.getHeadNode()
    newHead = zigzag(head)
    print(ll1.traverseWithHead(newHead))