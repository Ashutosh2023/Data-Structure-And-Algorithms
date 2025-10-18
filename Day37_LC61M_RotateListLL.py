from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        temp = head
        length = 1
        while temp.next != None:
            length += 1
            temp = temp.next
        k = k % length
        temp.next = head
        end = length-k
        while end:
            print(end,":", temp.val)
            temp = temp.next
            end -= 1
        head = temp.next
        temp.next = None
        
        temp = head
        while temp is not None:
            print(temp.val, end="-")
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
# six = ListNode(6)
# five.next = six
Solution().rotateRight(one,2)