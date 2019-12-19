"""
return a tree's right-hand-most nodes in every level.
"""
import unittest

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def level_values(self, root, level, res):
        if not root:
            return
        if len(res) == level:
            res.append([])
        res[level].append(root.val)
        if root.left: self.level_values(root.left, level + 1, res)
        if root.right: self.level_values(root.right, level + 1, res)

    def right_values(self, root):
        res, ans = [], []
        self.level_values(root, 0, res)
        for level in res:
            ans.append(level[-1])
        return ans

    def generateTrees(self, n):
        def tree(left, right):
            ans = []
            if left > right:
                return [None]

            for i in range(left, right + 1):
                leftnodes = tree(left, i - 1)
                rightnodes = tree(i + 1, right)

                for leftnode in leftnodes:
                    for rightnode in rightnodes:
                        root = TreeNode(i)
                        root.left = leftnode
                        root.right = rightnode
                        ans.append(root)
            return ans

        if n == 0: return []
        return tree(1, n)

class TestSolution(unittest.TestCase):
    def test(self):
        solve = Solution()
        n = 3
        self.assertEqual(solve.right_values(solve.generateTrees(n)[0]), [1, 2, 3])
        self.assertEqual(solve.right_values(solve.generateTrees(n)[1]), [1, 3, 2])
        self.assertEqual(solve.right_values(solve.generateTrees(n)[2]), [2, 3])
        self.assertEqual(solve.right_values(solve.generateTrees(n)[3]), [3, 1, 2])
        self.assertEqual(solve.right_values(solve.generateTrees(n)[4]), [3, 2, 1])

if __name__ == "__main__":
    unittest.main()
