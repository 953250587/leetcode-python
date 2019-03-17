"""
Some people will make friend requests. The list of their ages is given and ages[i] is the age of the ith person.

Person A will NOT friend request person B (B != A) if any of the following conditions are true:

    age[B] <= 0.5 * age[A] + 7
    age[B] > age[A]
    age[B] > 100 && age[A] < 100

Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.  Also, people will not friend request themselves.

How many total friend requests are made?

Example 1:

Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.

Example 2:

Input: [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.

Example 3:

Input: [20,30,100,110,120]
Output:
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.



Notes:

    1 <= ages.length <= 20000.
    1 <= ages[i] <= 120.

"""


class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        202ms
        """
        ans = 0
        import bisect
        ages = sorted(ages)
        i = 0
        while i < len(ages):
            age = ages[i]
            count = 1
            while i + 1 < len(ages) and ages[i + 1] == age:
                i += 1
                count += 1
            low = 0.5 * age + 7
            pos = bisect.bisect_right(ages[0: i], low)
            ans += (i - pos) * count
            i += 1
        return ans

    def numFriendRequests_1(self, ages):
        """
        433ms
        :param ages:
        :return:
        """
        import collections
        def request(a, b):
            return not (b <= 0.5 * a + 7 or b > a or b > 100 and a < 100)

        c = collections.Counter(ages)
        return sum(request(a, b) * c[a] * (c[b] - (a == b)) for a in c for b in c)
print(Solution().numFriendRequests([16,16]))
print(Solution().numFriendRequests([16,16,16]))
print(Solution().numFriendRequests([16,17,18]))
print(Solution().numFriendRequests([20,30,100,110,120]))
