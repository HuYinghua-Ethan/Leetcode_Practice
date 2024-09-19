"""
给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head
        while current:
            next_node = current.next   # 保存下一个节点
            current.next = prev        # 反转当前节点的指向
            prev = current             # 更新 prev
            current = next_node        # 更新 current
        return prev
            

if __name__ == "__main__":
    head = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(5)

    head.next = node1
    node1.next = node2
    node2.next = node3
    node3.next = node4

    my_solution = Solution()
    new_head = my_solution.reverseList(head)
    while new_head:
        print(new_head.val, end=" ")
        new_head = new_head.next

    









