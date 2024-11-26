class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createSinglyLinkedList(array):
    n = len(array)
    if (n == 0): return ListNode(None)
    head = ListNode(array[0])
    res = head
    for i in range(1, n):
        head.next = ListNode(array[i])
        head = head.next
    head.next = None
    return res

def printSinglyLinkedList(linkedList):
    arr = []
    while(linkedList != None):
        temp = linkedList
        linkedList = linkedList.next
        temp.next = None
        arr.append(temp.val)
    print("->".join(map(str, arr)))
        