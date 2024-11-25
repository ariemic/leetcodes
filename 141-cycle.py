# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # pomysł: mamy dwa pointery: pierwszy skacze o 1 do przodu, drugi skacze o 2 do przodu, jeśli pointery się kiedyś spotkają to mamy cykl
        # jeśli szybszy pointer wyjdzie poza linked liste to nie ma cyklu
        if(head is None): return False

        fast = head
        slow = head
  
        while(fast.next != None and fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
            if (slow == fast): return True
        return False
    

head = ListNode(3)
node2 = ListNode(2)
node3 = ListNode(0)
node4 = ListNode(-4)

head.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

head2 = ListNode(1)

solution = Solution()
# print(solution.hasCycle(head))
print(solution.hasCycle(head2))