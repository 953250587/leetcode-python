"""
Given a binary tree, we install cameras on the nodes of the tree.

Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.



Example 1:


Input: [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.
Example 2:


Input: [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.

Note:

The number of nodes in the given tree will be in the range [1, 1000].
Every node has value 0.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        52 ms
        13.5 MB
        """
        """
        使用dfs反向贪心搜索
        用0表示当前节点未被相机照到
        用1表示当前节点被相机照到
        用2表示当前节点就是相机位置
        """
        ans = 0

        def _isleaf(root):
            if not root.left and not root.right:
                return True
            else:
                return False

        def dfs(root):
            nonlocal ans
            # 初始化左右子树,如果没有可以当作是当前节点被其它节点包括的情况
            # 及如果没有左右子树,则可以无视掉
            left = right = 1
            if root.left:
                # 如果有左子树,且为叶子节点,叶子节点默认为0的情况
                if _isleaf(root.left):
                    left = 0
                # 否则则获得左子树的情况
                else:
                    left = dfs(root.left)
            # 右子树和左子树相同
            if root.right:
                if _isleaf(root.right):
                    right = 0
                else:
                    right = dfs(root.right)
            # 得到左右子树比较的情况
            min_temp = min(left, right)
            max_temp = max(left, right)
            # 如果左右子树任一个没有被相机照到,则当前节点一定要为一个相机点
            if min_temp == 0:
                ans += 1
                # print(root.val, ans)
                return 2
            # 否则
            else:
                # 有一个为相机节点,且另一个被相机照到,则当前节点也是能被相机照到
                if max_temp == 2:
                    return 1
                # 2个都是被相机照到,则该节点则未被任何相机照到
                else:
                    return 0
        # 如果根节点未被相机照到,则需要把自己位置指定为相机位置
        if dfs(root) == 0:
            ans += 1
        return ans

    def minCameraCover_1(self, root):
        """
        52 ms
        13.5 MB
        :param root:
        :return:
        """
        self.res = 0

        def dfs(root):
            if not root: return 2
            l, r = dfs(root.left), dfs(root.right)
            if l == 0 or r == 0:
                self.res += 1
                return 1
            return 2 if l == 1 or r == 1 else 0

        return (dfs(root) == 0) + self.res


if __name__ == '__main__':
    root = TreeNode(0)
    root.left = TreeNode(0)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(0)
    print(Solution().minCameraCover(root))  # 1

    root = TreeNode(0)
    root.left = TreeNode(1)
    root.left.left = TreeNode(2)
    root.left.left.right = TreeNode(3)
    print(Solution().minCameraCover(root))  # 2

    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    root.right.left.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.right.left = TreeNode(8)
    print(Solution().minCameraCover(root))  # 3

    root = TreeNode(0)
    print(Solution().minCameraCover(root))  # 1

    root = TreeNode(0)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    print(Solution().minCameraCover(root))  # 2


