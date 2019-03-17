"""
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].
"""
class Solution:
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        1029ms
        """
        row=len(M)
        col=0
        if row!=0:
            col=len(M[0])
        def Convolution(row,col,position,M):
            sum=0
            x=position[0];y=position[1]
            start_x=max(0,x-1)
            end_x=min(row-1,x+1)
            strat_y=max(0,y-1)
            end_y=min(col-1,y+1)
            count = (end_x-start_x+1)*(end_y-strat_y+1)
            for i in range(start_x,end_x+1):
                for j in range(strat_y,end_y+1):
                    sum+=M[i][j]
            # print(sum,count)
            return int((sum/count)//1)
        M_1=[[0 for j in range(col)] for i in range(row)]
        for i in range(row):
            for j in range(col):
                M_1[i][j]=Convolution(row,col,[i,j],M)
        return M_1
M=[[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
print(Solution().imageSmoother(M))