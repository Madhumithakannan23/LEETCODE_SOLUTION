class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:

            x = 0
            if l1:
                x = l1.val
                l1 = l1.next

            y = 0
            if l2:
                y = l2.val
                l2 = l2.next

            total = x + y + carry
            carry = total // 10

            current.next = ListNode(total % 10)
            current = current.next

        return dummy.next