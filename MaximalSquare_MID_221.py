"""
 Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Return 4.
"""
class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        395ms
        """
        row=len(matrix)
        if row<=0:
            return 0
        column=len(matrix[0])
        print(row,column)
        def findsquare(i,j):
            for num in range(1,min(row-i,column-j)):
                for new_j in range(num+1):
                    # print('value_!', matrix[i+num][j+new_j])
                    if matrix[i+num][j+new_j]!='1':
                        return num-1
                for new_i in range(num+1):
                    # print('value_?', matrix[i+new_i][j+num])
                    if matrix[i+new_i][j+num]!='1':
                        return num-1
            return min(row-i,column-j)-1

        max_area=0
        for i in range(row):
            for j in range(column):
                if matrix[i][j]!='0':
                    num=findsquare(i,j)
                    print(num)
                    max_area=max(num+1,max_area)
        return max_area**2

    def maximalSquare_dp(self, matrix):
        # 76ms
        if (not matrix) or (not matrix[0]):
            return 0
        n = len(matrix)
        m = len(matrix[0])
        widths = [0] * n
        k = 0
        # 选定一列
        for j in range(0, m):
            max_continous_k = 0
            continous_k = 0
            for i in range(0, n):
                # 如果行为1，宽度+1
                if matrix[i][j] == '1':
                    widths[i] += 1
                # 否则重置为0
                else:
                    widths[i] = 0
                if widths[i] > k:
                    continous_k += 1
                    max_continous_k = max(continous_k, max_continous_k)
                else:
                    continous_k = 0
            if max_continous_k > k:
                k += 1
        return k * k

print(Solution().maximalSquare(['0110','1111','1110','1110']))