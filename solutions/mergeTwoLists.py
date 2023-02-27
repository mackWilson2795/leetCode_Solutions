# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        h1 = list1
        h2 = list2
        if h1 is None:
            return h2
        elif h2 is None:
            return h1

        if h1.val > h2.val:
            tmp2 = h2
            h2 = h1
            h1 = tmp2
        tmp = ListNode(next=h1)

        while h2 is not None:
            if tmp.next is None or tmp.next.val > h2.val:
                tmp2 = tmp.next
                tmp.next = h2
                h2 = tmp2
            else:
                tmp = tmp.next
        return h1