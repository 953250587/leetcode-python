"""
We have a list of bus routes. Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7], this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop T. Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1 if it is not possible.

Example:
Input:
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2
Explanation:
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.

Note:

    1 <= routes.length <= 500.
    1 <= routes[i].length <= 500.
    0 <= routes[i][j] < 10 ^ 6.

"""


class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        1099ms
        """
        import collections
        stop2bus = collections.defaultdict(list)
        for i, route in enumerate(routes):
            for bus_stop in route:
                stop2bus[bus_stop].append(i)
        def bfs(S, T):
            ans = 0
            used_bus = set()
            # 查找这个bus列表能到达的stop有哪些
            def bus_all_stop(bus_list):
                stops = []
                for bus in bus_list:
                    stops.extend(routes[bus])
                return set(stops)
            # 起始站能乘坐的公交
            start_bus_list = stop2bus[S]
            while start_bus_list:
                if S == T:
                    return 0
                ans += 1
                # 起始站能乘坐的公交能到达的站点
                can_arrive_stop = bus_all_stop(start_bus_list)
                # 如果能到达目的地，返回乘车次数
                if T in can_arrive_stop:
                    return ans
                # 如果不能，说明这些公交车不能到达，记录之后不会重复考虑
                for bus in start_bus_list:
                    used_bus.add(bus)
                # 下一次考虑能乘坐的公交车
                next_bus_list = []
                # 考虑当前公交车能到达的车站可以转乘哪些公交车
                for stop in can_arrive_stop:
                    # 只考虑之前没去过的车站就好了
                    for bus in stop2bus[stop]:
                        if bus not in used_bus:
                            next_bus_list.append(bus)
                start_bus_list = next_bus_list
            return -1
        return bfs(S, T)

    def numBusesToDestination_1(self, routes, S, T):
        """
        248ms
        :param routes:
        :param S:
        :param T:
        :return:
        """
        import collections
        to_routes = collections.defaultdict(set)
        for i, route in enumerate(routes):
            for j in route: to_routes[j].add(i)
        bfs = [(S, 0)]
        seen = set([S])
        for stop, bus in bfs:
            if stop == T: return bus
            for route_i in to_routes[stop]:
                for next_stop in routes[route_i]:
                    if next_stop not in seen:
                        bfs.append((next_stop, bus + 1))
                        seen.add(next_stop)
                routes[route_i] = []
        return -1
print(Solution().numBusesToDestination(routes = [[1, 2, 7], [3, 6, 7]],S = 1,T = 6))
print(Solution().numBusesToDestination([[1,7],[3,5]],5,5))
