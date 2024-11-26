from helpers import *


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def checkIfThereIsTwoDigitVal(l, res):
    if l is not None:
        if l.val < 10:
            res.next = l
        else:
            while l and l.val > 9:
                res.next = ListNode(l.val % 10)
                if l.next:
                    l.next.val += l.val // 10
                    res = res.next
                    l = l.next
                else:
                    res.next = ListNode(l.val % 10)
                    res.next.next = ListNode(l.val // 10)
                    l = l.next
            if l and l.val < 10:
                res.next = l
    return res.next


def addTwoNumbers(l1, l2):
    """
    Complexity: O(N)
    Idea: add next digits starting from units digit upto hundreds digit and so on as doing in "adding written",
    so if the digit > 10 after suming two node values then add units digit to res
    and tens digit to l1.next.val or l2.next.val if l1.next or l2.next exist
    """
    res = ListNode(0)
    sol = res
    while l1 and l2:
        suma = l1.val + l2.val
        if suma < 10:
            res.next = ListNode(suma)
        else:
            if l1.next is not None:
                l1.next.val += suma // 10
                res.next = ListNode(suma % 10)
            elif l2.next is not None:
                l2.next.val += suma // 10
                res.next = ListNode(suma % 10)
            else:
                # we need to create separate node for every digit in this at this number which is >= 10
                while suma > 9:
                    res.next = ListNode(suma % 10)
                    suma //= 10
                    res = res.next
                res.next = ListNode(suma)
        res = res.next
        l1 = l1.next
        l2 = l2.next
    # because we always add to l1 we can have here node with two digits number
    if l1 is not None:
        res = checkIfThereIsTwoDigitVal(l1, res)
    elif l2 is not None:
        res = checkIfThereIsTwoDigitVal(l2, res)
    return sol.next


def add_two_numbers2(l1, l2):
    """
    Complexity: O(N)
    Idea: 
        we have [2, 4, 3] and [5, 6, 4], we define mulit = 1 and we sum
        sum = 2*1 + 5*1 + 4*10 + 6*10 .....
        then sum is our solution we need to create ll from it where units digits will be first node
    """
    # we have special case as l1 = [0] and l2 = [0] then our sum will be 0 but we would return None
    if l1.val == 0 and l1.next is None and l2.val == 0 and l2.next is None:
        return l1
    
    suma = 0
    multi = 1

    while l1:
        suma += l1.val*multi 
        multi *= 10
        l1 = l1.next

    multi = 1
    while l2:
        suma += l2.val * multi
        multi *= 10
        l2 = l2.next

    # create res linked list
    res = ListNode(0)
    sol = res
    while suma != 0:
        res.next = ListNode(suma % 10)
        suma //= 10
        res = res.next
    return sol


l1 = createSinglyLinkedList([9, 9, 9, 9, 9, 9, 9])
l2 = createSinglyLinkedList([9, 9, 9, 9])

printSinglyLinkedList(addTwoNumbers(l1, l2))
# Output: [8,9,9,9,0,0,0,1]
