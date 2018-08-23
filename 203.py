import unittest

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return head
        
        while True:
            if head is None :
                return None
            if head.val == val:
                head = head.next 
            else:
                break 
        cur = head
        pre = head

        cur = pre.next 
        while cur is not None:
            if cur.val == val:
                pre.next=cur.next 
                cur = cur.next 
            else:
                pre = cur 
                cur = cur.next 
                    
        return head

        


class TestSolution(unittest.TestCase):
    def setUp(self, *args, **kwargs):
        self.s = Solution()
        
        
    def init(self, arr):
        if len(arr)==0:
            return None
        head = None
        cur = None
        for a in arr:
            node = ListNode(a)
            if head is None:
                head = node 
                cur = head 
            else:
                cur.next = node 
                cur = node 
        return head
    
    def listnode2list(self, head):
        list = []
        cur = head 
        while cur is not None:
            list.append(cur.val)
            cur = cur.next 
        return list
            
    def test1(self):
        arr = [1,2,3]
        expect = [1,3]
        actual = self.s.removeElements(self.init(arr), 2)
        list_actual = self.listnode2list(actual)
        self.assertEqual(list_actual, expect)

    def test2(self):
        arr = [1,2,3,2]
        expect = [1,3]
        actual = self.s.removeElements(self.init(arr), 2)
        list_actual = self.listnode2list(actual)
        self.assertEqual(list_actual, expect)

    def test3(self):
        arr = []
        expect = []
        actual = self.s.removeElements(self.init(arr), 2)
        list_actual = self.listnode2list(actual)
        self.assertEqual(list_actual, expect)
    
    def test4(self):
        arr = [1]
        expect = [1]
        actual = self.s.removeElements(self.init(arr), 2)
        list_actual = self.listnode2list(actual)
        self.assertEqual(list_actual, expect)
    def test5(self):
        arr = [1,1]
        expect = []
        actual = self.s.removeElements(self.init(arr), 1)
        list_actual = self.listnode2list(actual)
        self.assertEqual(list_actual, expect)

if __name__ == '__main__':
    unittest.main()