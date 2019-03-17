"""
An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).

Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.

To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. Replace the color of all of the aforementioned pixels with the newColor.

At the end, return the modified image.

Example 1:
Input:
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation:
From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected
by a path of the same color as the starting pixel are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected
to the starting pixel.
Note:

The length of image and image[0] will be in the range [1, 50].
The given starting pixel will satisfy 0 <= sr < image.length and 0 <= sc < image[0].length.
The value of each color in image[i][j] and newColor will be an integer in [0, 65535]
"""
import numpy as np
class Solution:
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        109ms
        """
        self.row = len(image)
        if self.row <= 0:
            return image
        self.col = len(image[0])
        self.color = image[sr][sc]
        def dfs(sr, sc):
            if sr < self.row and sr >= 0 and sc < self.col and sc >= 0:
                if image[sr][sc] == self.color:
                    image[sr][sc] = -1
                else:
                    return
                dircations = [[1, 0], [0, 1], [-1, 0], [0, -1]]
                for dircation in dircations:
                    dfs(sr + dircation[0], sc + dircation[1])
            return
        dfs(sr, sc)
        for i in range(self.row):
            for j in range(self.col):
                if image[i][j] == -1:
                    image[i][j] = newColor
        return image

    def floodFill_1(self, image, sr, sc, newColor):
        """
        128ms
        :param image:
        :param sr:
        :param sc:
        :param newColor:
        :return:
        """
        rows, cols, orig_color = len(image), len(image[0]), image[sr][sc]

        def traverse(row, col):
            if (not (0 <= row < rows and 0 <= col < cols)) or image[row][col] != orig_color:
                return
            image[row][col] = newColor
            [traverse(row + x, col + y) for (x, y) in ((0, 1), (1, 0), (0, -1), (-1, 0))]

        if orig_color != newColor:
            traverse(sr, sc)
        return image
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
print(np.array(Solution().floodFill(image, sr, sc, newColor)))
