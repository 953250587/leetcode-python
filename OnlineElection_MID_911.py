"""
In an election, the i-th vote was cast for persons[i] at time times[i].

Now, we would like to implement the following query function: TopVotedCandidate.q(int t) will return the number of the person that was leading the election at time t.

Votes cast at time t will count towards our query.  In the case of a tie, the most recent vote (among tied candidates) wins.



Example 1:

Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
Output: [null,0,1,1,0,0,1]
Explanation:
At time 3, the votes are [0], and 0 is leading.
At time 12, the votes are [0,1,1], and 1 is leading.
At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
This continues for 3 more queries at time 15, 24, and 8.


Note:

1 <= persons.length = times.length <= 5000
0 <= persons[i] <= persons.length
times is a strictly increasing array with all elements in [0, 10^9].
TopVotedCandidate.q is called at most 10000 times per test case.
TopVotedCandidate.q(int t) is always called with t >= times[0].
"""


class TopVotedCandidate(object):
    def __init__(self, persons, times):
        """
        :type persons: List[int]
        :type times: List[int]
        532 ms,
        """
        import collections
        # 先对时间排个序
        self.times = sorted(times)
        # 记录每个时间点的当选人物
        self.sort_list = []
        # 用来记录每个人得票的变化
        self.persons_vote = collections.defaultdict(int)
        # 一开始无人当选
        cur_person = None
        # 按时间排完序的进行判断
        for person, time in sorted(zip(persons, times), key=lambda a:a[1]):
            # 得票数+1
            self.persons_vote[person] += 1
            # 得到投票的人的票数是否超过上次最多的人
            if cur_person is not None:
                cur_person = cur_person if self.persons_vote[person] < self.persons_vote[cur_person] else person
            else:
                cur_person = person
            print(person, times, cur_person)
            self.sort_list.append(cur_person)
        print(self.sort_list)
        print(self.times)


    def q(self, t):
        """
        :type t: int
        :rtype: int
        """
        import bisect
        # 二分查找当前时间点之前的位置
        position = bisect.bisect_right(self.times, t)
        # print('t', t, 'position', position)
        if position > 0:
            return self.sort_list[position - 1]
        else:
            return None




# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
# persons = [0, 1, 1, 0, 0, 1, 0]
# times = [0,5,10,15,20,25,30]
# obj = TopVotedCandidate(persons, times)
# ts = [[3],[12],[25],[15],[24],[8]]
# for t in ts:
#     print(obj.q(t[0]))


persons = [0,0,0,0,1]
times = [0,6,39,52,57]
obj = TopVotedCandidate(persons, times)
ts = [[45],[49],[59],[68],[42],[37],[99],[26],[78],[43]]
for t in ts:
    print(obj.q(t[0]))

from collections import defaultdict

import bisect
class TopVotedCandidate(object):
    def __init__(self, persons, times):
        """
        384 ms
        :param persons:
        :param times:
        """
        voteCount = defaultdict(lambda: 0)
        curMax = 0

        self.leader = [0] * len(times)
        self.times = times
        # i is cast for person[i] at time times[i]

        for i in range(len(persons)):

            voteCount[persons[i]] += 1

            # If the votecount is more than the max, we have a potential new leader.
            if voteCount[persons[i]] > curMax:
                # persons[i] is now the leader.
                curMax += 1
                self.leader[i] = persons[i]
            elif voteCount[persons[i]] == curMax:
                self.leader[i] = persons[i]
            else:
                self.leader[i] = self.leader[i - 1]

    '''
    def binSearchNextLowerValue(self, A, t):
        #A is guaranteed to be in ascending order.
        #This value is the centre value + 1 - unless our length is 1, there is always some value 1 beneath this.
        #base
        if len(A) == 1:
            return 0

        ctr = len(A) / 2

        idx = 0

        #We've found our target.  Return the index where this is.
        if A[ctr] == t:
            #return this index
            return ctr
        elif A[ctr-1] == t:
            return ctr-1

        #if A[ctr] is less than the target, we want to search the top half of the list.
        elif A[ctr] < t:
            idx = ctr + self.binSearchNextLowerValue(A[ctr:], t)            
        else:
            idx = self.binSearchNextLowerValue(A[:ctr], t)
        return idx
    '''

    def q(self, t):
        num = bisect.bisect_right(self.times, t)
        return self.leader[num - 1]
