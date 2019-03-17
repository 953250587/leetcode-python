"""
 Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.

Examples 1
Input:

  5
 /  \
2   -3

return [2, -3, 4], since all the values happen only once, return all of them in any order.

Examples 2
Input:

  5
 /  \
2   -5

return [2], since 2 happens twice, however -5 only occur once.

Note: You may assume the sum of values in any subtree is in the range of 32-bit signed integer.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        82ms
        """
        if not root:
            return []
        import collections
        self.dicts = collections.defaultdict(int)

        def dfs(root):
            if not root.left and not root.right:
                self.dicts[root.val] += 1
                return root.val
            if root.left:
                a = dfs(root.left)
            else:
                a = 0
            if root.right:
                b = dfs(root.right)
            else:
                b = 0
            c = a + b + root.val
            self.dicts[c] += 1
            return c

        dfs(root)
        s = sorted(self.dicts.items(), key=lambda a:a[1], reverse=True)
        temp = s[0][1]
        result=[]
        for i in s:
            if i[1] < temp:
                break
            result.append(i[0])
        return result

    def findFrequentTreeSum_1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        82ms
        """
        import collections
        if not root:
            return []
        r = []
        h = collections.defaultdict(int)

        def treeSum(node):
            if not node:
                return 0

            ls = treeSum(node.left)
            rs = treeSum(node.right)
            ss = ls + rs + node.val

            h[ss] += 1

            return ss

        treeSum(root)

        c = max(h.values())
        for k, v in h.items():
            if v == c:
                r.append(k)
        return r
root = TreeNode(5)
root.left = TreeNode(2)
root.right =TreeNode(-3)
print(Solution().findFrequentTreeSum(root))

root = TreeNode(5)
root.left = TreeNode(2)
root.right =TreeNode(-5)
print(Solution().findFrequentTreeSum(root))

root = TreeNode(5)
# root.left = TreeNode(2)
# root.right =TreeNode(-5)
print(Solution().findFrequentTreeSum(None))