"""
 You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north, then x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on. In other words, after each move your direction changes counter-clockwise.

Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.

Example 1:

Given x = [2, 1, 1, 2],
?????
?   ?
???????>
    ?

Return true (self crossing)

Example 2:

Given x = [1, 2, 3, 4],
????????
?      ?
?
?
?????????????>

Return false (not self crossing)

Example 3:

Given x = [1, 1, 1, 1],
?????
?   ?
?????>

Return true (self crossing)

"""
class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        45ms
        """
        def isCross_1(pos_start, pos_final):
            if pos_start[0] >= pos_final[0] and pos_start[1] <= pos_final[1]:
                return 1
            elif pos_start[0] < pos_final[0]:
                return 2
            elif pos_start[0] == pos_final[0]:
                return 3
            else:
                return 4

        def isCross(line1, line2):
            if line1[0] <= line2[1][1] and line1[0] >= line2[1][0] \
                and line2[0] <= line1[1][1] and line2[0] >= line1[1][0]:
                return True
            else:
                return False

        def isCross_2(dic, cur_lines, num):
            if num == 2:
                for i, cur_line in enumerate(cur_lines):
                    if isCross(cur_line, dic[(i + 1) % 4]):
                        return True
                    else:
                        dic[i] = cur_line
            if num == 3:
                for i, cur_line in enumerate(cur_lines):
                    if i == 0:
                        if dic[i][1][0] <= cur_line[1][1]:
                            return True
                        else:
                            dic[i] = cur_line
                    else:
                        if isCross(cur_line, dic[(i + 1) % 4]):
                            return True
                        else:
                            dic[i] = cur_line
            if num == 4:
                for i,cur_line in enumerate(cur_lines):
                    if i == 0:
                        continue
                    if isCross(cur_line, dic[(i - 1) % 4]):
                        return True
                    else:
                        dic[i - 1] = cur_lines[i - 1]
            return False

        if len(x) <= 3:
            return False
        dic = []
        cur_x, cur_y = 0, 0
        start_x, start_y = 0, 0
        for num, i in enumerate(x[0:4]):
            if num % 4 in [2, 3]:
                i = -i
                dic.append([cur_x, [cur_y + i, cur_y]])
            else:
                dic.append([cur_x, [cur_y, cur_y + i]])
            cur_x, cur_y = cur_y + i, cur_x
            print(cur_x, cur_y)
        print(dic)
        count = 4
        while count <= len(x):
            # print([[start_x, start_y], [cur_x, cur_y]])
            num_1 = isCross_1([start_x, start_y], [cur_x, cur_y])
            print(num_1)
            if num_1 == 1:
                # print('num_1', num_1)
                return True
            else:
                start_x, start_y = cur_x, cur_y
            cur_lines = []
            for num, i in enumerate(x[count:count + 4]):
                if num % 4 in [2, 3]:
                    i = -i
                    cur_lines.append([cur_x, [cur_y + i, cur_y]])
                else:
                    cur_lines.append([cur_x, [cur_y, cur_y + i]])
                cur_x, cur_y = cur_y + i, cur_x
            count += 4
            if isCross_2(dic, cur_lines, num_1):
                return True
        return False

    def isSelfCrossing_1(self, x):
        """
        29ms
        :param x:
        :return:
        """
        b = c = d = e = 0
        for a in x:
            if d >= b > 0 and (a >= c or a >= c - e >= 0 and f >= d - b):
                return True
            b, c, d, e, f = a, b, c, d, e
        return False

# print(Solution().isSelfCrossing(x = [2, 1, 1, 2]))
# print(Solution().isSelfCrossing(x = [1, 2, 3, 4]))
# print(Solution().isSelfCrossing(x = [1, 1, 1, 1]))
print(Solution().isSelfCrossing(x = [1, 2, 3, 2, 1, 1]))
print(False or True and False)


