"""
Your car starts at position 0 and speed +1 on an infinite number line.  (Your car can go into negative positions.)

Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).

When you get an instruction "A", your car does the following: position += speed, speed *= 2.

When you get an instruction "R", your car does the following: if your speed is positive then speed = -1 , otherwise speed = 1.  (Your position stays the same.)

For example, after commands "AAR", your car goes to positions 0->1->3->3, and your speed goes to 1->2->4->-1.

Now for some target position, say the length of the shortest sequence of instructions to get there.

Example 1:
Input:
target = 3
Output: 2
Explanation:
The shortest instruction sequence is "AA".
Your position goes from 0->1->3.

Example 2:
Input:
target = 6
Output: 5
Explanation:
The shortest instruction sequence is "AAARA".
Your position goes from 0->1->3->7->7->6.



Note:

    1 <= target <= 10000.
"""
class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        3704 ms
        """
        used = set()
        h = [(0, 1)]
        ans = 0
        while h:
            next_h = []
            for i in h:
                if i[0] == target:
                    return ans
                next_h.append((i[0] + i[1], 2 * i[1]))
                a = (i[0], 1 if i[1] < 0 else -1)
                if a not in used:
                    used.add(a)
                    next_h.append(a)

            ans += 1
            h = next_h

        return -1

    def racecar_1(self, target):
        """
        :type target: int
        :rtype: int
        2753ms
        """
        if target == 0:
            return 0
        q = [(0, 1)]
        visited = set([(0, 1)])
        cnt = 0
        while q:
            new_q = []
            cnt += 1
            for pos, sp in q:
                p1, s1 = pos + sp, sp * 2
                if p1 == target:
                    return cnt
                p2, s2 = pos, -1 if sp > 0 else 1

                # If we remember every position and speed pair, we get Memory Limit Exceed
                # The most annoying part is continuous R, so only remember situations with speed 1 and -1
                new_q.append((p1, s1))
                if (p2, s2) not in visited:
                    visited.add((p2, s2))
                    new_q.append((p2, s2))
            q = new_q
        return -1

    def racecar_2(self, target):
        """
        1786ms
        :param target:
        :return:
        """
        import heapq
        K = target.bit_length() + 1
        barrier = 1 << K
        pq = [(0, target)]
        dist = [float('inf')] * (2 * barrier + 1)
        dist[target] = 0

        while pq:
            steps, targ = heapq.heappop(pq)
            if dist[targ] > steps: continue

            for k in range(K + 1):
                walk = (1 << k) - 1
                steps2, targ2 = steps + k + 1, walk - targ
                if walk == targ: steps2 -= 1  # No "R" command if already exact

                if abs(targ2) <= barrier and steps2 < dist[targ2]:
                    heapq.heappush(pq, (steps2, targ2))
                    dist[targ2] = steps2

        return dist[0]

    def __init__(self):
        self.dp = {0: 0}

    def racecar_3(self, t):
        """
        117ms
        :param t:
        :return:
        """
        if t in self.dp: return self.dp[t]
        n = t.bit_length()
        if 2 ** n - 1 == t:
            self.dp[t] = n
        else:
            self.dp[t] = self.racecar_3(2 ** n - 1 - t) + n + 1
            for m in range(n - 1):
                self.dp[t] = min(self.dp[t], self.racecar_3(t - 2 ** (n - 1) + 2 ** m) + n + m + 1)
        return self.dp[t]
# print(Solution().racecar(target = 3))
# print(Solution().racecar(target = 6))
print(Solution().racecar(target = 931))
print(Solution().racecar(5478))


