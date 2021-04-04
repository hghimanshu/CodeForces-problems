from Tree_latest import BST,BinaryTreeNode
class Solution:
    def maxPathSum(self, root):
        self.max_sum = -9999999
        def getPathSum(root):

            if not root.left and not root.right: #leaf nodes
                self.max_sum = max(root.data,self.max_sum)
                return root.data

            if root.left:
                left_sum = getPathSum(root.left)
                
            else:
                left_sum = 0

            if root.right:
                right_sum = getPathSum(root.right)
        
            else:
                right_sum = 0     
            self.max_sum = max(left_sum+root.data,self.max_sum)
            self.max_sum = max(right_sum+root.data,self.max_sum)
            self.max_sum = max(right_sum+root.data+left_sum,self.max_sum)
            self.max_sum = max(root.data,self.max_sum)
            
            return max(root.data,max(root.data+left_sum,root.data+right_sum))
            # current_sum = root.data + left_sum + right_sum
            # if current_sum > self.max_sum:
            #     self.max_sum=current_sum
            # return current_sum

        getPathSum(root)

        return self.max_sum





if __name__ == "__main__":
    bst = BST() 
    print(bst)
    bst.push(1)
    bst.push(-2)
    bst.push(3)
    soln = Solution()
    print(soln.maxPathSum(bst.root))