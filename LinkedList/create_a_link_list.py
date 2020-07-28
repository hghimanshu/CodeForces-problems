
class LinkNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class Solution:
    def printList(self, L):
        while L:
            print(L.data)
            L = L.next




# [1 --> 2 --> 4 --> 6]
node = LinkNode(1)
node.next = LinkNode(2)
node.next.next = LinkNode(4)
node.next.next.next = LinkNode(6)


ans = Solution()
ans.printList(node)