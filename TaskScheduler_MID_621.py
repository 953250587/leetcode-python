"""
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks.Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
"""
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        195ms
        """
        self.least=0
        self.num_tast=[0 for i in range(26)]
        for i in tasks:
            self.num_tast[ord(i)-ord('A')]+=1
        self.num_tast=sorted(self.num_tast,reverse=True)
        self.num=self.num_tast[0:n+1]
        while 0 not in self.num:
            self.least+=n+1
            for i in range(n+1):
                self.num_tast[i]-=1
            self.num_tast = sorted(self.num_tast,reverse=True)
            self.num = self.num_tast[0:n + 1]
        temp=self.num[0]
        if temp==0:
            return self.least
        count=1
        for i in self.num[1:]:
            if i==temp:
                count+=1
            else:
                break
        self.least+=(temp-1)*(n+1)+count
        print(self.num_tast)
        return self.least

    def leastInterval_1(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        172ms
        """
        self.num_tast = [0 for i in range(26)]
        for i in tasks:
            self.num_tast[ord(i) - ord('A')] += 1
        self.num_tast = sorted(self.num_tast, reverse=True)
        temp=self.num_tast[0]
        count=1
        for i in self.num_tast[1:]:
            if i==temp:
                count+=1
            else:
                break
        return max(len(tasks),(temp-1)*(n+1)+count)
tasks = ["A","B","C"]
n = 2
# tasks = ['A']
print(Solution().leastInterval_1(tasks,n))