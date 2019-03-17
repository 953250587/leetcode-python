"""
Given a list of airline tickets represented by pairs of departure and arrival airports [from, to], reconstruct the itinerary in order. All of the tickets belong to a man who departs from JFK. Thus, the itinerary must begin with JFK.

Note:

    If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
    All airports are represented by three capital letters (IATA code).
    You may assume all tickets form at least one valid itinerary.

Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].

Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].
Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"]. But it is larger in lexical order.
"""
class Solution(object):
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        162ms
        """
        self.dicts={}
        self.sets=set()
        self.l=len(tickets)

        for ticket in tickets:
            self.sets.add(ticket[0])
            self.sets.add(ticket[1])

            if ticket[0] not in self.dicts.keys():
                self.dicts[ticket[0]]=[[],[]]
            self.dicts[ticket[0]][0].append(ticket[1])
            self.dicts[ticket[0]][1].append(1)

        start='JFK'

        for key in self.dicts.keys():
            self.dicts[key][0].sort()

        result=[start]
        count=1

        def dfs(count,start):
            # print(1,start)
            if start in self.dicts.keys():
                dicts = self.dicts[start]
            else:
                dicts=[]
            if dicts==[] and count<=self.l:
                return False
            if count>self.l:
                return True
            # print(2,dicts)
            # print(count)

            for pos in range(len(dicts[0])):
                # print(result)
                # print(dicts)
                if dicts[1][pos] == 1:
                    dicts[1][pos] = 0
                    start = dicts[0][pos]
                    result.append(start)
                    count += 1

                    if dfs(count, start):
                        return True

                    dicts[1][pos] = 1
                    result.pop()
                    count -= 1
            return False
        dfs(count,start)
        return result

    def findItinerary_1(self, tickets):

        """
        :type tickets: List[List[str]]
                  :rtype: List[str]
                  92ms
        """
        import collections
        targets = collections.defaultdict(list)  # dict (key,list)
        for a, b in sorted(tickets)[::-1]:  # sort dict, when key is the same, sort the items in the list
            targets[a].append(b)  # a is departure, b is arrival

        route, stack = [], ['JFK']

        while stack:
            while targets[stack[-1]]:  # search from the last one of the stack
                stack.append(
                    targets[stack[-1]].pop())  # pop the last one of the list, which has the smaller lexical order
            route.append(stack.pop())

        return route[::-1]


        # print(self.dicts)
        # print(self.dicts['JFK'].pop())
        # print(self.dicts_count, self.dicts)
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
# tickets=[["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
# tickets=[["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]
tickets=[["JFK","ATL"],["ATL","JFK"]]
print(Solution().findItinerary(tickets))
