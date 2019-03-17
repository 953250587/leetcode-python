"""
Given the running logs of n functions that are executed in a nonpreemptive single threaded CPU, find the exclusive time of these functions.

Each function has a unique id, start from 0 to n-1. A function may be called recursively or by another function.

A log is a string has this format : function_id:start_or_end:timestamp. For example, "0:start:0" means function 0 starts from the very beginning of time 0. "0:end:0" means function 0 ends to the very end of time 0.

Exclusive time of a function is defined as the time spent within this function, the time spent by calling other functions should not be considered as this function's exclusive time. You should return the exclusive time of each function sorted by their function id.

Example 1:

Input:
n = 2
logs =
["0:start:0",
 "1:start:2",
 "1:end:5",
 "0:end:6"]
Output:[3, 4]
Explanation:
Function 0 starts at time 0, then it executes 2 units of time and reaches the end of time 1.
Now function 0 calls function 1, function 1 starts at time 2, executes 4 units of time and end at time 5.
Function 0 is running again at time 6, and also end at the time 6, thus executes 1 unit of time.
So function 0 totally execute 2 + 1 = 3 units of time, and function 1 totally execute 4 units of time.

Note:

    Input logs will be sorted by timestamp, NOT log id.
    Your output should be sorted by function id, which means the 0th element of your output corresponds to the exclusive time of function 0.
    Two functions won't start or end at the same time.
    Functions could be called recursively, and will always end.
    1 <= n <= 100

"""
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        126ms
        """
        n_list = [0] * n
        n_dict ={}
        stack = []
        for log in logs:
            info =log.split(':')
            id = int(info[0])
            time = int(info[2])
            print(n_list)
            print(n_dict)
            if info[1] == 'start':
                if stack != []:
                    b = stack[-1]
                    n_list[b] += time - n_dict[b][-1][0]
                if id not in n_dict:
                    n_dict[id] = [[time, float('inf')]]
                else:
                    n_dict[id].append([time, float('inf')])
                stack.append(id)
            else:
                if stack[-1] != id:
                    n_dict[id][-1][-1] = time
                else:
                    a = stack.pop()
                    n_list[a] += time - n_dict[a][-1][0] + 1
                    n_dict[a].pop()
                    while stack != [] and n_dict[stack[-1]][-1][-1] < time:
                        b = stack.pop()
                        n_dict[stack[-1]].pop()
                    if stack != []:
                        n_dict[stack[-1]][-1][0] = time + 1
        result = []
        for i in n_list:
            result.append(i)
        return result

    def exclusiveTime_1(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        132ms
        """
        timeList = [0 for _ in range(n)]
        stack = list()
        prevEndTime = 0
        for log in logs:
            fId, op, time = log.split(':')
            fId, time = int(fId), int(time)

            if op == 'start':
                if len(stack) > 0:
                    timeList[stack[-1]] += time - prevEndTime
                stack.append(fId)
                prevEndTime = time
            else:
                fIds = stack.pop()
                timeList[fIds] += time - prevEndTime + 1
                prevEndTime = time + 1
        return timeList

    def exclusiveTime_2(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        92ms
        """
        stk = []

        rt = [0] * n
        last = 0
        for s in logs:
            sA = s.split(':')
            if sA[1] == 'start':
                ts = int(sA[2])
                if stk:
                    rt[stk[-1]] += (ts - last)
                last = ts
                stk.append(int(sA[0]))
            else:
                ts = int(sA[2]) + 1
                if stk:
                    rt[stk[-1]] += (ts - last)
                last = ts
                stk.pop()
        return rt
n = 2
logs = ["0:start:0",
 "1:start:2",
 "1:end:5",
 "0:end:6"]
print(Solution().exclusiveTime(n, logs))

n = 1
logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
print(Solution().exclusiveTime(n, logs))

