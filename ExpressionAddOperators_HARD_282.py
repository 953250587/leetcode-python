"""
 Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators (not unary) +, -, or * between the digits so they evaluate to the target value.

Examples:

"123", 6 -> ["1+2+3", "1*2*3"]
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []

"""
class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        import collections
        self.l = len(num)
        self.temp = []
        self.dicts = {}
        self.num = num
        def dfs(start):
            temp = []
            if start >= self.l:
                return []
            if start in self.dicts:
                return self.dicts[start]
            if self.num[start] != '0':
                for i in range(start + 1, self.l + 1):
                    lists = dfs(i)
                    cur_num = self.num[start:i]
                    for a in lists:
                        temp.append([cur_num] + a)
                temp.append([cur_num])
            else:
                lists = dfs(start + 1)
                cur_num = '0'
                for a in lists:
                    temp.append([cur_num] + a)
                if start == self.l - 1:
                    temp.append([cur_num])
            self.dicts[start] = temp
            return temp
        dfs(0)
        # print(self.dicts)
        self.result = []

        def dfs_cal(lists, number):
            if number >= len(lists) - 1:
                self.dicts_1[number] = [lists[number]]
                return [lists[number]]
            if number in self.dicts_1:
                return self.dicts_1[number]
            a = dfs_cal(lists, number + 1)
            temp = []
            for char in '+-*':
                for i in a:
                    temp.append(lists[number] + char + i)
            self.dicts_1[number] = temp
            return temp

        for i in self.dicts[0]:
            self.dicts_1 = collections.defaultdict(list)
            dfs_cal(i, 0)
            # print(self.dicts_1)
            for k in self.dicts_1[0]:
                if eval(k) == target:
                    self.result.append(k)

        return self.result

    def addOperators_1(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        1565ms
        """
        res = []
        for i in range(len(num)):
            cur_str = num[:i + 1]
            cur_num = int(cur_str)
            if str(cur_num) == cur_str:
                self.dfs(res, cur_str, i + 1, num, target, cur_num, cur_num, '+')
        return res

    def dfs(self, res, cur_str, pos, num, target, total, multiplier, operator):
        if pos == len(num):
            if total == target:
                res.append(cur_str)
            return

        i = pos
        while i < len(num):
            cur_s = num[pos:i + 1]
            cur_num = int(cur_s)
            if str(cur_num) == cur_s:
                self.dfs(res, cur_str + '+' + cur_s, i + 1, num, target, total + cur_num, cur_num, '+')
                self.dfs(res, cur_str + '-' + cur_s, i + 1, num, target, total - cur_num, cur_num, '-')
                if operator == '+':
                    self.dfs(res, cur_str + '*' + cur_s, i + 1, num, target, total - multiplier + multiplier * cur_num,
                             multiplier * cur_num, operator)
                else:
                    self.dfs(res, cur_str + '*' + cur_s, i + 1, num, target, total + multiplier - multiplier * cur_num,
                             multiplier * cur_num, operator)
            i += 1

    def addOperators_2(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        1382
        """
        self.ans = []
        self.target = target
        for i in range(1, len(num) + 1):
            if i > 1 and num[0] == '0':
                continue
            path = num[:i]
            n = int(num[:i])
            self.dfs(num[i:], path, n, n)
        return self.ans

    def dfs(self, num, path, val, last):
        if not num:
            if val == self.target:
                self.ans.append(path)
            return

        for i in range(1, len(num) + 1):
            if i > 1 and num[0] == '0':
                continue
            rest = num[i:]
            s = num[:i]
            n = int(s)
            self.dfs(rest, path + '+' + s, val + n, n)
            self.dfs(rest, path + '-' + s, val - n, -n)
            self.dfs(rest, path + '*' + s, val - last + n * last, n * last)

print(Solution().addOperators("123", 6))
print(Solution().addOperators("0", 0))
print(Solution().addOperators("11", 11))
print(Solution().addOperators("100", 6))
print(Solution().addOperators('232', 8))
print(Solution().addOperators('105', 5))
print(Solution().addOperators('00', 0))
print(Solution().addOperators('3456237490', 9191))






