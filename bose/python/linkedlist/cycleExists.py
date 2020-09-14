from LinkedList import LinkedList
from LinkedList import Node


def getCycle(head):

    def cyclePresent(head):
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return getStartOfCycle(slow,fast,head)
        return None
    
    return cyclePresent(head)


def getStartOfCycle(slow,fast,head):
    slow = head
    while slow and fast:
        slow , fast = slow.next , fast.next
        if slow is fast:
            return slow.data


def createCycle(index,head):
    temp = head
    tail = head
    step = 1
    while temp:
        temp= temp.next
        step+=1
        if step==index:
            break
    
    while tail.next:
        tail=tail.next
    
    tail.next = temp
    return head


if __name__ == "__main__":
    ll1 = LinkedList()
    ll1.addEnd(1)
    ll1.addEnd(2)
    ll1.addEnd(3)
    ll1.addEnd(4)
    ll1.addEnd(5)
    ll1.addEnd(6)
    ll1.addEnd(7)

    headNode = ll1.getHeadNode()
    newHead = createCycle(4,headNode)
    print(getCycle(newHead))

    
