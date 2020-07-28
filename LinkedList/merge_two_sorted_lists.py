class LinkNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next



class Solution:
    def insertAtaNode(self, node, new_node):
        remain_list = new_node.next
        new_node.next = node.next
        node.next = new_node

        return node, remain_list


    def mergingList(self, L1, L2):
        if L1.next and L2:
            if L1.next.data > L2.data:
                L1, L2 = self.insertAtaNode(L1, L2)
            self.mergingList(L1.next, L2)
        
        else:
            if L2.data:
                L1, L2 = self.insertAtaNode(L1, L2)
        return L1

    def printList(self, L):
        while L:
            print(L.data)
            L = L.next




## L1 --> 2 --> 5 --> 7
# L2 --> 3 --> 11 

## output --> 2 --> 3 --> 5 --> 7 --> 11

list1 = LinkNode(2)
list1.next = LinkNode(5)
list1.next.next = LinkNode(7)

list2 = LinkNode(3)
list2.next = LinkNode(11)

ans = Solution()
if list1.data < list2.data:
    L = ans.mergingList(list1, list2)

else:
    L = ans.mergingList(list2, list1)


ans.printList(L)
