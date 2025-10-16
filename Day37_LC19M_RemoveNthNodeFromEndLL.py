# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1. Create a dummy node pointing to the head.
        dummy = ListNode(0)
        dummy.next = head
        
        slow = dummy
        fast = dummy
        
        # 2. Move 'fast' pointer n+1 steps ahead.
        # This creates a gap of n nodes between 'slow' and 'fast',
        # and positions 'slow' one node BEFORE the one to be removed
        # when 'fast' reaches the end.
        for _ in range(n + 1):
            if fast is None:
                # Should not happen given problem constraints, but good practice
                print(head.val)
                break
            fast = fast.next
            
        # 3. Move both pointers forward one step at a time
        # until 'fast' reaches the end (i.e., 'fast' is None).
        while fast is not None:
            slow = slow.next
            fast = fast.next
            
        # 4. Remove the Nth node from the end.
        # At this point, 'slow' is pointing to the node *before* the target.
        # The target node is 'slow.next'.
        slow.next = slow.next.next
        
        # 5. Return the new head (which is dummy.next)
        print(dummy.next.val)

        temp = dummy.next
        while temp is not None:
            print(temp.val)
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
Solution().removeNthFromEnd(one, 3) 