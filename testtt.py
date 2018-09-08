# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return "<{}>".format(self.val)

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
#         https://www.cnblogs.com/hiddenfox/p/3408931.html
        if head is None or head.next is None:
            return None
        slow,fast = head, head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if fast is slow:
                slow=head
                while True:
                    slow=slow.next
                    fast=fast.next
                    if fast is slow:
                        return fast
        return None

head=ListNode(1)
head.next=ListNode(2)
head.next.next=head
print(Solution().detectCycle(head))