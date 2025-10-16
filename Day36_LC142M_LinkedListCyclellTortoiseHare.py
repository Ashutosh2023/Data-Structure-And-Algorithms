# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # Takes O(n) space
    # def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     hashSet = set()
    #     temp = head
    #     while temp is not None:
    #         # print(temp.val)
    #         if temp in hashSet:
    #             print(temp.val)
    #             return temp
    #         hashSet.add(temp)
    #         temp = temp.next
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            print(None)

        slow = head
        fast = head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        else:
            print(None)

        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        print(slow.val)   


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
six.next = two
Solution().detectCycle(one)

