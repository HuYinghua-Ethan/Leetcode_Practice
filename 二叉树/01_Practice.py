"""
给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。


示例 1：
输入：root = [1,null,2,3]
输出：[1,3,2]


前序遍历
def pre_order(root: TreeNode | None):
    if root is None:
        return
    # 访问优先级：根节点 -> 左子树 -> 右子树
    res.append(root.val)
    pre_order(root=root.left)
    pre_order(root=root.right)


中序遍历
def in_order(root: TreeNode | None):
    if root is None:
        return
    # 访问优先级：左子树 -> 根节点 -> 右子树
    in_order(root=root.left)
    res.append(root.val)
    in_order(root=root.right)

后序遍历
def post_order(root: TreeNode | None):
    if root is None:
        return
    # 访问优先级：左子树 -> 右子树 -> 根节点
    post_order(root=root.left)
    post_order(root=root.right)
    res.append(root.val)

"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        result = []
        self._inorderHelper(root, result)
        return result
    
    def _inorderHelper(self, root, result):
        if root is None:
            return
        self._inorderHelper(root.left, result)   # 访问左子树
        result.append(root.val)                   # 访问根节点
        self._inorderHelper(root.right, result)  # 访问右子树
        
if __name__ == "__main__":
    # 构建二叉树：根节点为1，右子节点为2，左子节点为3
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    
    my_solution = Solution()
    result = my_solution.inorderTraversal(root)
    print(result)  # 输出: [1, 3, 2]




