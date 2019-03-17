"""
 Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

    The root is the maximum number in the array.
    The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
    The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.

Construct the maximum tree by the given array and output the root node of this tree.

Example 1:

Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    /
     2  0
       \
        1

Note:

    The size of the given array will be in the range [1,1000].

"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        282ms
        """
        def structure2list(list):
            if list == []:
                return None
            max_1 = list[0]
            max_item = 0
            for i, val in enumerate(list):
                if val >= max_1:
                    max_1 = val
                    max_item = i
            root = TreeNode(max_1)
            root.left = structure2list(list[0: max_item])
            root.right = structure2list(list[max_item + 1:])
            return root
        return structure2list(nums)

    def constructMaximumBinaryTree_1(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        192ms
        """
        temp = []
        for n in nums:
            if len(temp) == 0:
                temp.append(TreeNode(n))
            elif temp[-1].val > n:
                n_node = TreeNode(n)
                temp[-1].right = n_node
                temp.append(n_node)
            else:
                n_node = TreeNode(n)
                while len(temp) != 0 and temp[-1].val < n:
                    n_node.left = temp[-1]
                    temp.pop()
                if len(temp) != 0:
                    temp[-1].right = n_node
                temp.append(n_node)

        return temp[0]

    def constructMaximumBinaryTree_2(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        159ms
        """
        st = []
        for num in nums:
            node = TreeNode(num)
            while st and num > st[-1].val:
                node.left = st.pop()
            if st:
                st[-1].right = node
            st.append(node)
        return st[0]
root = Solution().constructMaximumBinaryTree([3,2,1,6,0,5])
print(root)
def visit(root):
    if not root:
        print('None')
        return
    print(root.val)
    if root.left:
        visit(root.left)
    if root.right:
        visit(root.right)
visit(root)

