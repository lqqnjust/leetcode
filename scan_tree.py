# coding:utf-8

"""
树的几种遍历方式
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


a = TreeNode('A')
b = TreeNode('B')
c = TreeNode('C')
d = TreeNode('D')
e = TreeNode('E')
f = TreeNode('F')
g = TreeNode('G')
h = TreeNode('H')
i = TreeNode('I')
j = TreeNode('J')
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g
d.left = h
d.right=i
e.left=j

def preorder(root):
    """
    前序遍历
    :param root:
    :return:
    """
    if root is None:
        return ''
    v = root.val
    lv = preorder(root.left)
    rv = preorder(root.right)
    return v+lv+rv

def midorder(root):
    if root is None:
        return ''
    v = root.val
    lv = midorder(root.left)
    rv = midorder(root.right)
    return lv+v+rv

def endorder(root):
    if root is None:
        return ''
    v = root.val
    lv = endorder(root.left)
    rv = endorder(root.right)
    return lv+rv+v

def graorder(root):
    """
    用队列来存储同一层节点，先进先出
    :param root:
    :return:
    """
    if root is None:
        return ''
    queue = [root]
    v=''
    while len(queue)>0:

        item = queue.pop(0)
        v+=item.val
        if item.left:
            queue.append(item.left)
        if item.right:
            queue.append(item.right)
    print(v)

if __name__ == '__main__':
    v = preorder(a)
    print("前序",v)

    v = midorder(a)
    print("中序",v)

    v = endorder(a)
    print("后序",v)

    graorder(a)