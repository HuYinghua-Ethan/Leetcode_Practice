"""
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。

输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]
""" 

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root=root.left)
        self.invertTree(root=root.right)
        return root

def print_tree(root):
    if root is None:
        return
    print(root.val, end=" ")
    print_tree(root.left)
    print_tree(root.right)


if __name__ == '__main__':
    # 构建二叉树：根节点为4，左子节点为2，右子节点为7，依次构建完整的树
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)
        
    my_solution = Solution()
    inverted_root = my_solution.invertTree(root)

    print_tree(inverted_root)

