"""
We are given a binary tree (with root node root), a target node, and an integer value `K`.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any order.



Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
Output: [7,4,1]
Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.

Note:

The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode !!!!!!!!!
        :rtype: List[int]
         48 ms
        """
        dicts_node = {root.val: None}
        dicts_n = {}
        def visit(root, dicts_node, dicts_n):
            dicts_n[root.val] = root
            if root.left:
                dicts_node[root.left.val] = root
                visit(root.left, dicts_node, dicts_n)
            if root.right:
                dicts_node[root.right.val] = root
                visit(root.right, dicts_node, dicts_n)


        result = []
        used = set()
        def find_k(start, k, result):
            if start.val in used:
                return []
            used.add(start.val)
            if k == 0 and start:
                return [start.val]
            parent = dicts_node[start.val]
            a, b, c =[], [], []
            if start.left:
                a += find_k(start.left, k - 1, result)
            if start.right:
                b += find_k(start.right, k - 1, result)
            if parent:
                # used.add(parent.val)
                # print('parent', parent.val, 'k - 1', k - 1)
                c += find_k(parent, k - 1, result)
            result = a + b + c
            # print(result, start.val)
            return result
        visit(root, dicts_node, dicts_n)
        # print(start.val)
        return find_k(dicts_n[target], K, result)

    def distanceK_1(self, root, target, K):
        """
        44ms
        :param root:
        :param target:
        :param K:
        :return:
        """
        import collections
        def dfs(node, par=None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        queue = collections.deque([(target, 0)])
        seen = {target}
        while queue:
            if queue[0][1] == K:
                return [node.val for node, d in queue]
            node, d = queue.popleft()
            for nei in (node.left, node.right, node.par):
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d + 1))

        return []

root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.left = TreeNode(8)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
print(Solution().distanceK(root, target = 5, K = 2))
