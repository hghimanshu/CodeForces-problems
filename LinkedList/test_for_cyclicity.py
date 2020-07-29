class LinkNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next



class Solution:
    def test_for_cyclic(self, L):
        list = []
        cycleFound = False
        while L:
            if L.next.data not in list:
                list.append(L.data)
            else:
                cycleFound = True
                break
            L = L.next
        
        if cycleFound:

            print("Cycle found !!")
            print(L.data)
        else:
            print("No cycle found!!")


## Li --> 2 --> 6 --> 9 --> 6 --> 9
## s --> 2, f --> 4
# 
# output --> NO cycle


list1 = LinkNode(2)
list1.next = LinkNode(6)
list1.next.next = LinkNode(9)
list1.next.next.next = LinkNode(6)
list1.next.next.next.next = LinkNode(9)

ans = Solution()
ans.test_for_cyclic(list1)