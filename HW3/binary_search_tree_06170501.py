#!/usr/bin/env python
# coding: utf-8

# In[7]:


class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None


        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
class Solution(object):
    def insert(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if root.val is not None:
            if root.val > val:
                if root.left is None:
                    root.left = TreeNode(val)
                else:
                    self.insert(root.left, val)
            elif root.val < val:
                if root.right is None:
                    root.right = TreeNode(val)
                else:
                    self.insert(root.right, val)
            else:
                temp = TreeNode(val)
                temp.left = root.left
                root.left = temp
        else:
            root.val=val

        '''if root.val is None:
                root.val = val
            elif root.val > val:
                if root.left is None
                    root.left = TreeNode(val)
                else:
                    self.insert(root.left, val)
            elif root.val < val:
                if root.right is None
                    root.right = TreeNode(val)
                else:
                    self.insert(root.right, val)
            else:
                temp = TreeNode(val)
                temp.left=root.left
                root.left=temp'''

    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """
        if root is None:
            return root
        elif root.val == target:
            if root.left is None and root.right is None:
                return None
            elif root.left is None and root.right is not None:
                return root.right
            elif root.left is not None and root.right is None:
                if root.left.val == target:
                    root.left = self.delete(root.left, target)
                return root.left
            else:
                if root.left.val == target:
                    root.left = self.delete(root.left, target)
                current = cur.right
                while current.left is not None:
                    current = current.left
                root.val = current.val
                current.val = target
                root.right = self.delete(root.right, target)
        elif root.val > target:
            root.left = self.delete(root.left, target)
        else:
            root.right = self.delete(root.right, target)
        return root

    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if root:
            if root.val is target:
                return root
            if root.left:
                temp = self.search(root.left, target)
                if temp is not None:
                    return temp
            if root.right:
                return self.search(root.right, target)


    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """
        cnt = [0]
        def dfs_cnt(root, target):
            if root:
                if root.val == target:
                    cnt[0] = cnt[0]+1
                dfs_cnt(root.left, target)
                dfs_cnt(root.right, target)
        dfs_cnt(root, target)
        self.delete(root, target)
        for i in range(cnt[0]):
            self.insert(root, new_val)

        '''sort_array=list()
            def traverseInorder(root, target):
                if root:
                    traverseInorder(root.left, target)
                    sort_array.append(root.val)
                    traverseInorder(root.right, target)
            def insertBalanced(start ,end):
                if(start>end):
                    return None
                mid = (start + end) // 2
                node = TreeNode(sort_array[mid])
                node.left = insertBalanced(start, mid-1)
                node.right = insertBalanced(mid+1, end)
            traverseInorder(root, target)
            insertBalanced(0, len(sort_array)-1)
            tree2D = self.printTree(node)
            for i in range(len(tree2D)):
                for j in range(len(tree2D[i])):
                    if tree2D[i][j]=="":
                        print(" ", end='')
                    else:
                        print(tree2D[i][j], end='')
                print("")'''


    def printTree(self, root):
        def height(root):
            if not root: return 0
            return max(height(root.left), height(root.right)) + 1

        def fill(root, h, l, r):
            if not root: return
            mid = (l + r) // 2
            m[h][mid] = str(root.val)
            if root.left: fill(root.left, h + 1, l, mid - 1)
            if root.right: fill(root.right, h + 1, mid + 1, r)

        h = height(root)
        w = 2 ** h - 1
        m = [[""] * w for _ in range(h)]
        fill(root, 0, 0, w - 1)
        return m

