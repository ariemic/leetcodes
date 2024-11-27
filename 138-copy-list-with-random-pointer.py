# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Graph:
  def __init__(self, x: int, next: "Graph" = None, random: "Graph" = None) -> None:
      pass

def copyRandomList(head: "Optional[Node]") -> "Optional[Node]":
    """
    1. copy ll without random pointers
    2. and random pointers
    I can't do this in one go, because these nodes don't exist yet
    """
    q = head
    res = Node(q.val)
    q = q.next
    sol = res

    while q:
        res.next = Node(q.val)
        q = q.next
        res = res.next
    res.next = None

    r = sol
    while head:
        sol.random = head.random
