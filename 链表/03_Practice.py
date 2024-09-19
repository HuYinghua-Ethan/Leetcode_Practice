"""
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表
如果是，返回 true ；否则，返回 false 。

输入：head = [1,2,2,1]
输出：true

思路：
首先，我们需要找到链表的中间节点，如果链表长度为奇数，则中间节点为中间的那个节点；如果链表长度为偶数，则中间节点为中间的两个节点。
判断一个单链表是否为回文链表，可以使用快慢指针的方法来找到链表的中间节点，然后反转后半部分的链表，再与前半部分进行比较。
"""


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        
        # 使用快慢指针找到中间节点
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 反转后半部分链表
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        # 前半部分和反转后的后半部分进行比较
        left, right = head, prev
        while right:  # 只需比较后半部分
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
    

if __name__ == "__main__":
    my_solution = Solution()
    # 构建链表 1 -> 2 -> 2 -> 1
    head   = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    
    # 判断是否为回文链表
    print(my_solution.isPalindrome(head))  # 输出: True

    # 创建链表 1 -> 2 -> 3
    head2 = ListNode(1)
    head2.next = ListNode(2)
    head2.next.next = ListNode(3)

    # 判断是否为回文链表
    print(my_solution.isPalindrome(head2))  # 输出: False

