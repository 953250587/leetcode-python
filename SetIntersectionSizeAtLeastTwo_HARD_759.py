"""
 An integer interval [a, b] (for integers a < b) is a set of all consecutive integers from a to b, including a and b.

Find the minimum size of a set S such that for every integer interval A in intervals, the intersection of S with A has size at least 2.

Example 1:

Input: intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
Output: 3
Explanation:
Consider the set S = {2, 3, 4}.  For each interval, there are at least 2 elements from S in the interval.
Also, there isn't a smaller size set that fulfills the above condition.
Thus, we output the size of this set, which is 3.

Example 2:

Input: intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
Output: 5
Explanation:
An example of a minimum sized set is {1, 2, 3, 4, 5}.

Note:

    intervals will have length in range [1, 3000].
    intervals[i] will have length 2, representing some integer interval.
    intervals[i][j] will be an integer in [0, 10^8].

"""
class Solution(object):
    def intersectionSizeTwo(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        89ms
        """
        intervals = sorted(intervals, key= lambda a:(a[-1], a[0]))
        print(intervals)
        end = intervals[0][-1]
        count = 2
        sets = set()
        sets.add(end)
        sets.add(end - 1)
        mid = end - 1
        for interval in intervals[1:]:
            # print(sets, mid, interval)
            if interval[0] <= mid:
                continue
            elif interval[0] > mid and interval[0] <= end:
                mid = end
                end = interval[1]
                if end not in sets:
                    sets.add(end)
                else:
                    sets.add(end - 1)
                    mid = end - 1
                count += 1
            # elif interval[0] <= end:
            #     mid = end
            #     end = interval[1]
            #     sets.add(end)
            #     count += 1
            else:
                end = interval[1]
                sets.add(end)
                sets.add(end - 1)
                mid = end - 1
                count += 2
        print(sets)

        return count

print(Solution().intersectionSizeTwo([[1, 3], [1, 4], [2, 5], [3, 5]]))
print(Solution().intersectionSizeTwo([[1, 2], [2, 3], [2, 4], [4, 5]]))
print(Solution().intersectionSizeTwo([[8,9],[4,21],[3,19],[5,9],[1,5]]))
print(Solution().intersectionSizeTwo([[12,19],[18,25],[4,6],[19,24],[19,22]]))
print(Solution().intersectionSizeTwo([[4,7],[5,8],[7,9],[2,6],[0,1],[1,4],[1,9],[0,5],[5,10],[7,8]]))
print(Solution().intersectionSizeTwo([[16,18],[11,18],[15,23],[1,16],[10,16],[6,19],[18,20],[7,19],[10,11],[11,23],[6,7],[23,25],[1,3],[7,12],[1,13],[23,25],[10,22],[23,25],[0,19],[0,13],[7,12],[14,19],[8,17],[7,23],[4,24]]))
print(Solution().intersectionSizeTwo([[0,9],[0,2],[2,7],[8,10],[6,7],[3,7],[1,9],[0,9],[3,9],[3,9]]))