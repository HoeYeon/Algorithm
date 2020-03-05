# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        check = 0
        tt = result
        while l1 or l2 or check:
            val1 = l1.val if l1 != None else 0
            val2 = l2.val if l2 != None else 0
            check, out = divmod(val1+val2+check, 10)
            tt.next = ListNode(out)
            tt = tt.next
            l1 = l1.next if l1 != None else l1
            l2 = l2.next if l2 != None else l2
        return result.next
