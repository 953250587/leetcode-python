"""
Suppose we abstract our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.

Note:
The name of a file contains at least a . and an extension.
The name of a directory or sub-directory will not contain a ..
Time complexity required: O(n) where n is the size of the input string.

Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.
"""
class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        35ms
        """
        self.count=0
        self.num=0
        self.max=0
        self.l=len(input)
        self.input=input

        def read_info(start,rank):
            count=1
            rank_1=0
            flag=False
            while start<self.l:
                while start<self.l and self.input[start] != '\n':
                    if self.input[start] == '.':
                        flag = True
                    count += 1
                    start += 1
                self.num += count
                if flag:
                    self.max = max(self.max, self.num)
                start += 1
                if start >= self.l:
                    return start,rank_1
                while self.input[start] == '\t':
                    rank_1 += 1
                    start += 1
                print('k', start, rank_1, rank, self.num, self.max,count)
                if rank_1 > rank:
                    start,rank_1 = read_info(start, rank_1)
                self.num -= count
                count=1
                flag=False
                if rank_1 < rank:
                    return start,rank_1
                rank_1=0
            return start
        start=0
        while start<self.l:
            start=read_info(start,0)
        return max(self.max-1,0)

    def lengthLongestPath_1(self, input):
        """
        :type input: str
        :rtype: int
        32ms
        """
        maxLen = 0
        pathLen = {0: 0}
        for line in input.split('\n'):
            name = line.strip('\t')
            level = len(line) - len(name)
            if '.' in name:
                maxLen = max(maxLen, pathLen[level] + len(name))
            else:
                pathLen[level + 1] = (pathLen[level] + len(name) + 1)
        return maxLen

s="dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
l=len(s)
s="dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
# s="a\n\taa\n\t\taaa\n\t\t\tfile1.txt\naaaaaaaaaaaaaaaaaaaaa\n\tsth.png"
print(len(s))
print(Solution().lengthLongestPath(s))

