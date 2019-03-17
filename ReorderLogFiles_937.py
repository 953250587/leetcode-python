"""
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.



Example 1:

Input: ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]


Note:

0 <= logs.length <= 100
3 <= logs[i].length <= 100
logs[i] is guaranteed to have an identifier, and a word after the identifier.
"""


class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        36 ms
        """
        # 分成两部分，然后分别判断
        new_logs = [log.split(' ', 1) for log in logs]
        # print(new_logs)
        digit_logs = []
        letter_logs = []
        for log in new_logs:
            if log[1][0].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        # print(digit_logs)
        # print(letter_logs)
        result = sorted(letter_logs, key=lambda a:a[1]) + digit_logs
        return [log[0] + ' ' + log[1] for log in result]

    def reorderLogFiles_1(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        32ms
        """
        # ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
        # filter(lambda x : x[x.find(" ") + 1].isdigit(), logs)
        # fast
        # filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。
        d = filter(lambda x: x.split()[1].isdigit(), logs)
        l = filter(lambda x: x.split()[1].isalpha(), logs)
        # l = filter(lambda x : x[x.find(" ") + 1].isalpha(), logs)
        # slow
        # d = [i for i in logs if i[i.find(" ") + 1].isdigit()]
        # l = [i for i in logs if i[i.find(" ") + 1].isalpha()]
        # l.sort(key = lambda x: (x[x.find(" "):]))
        l.sort(key=lambda x: x.split(" ", 1)[1])
        return l + d


print(Solution().reorderLogFiles(["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]))