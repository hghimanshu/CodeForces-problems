class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def constructMaximumBinaryTree(nums):
    if not nums:
        return None
    curr = None
    # max_val = max(nums)
    # root = TreeNode(val=max_val)
    
    def build(curr,nums):
        max_val = max(nums)
        max_index = nums.index(max_val)
        prefix = nums[0:max_index]
        suffix = nums[max_index+1:]

        curr = TreeNode(val=max_val)

        if prefix:
            curr.left = build(curr.left,prefix)
        if suffix:
            curr.right = build(curr.right,suffix)

        return curr
    
    curr = build(curr,nums)
    return curr


if __name__ == "__main__":
    nums = [3,2,1,6,0,5]
    constructMaximumBinaryTree(nums)