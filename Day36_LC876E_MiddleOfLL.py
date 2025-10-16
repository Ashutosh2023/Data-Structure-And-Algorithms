# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = j = 1
        ipos = jpos = head
        while jpos is not None:
            print(jpos.val, end=" ")
            if i <= j//2:
                i += 1
                ipos = ipos.next
            else:
                j += 1
                jpos = jpos.next
        print("||", end="")
        while ipos is not None:
            print(ipos.val, end = " ")
            ipos = ipos.next

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
Solution().middleNode(one)