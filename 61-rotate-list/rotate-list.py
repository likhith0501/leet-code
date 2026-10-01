# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next or k == 0:
            return head

        # 1. Compute the length of the list and locate the tail
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # 2. Normalize k (k can be larger than length)
        k %= length
        if k == 0:
            return head

        # 3. Form a ring by linking the tail to the head
        tail.next = head

        # 4. Find the new tail: (length - k - 1) steps from head
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next

        # 5. Break the ring and update head
        new_head = new_tail.next
        new_tail.next = None

        return new_head