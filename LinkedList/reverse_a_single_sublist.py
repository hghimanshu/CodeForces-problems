class LinkNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next



class Solution:
    def printList(self, L):
        while L:
            print(L.data)
            L = L.next

    def reversingSublist(self, L, s, f):
        dummy_head = sublist_head = LinkNode(0, L)
        for _ in range(1, s):
            sublist_head = sublist_head.next
        
        ##Reverse sublist
        sublist_iter = sublist_head.next
        for _ in range(f -s):
            temp = sublist_iter.next
            sublist_iter.next, temp.next, sublist_head.next = (temp.next, sublist_head.next, temp)
        return dummy_head.next
    

    # def reverseFullList(self, L):
    #     self.findTailOfList(L)
    #     first, tail = 

    
    # def findTailOfList(self, L):
    #     self.head = None
    #     while L:
    #         if L.next:
    #             self.head = L.next
    #         L = L.next    


## Li --> 2 --> 6 --> 9 --> 4
## s --> 2, f --> 4
# 
# output --> 2 --> 4 --> 9 --> 6 


list1 = LinkNode(2)
list1.next = LinkNode(6)
list1.next.next = LinkNode(9)
list1.next.next.next = LinkNode(4)

s = 2
f = 4


ans = Solution()
# L = ans.reversingSublist(list1, s, f)
# ans.printList(L)

# L = ans.reverseFullList(list1)
# ans.printList(L)