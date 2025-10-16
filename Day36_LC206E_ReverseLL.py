# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        prev = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        # return current
        temp = prev
        while temp is not None:
            print(temp.val, end=" ")
            temp = temp.next

one = ListNode(1)
two = ListNode(2)
one.next = two
three = ListNode(3)
two.next = three
four = ListNode(4)
three.next = four
five = ListNode(5)
four.next = five
six = ListNode(6)
five.next = six
Solution().reverseList(one)