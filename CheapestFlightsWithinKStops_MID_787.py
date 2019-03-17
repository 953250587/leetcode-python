"""
There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and fights, together with starting city src and the destination dst, your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

Example 2:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.

Note:

    The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
    The size of flights will be in range [0, n * (n - 1) / 2].
    The format of each flight will be (src, dst, price).
    The price of each flight will be in the range [1, 10000].
    k is in the range of [0, n - 1].
    There will not be any duplicated flights or self cycles.

"""
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        315ms dfs + memory
        """
        # 把原始数据处理下，按起始点划分
        import collections
        flights_dict = collections.defaultdict(list)
        for flight in flights:
            flights_dict[flight[0]].append(flight[1:])
        # 用来记录已经计算过的位置
        memory = {}


        def dfs(K, src, price):
            # 如果该位置已经被访问过，直接输出结果
            if (src, K) in memory:
                return memory[(src, K)]
            # 不能到达的情况，记录下来
            if K < 0:
                memory[(src, K)] = float('inf')
                return float('inf')

            min_price = float('inf')
            # 遍历所有从该点出发的方案
            for next_src in flights_dict[src]:
                price += next_src[1]
                if next_src[0] == dst:
                    a = price
                else:
                    a = dfs(K - 1, next_src[0], 0) + price
                # 选择价格最少的
                min_price = min(a, min_price)
                price -= next_src[1]
            # 记录下来
            memory[(src, K)] = min_price
            return memory[(src, K)]
        ans = dfs(K, src, 0)
        return ans if ans != float('inf') else -1
        # return min(prop_result) if prop_result else -1

    def findCheapestPrice_1(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        176ms dp
        """
        import collections
        # 记录同一个终点的不同起点和价格
        flights_dict_end = collections.defaultdict(list)
        for flight in flights:
            flights_dict_end[flight[1]].append([flight[0], flight[2]])
        # 用来记录各种情况，n个站点，还剩K次，到达目的地最少价格
        dp = [[float('inf') for i in range(n)] for i in range(K + 1)]
        # 初始化能直达的
        for i in flights_dict_end[dst]:
            dp[0][i[0]] = i[1]
        # 反向推回去
        for k in range(1, K + 1):
            for pos in range(n):
                for before in flights_dict_end[pos]:
                    dp[k][before[0]] = min(dp[k][before[0]], dp[k-1][pos] + before[1])
                dp[k][pos] = min(dp[k][pos], dp[k-1][pos])
        ans = dp[K][src]
        return ans if ans != float('inf') else -1


    def findCheapestPrice_2(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        88ms heapq
        """
        import heapq, collections
        flights_dict = collections.defaultdict(list)
        for flight in flights:
            flights_dict[flight[0]].append(flight[1:])
        h = [(0, src, 0)]
        while h:
            a = heapq.heappop(h)
            if a[1] == dst:
                return a[0]
            for next_src in flights_dict[a[1]]:
                if a[2] < K + 1:
                    heapq.heappush(h, (next_src[1] + a[0], next_src[0], a[2] + 1))
        return -1

    def findCheapestPrice_3(self, n, flights, src, dst, k):
        """
        97ms
        :param n:
        :param flights:
        :param src:
        :param dst:
        :param k:
        :return:
        """
        import collections, heapq
        f = collections.defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        heap = [(0, src, k + 1)]
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
        return -1




print(Solution().findCheapestPrice_2(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, K = 1))
print(Solution().findCheapestPrice_2(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, K = 0))
print(Solution().findCheapestPrice_2(10,[[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]],6,0,7))
print(Solution().findCheapestPrice_2(17,[[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]],13,4,13))

print(Solution().findCheapestPrice_1(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, K = 1))
print(Solution().findCheapestPrice_1(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, K = 0))
print(Solution().findCheapestPrice_1(10,[[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]],6,0,7))
print(Solution().findCheapestPrice_1(17,[[0,12,28],[5,6,39],[8,6,59],[13,15,7],[13,12,38],[10,12,35],[15,3,23],[7,11,26],[9,4,65],[10,2,38],[4,7,7],[14,15,31],[2,12,44],[8,10,34],[13,6,29],[5,14,89],[11,16,13],[7,3,46],[10,15,19],[12,4,58],[13,16,11],[16,4,76],[2,0,12],[15,0,22],[16,12,13],[7,1,29],[7,14,100],[16,1,14],[9,6,74],[11,1,73],[2,11,60],[10,11,85],[2,5,49],[3,4,17],[4,9,77],[16,3,47],[15,6,78],[14,1,90],[10,5,95],[1,11,30],[11,0,37],[10,4,86],[0,8,57],[6,14,68],[16,8,3],[13,0,65],[2,13,6],[5,13,5],[8,11,31],[6,10,20],[6,2,33],[9,1,3],[14,9,58],[12,3,19],[11,2,74],[12,14,48],[16,11,100],[3,12,38],[12,13,77],[10,9,99],[15,13,98],[15,12,71],[1,4,28],[7,0,83],[3,5,100],[8,9,14],[15,11,57],[3,6,65],[1,3,45],[14,7,74],[2,10,39],[4,8,73],[13,5,77],[10,0,43],[12,9,92],[8,2,26],[1,7,7],[9,12,10],[13,11,64],[8,13,80],[6,12,74],[9,7,35],[0,15,48],[3,7,87],[16,9,42],[5,16,64],[4,5,65],[15,14,70],[12,0,13],[16,14,52],[3,10,80],[14,11,85],[15,2,77],[4,11,19],[2,7,49],[10,7,78],[14,6,84],[13,7,50],[11,6,75],[5,10,46],[13,8,43],[9,10,49],[7,12,64],[0,10,76],[5,9,77],[8,3,28],[11,9,28],[12,16,87],[12,6,24],[9,15,94],[5,7,77],[4,10,18],[7,2,11],[9,5,41]],13,4,13))
