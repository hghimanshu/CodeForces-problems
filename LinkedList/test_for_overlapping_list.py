class LinkNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class Solution:
    
    def printList(self, L):
        while L:
            print(L.data)
            L = L.next
    def checkInnerLoop(self, node, L2):
        while L2:
            if node.data == L2.data:
                self.nodeFound = True
                break
            else:
                L2 = L2.next
        

    def checkIfNodePresentCycleFree(self, L1, L2):
        self.nodeFound = False
        while L1:
            self.checkInnerLoop(L1, L2)            
            if self.nodeFound:
                break
            else:
                L1 = L1.next
        
        if self.nodeFound:
            print("There is a node that is common to both list")
        else:
            print("No such common node")



## L1 --> 2 --> 5 --> 7
# L2 --> 3 --> 5 --> 7


list1 = LinkNode(2)
list1.next = LinkNode(5)
list1.next.next = LinkNode(7)

list2 = LinkNode(3)
list2.next = LinkNode(5)
list2.next.next = LinkNode(7)

ans = Solution()
ans.checkIfNodePresentCycleFree(list1, list2)