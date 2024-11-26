from helpers import *

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode()
        sol = res
        while(list1 is not None and list2 is not None):
            if (list1.val < list2.val):
                temp = list1
                list1 = list1.next
            else:
                temp = list2
                list2 = list2.next
            res.next = temp
            temp.next = None
            res = res.next
        if(list1 is not None):
            res.next = list1
        else:
            res.next = list2
        return sol.next

list1 = [1,2,4]
list2 = [1,3,4]

solution = Solution()
sol = solution.mergeTwoLists(createSinglyLinkedList(list1), createSinglyLinkedList(list2))
printSinglyLinkedList(sol)