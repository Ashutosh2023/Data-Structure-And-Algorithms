from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]):
        temp = head
        n = 0
        while temp is not None:
            n += 1
            temp = temp.next

        dummy = ListNode(0,head)

        slow = dummy
        fast = dummy

        count = 0
        while fast.next is not None:
            count += 1
            slow = slow.next
            fast = fast.next.next
            if fast is None:
                break
        print(count, "::", slow.val)
        current = slow.next
        prev = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        #combine the reversed section to the start section
        slow.next = prev

        # compare
        slow = slow.next
        temp = head
        while slow is not None:
            print(temp.val, "-", slow.val)
            if temp.val != slow.val:
                print("False")
                return
            slow = slow.next
            temp = temp.next
        print("True")
        return


# one = ListNode(1)
# two = ListNode(2)
# one.next = two
# three = ListNode(3)
# two.next = three
# four = ListNode(0)
# three.next = four
# five = ListNode(3)
# four.next = five
# six = ListNode(2)
# five.next = six
# seven = ListNode(1)
# six.next = seven

one = ListNode(1)
two = ListNode(2)
one.next = two
three = ListNode(2)
two.next = three
four = ListNode(1)
three.next = four
Solution().isPalindrome(one)