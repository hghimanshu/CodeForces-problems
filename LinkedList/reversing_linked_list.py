class LinkNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next



class Solution:
    def __init__(self):
        self.head = None


    def printList(self, L):
        while L:
            print(L.data)
            L = L.next
    
    def push(self, x):
        data = LinkNode(x)
        data.next = self.head
        self.head = data
        return data
    
    def reverse(self):
        prev, current = None, self.head
        while current is not None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev
        return self.head

            



## Li --> 2 --> 6 --> 9 --> 4
# output --> 4 --> 9 --> 6 --> 2
# 2.next =None
# 4.next ==> 9.next ==> 6.next ==> 2.next ==> None
# ^
# |
# self.head


ans = Solution()
list1 = ans.push(2)
list1 = ans.push(6)
list1 = ans.push(9)
list1 = ans.push(4)

print("Original List :: ")
ans.printList(list1)

print("\n\n Reversed List :: ")
list1 = ans.reverse()
ans.printList(list1)