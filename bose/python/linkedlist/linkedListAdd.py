from LinkedList import LinkedList
from LinkedList import Node


def addLinkedList(head1,head2):
    sum=0
    i=0
    carry=0
    while head1 or head2 or carry:
        multiplier = pow(10,i)
        print("Multiplier is:: ",multiplier)
        print("Head1 data::: ",head1.getData() if head1 else 0)
        print("Head2 data::: ",head2.getData() if head2 else 0)
        print("Carry is::",carry)
        val = carry+ (head1.getData() if head1 else 0) + (head2.getData() if head2 else 0)
        digit = val%10

        sum+= multiplier*digit
        carry = val//10
        print("Sum is::: ",sum)
        print("\n")
        i+=1
        head1 = head1.getNext() if head1 else None
        head2 = head2.getNext() if head2 else None
    
    return sum


if __name__ == "__main__":
    l1 = LinkedList()
    l1.addFront(1)
    l1.addFront(2)
    l1.addFront(3)
    
    l2 = LinkedList()
    # l2.addFront(9)
    l2.addFront(9) 
    l2.addFront(9)
    l2.addFront(5)

    print(addLinkedList(l1.getHeadNode(),l2.getHeadNode()))