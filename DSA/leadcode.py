#You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
#You may assume the two numbers do not contain any leading zero, except the number 0 itself.
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

def addTwoNumbers(l1, l2):
    dummy = ListNode(0)
    current = dummy
    carry = 0

    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0

        total = x + y + carry
        carry = total // 10

        current.next = ListNode(total % 10)
        current = current.next

        if l1: l1 = l1.next
        if l2: l2 = l2.next

    if carry:
        current.next = ListNode(carry)

    return dummy.next