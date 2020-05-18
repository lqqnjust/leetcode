from typing import List
from queue import Queue
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        levels = []
        node_queue = Queue()
        node_queue.put(root)

        while True:
            current_level = []
            current_node_size = node_queue.qsize()
            if current_node_size==0:
                break
            for x in range(current_node_size):
                node  =node_queue.get()
                current_level.append(node.val)
                if node.left:
                    node_queue.put(node.left)
                if node.right:
                    node_queue.put(node.right)
            levels.append(current_level)
        return levels[::-1]