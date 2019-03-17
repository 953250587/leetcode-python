"""
 There are n different online courses numbered from 1 to n. Each course has some duration(course length) t and closed on dth day. A course should be taken continuously for t days and must be finished before or on the dth day. You will start at the 1st day.

Given n online courses represented by pairs (t,d), your task is to find the maximal number of courses that can be taken.

Example:

Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
Output: 3
Explanation:
There're totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day.
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day.
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.

Note:

    The integer 1 <= d, t, n <= 10,000.
    You can't take two courses simultaneously.

"""


class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        401ms
        """
        import heapq
        courses = sorted(courses, key=lambda a:(a[1], a[0]))
        # print(courses)
        have_course = []
        end = 0
        ans = 0
        for course in courses:
            if end + course[0] <= course[1]:
                ans += 1
                end += course[0]
                heapq.heappush(have_course, -course[0])
                # have_course.append(course)
            else:
                if not have_course:
                    continue
                max_pos = -have_course[0]
                if course[0] < max_pos:
                    heapq.heappop(have_course)
                    heapq.heappush(have_course, -course[0])
                    end -= max_pos
                    end += course[0]
            print(have_course)
        return ans


    class Solution(object):
        def scheduleCourse(self, courses):
            """
            :type courses: List[List[int]]
            :rtype: int
            254ms
            """
            import bisect
            courses = sorted(courses, key=lambda x: x[1])
            cum = 0
            take = []

            for duration, end in courses:
                if cum + duration <= end:
                    cum += duration
                    bisect.insort(take, duration)
                else:
                    if take and duration < take[-1]:
                        cum += duration - take[-1]
                        take.pop(-1)
                        bisect.insort(take, duration)
            return len(take)
# print(Solution().scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]))
print(Solution().scheduleCourse([[5,5],[4,6],[2,6]]))
# print(Solution().scheduleCourse([[860,4825],[13,1389],[746,8823],[455,2778],[233,2069],[106,5648],[802,2969],[958,2636],[567,2439],[623,1360],[700,4206],[9,3725],[241,7381]]))
# print(Solution().scheduleCourse([[100,2],[32,50]]))
print(Solution().scheduleCourse([[7,11],[1,11],[1,3],[2,6],[5,6],[7,7],[4,8],[2,20],[1,17],[8,11]]))
