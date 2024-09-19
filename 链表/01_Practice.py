"""
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 null 。

图示两个链表在节点 c1 开始相交：

题目数据 保证 整个链式结构中不存在环。

注意，函数返回结果后，链表必须 保持其原始结构 。
自定义评测：
评测系统 的输入如下（你设计的程序 不适用 此输入）：
intersectVal - 相交的起始节点的值。如果不存在相交节点，这一值为 0
listA - 第一个链表
listB - 第二个链表
skipA - 在 listA 中（从头节点开始）跳到交叉节点的节点数
skipB - 在 listB 中（从头节点开始）跳到交叉节点的节点数
评测系统将根据这些输入创建链式数据结构，并将两个头节点 headA 和 headB 传递给你的程序。如果程序能够正确返回相交节点，那么你的解决方案将被 视作正确答案 。

输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,6,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
— 请注意相交节点的值不为 1，因为在链表 A 和链表 B 之中值为 1 的节点 (A 中第二个节点和 B 中第三个节点) 是不同的节点。换句话说，它们在内存中指向两个不同的位置，而链表 A 和链表 B 中值为 8 的节点 (A 中第三个节点，B 中第四个节点) 在内存中指向相同的位置。
 
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        ptrA = headA
        ptrB = headB
        while ptrA != ptrB:
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA
        return ptrA
            

if __name__ == "__main__":
    # listA = [4,1,8,4,5]
    # listB = [5,6,1,8,4,5]
    # 构建链表 A : 4 -> 1 -> 8 -> 4 -> 5
    headA = ListNode(4)
    node1 = ListNode(1)
    node2 = ListNode(8)
    node3 = ListNode(4)
    node4 = ListNode(5)
    
    headA.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    # 构建链表 B: 5 -> 6 -> 1 -> 8 -> 4 -> 5
    headB = ListNode(5)
    node5 = ListNode(6)
    node6 = ListNode(1)

    headB.next = node5
    node5.next = node6
    node6.next = node2

    # 创建Solution对象并测试
    my_solution = Solution()
    intersection_node = my_solution.getIntersectionNode(headA, headB)
    if intersection_node:
        print(f"Intersected at '{intersection_node.val}'")
    else:
        print("No intersection")


