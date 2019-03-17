"""
Given a list accounts, each element accounts[i] is a list of strings, where the first element accounts[i][0] is a name, and the rest of the elements are emails representing emails of the account.

Now, we would like to merge these accounts. Two accounts definitely belong to the same person if there is some email that is common to both accounts. Note that even if two accounts have the same name, they may belong to different people as people could have the same name. A person can have any number of accounts initially, but all of their accounts definitely have the same name.

After merging the accounts, return the accounts in the following format: the first element of each account is the name, and the rest of the elements are emails in sorted order. The accounts themselves can be returned in any order.

Example 1:
Input:
accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
Explanation:
The first and third John's are the same person as they have the common email "johnsmith@mail.com".
The second John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'],
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Note:

The length of accounts will be in the range [1, 1000].
The length of accounts[i] will be in the range [1, 10].
The length of accounts[i][j] will be in the range [1, 30].
"""


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        579ms
        """
        import collections
        self.dict = collections.defaultdict(list)
        for account in accounts:
            self.dict[account[0]].append(list(set(account[1:])))
        print(self.dict)

        def build_graph(lists):
            for i in lists:
                self.sets_all.add(i)
                for j in lists:
                    if i != j:
                        self.dict_graph[i].add(j)
                        self.dict_graph[j].add(i)
        def dfs(sets):
            for i in list(sets):
                if i in self.sets:
                    pass
                else:
                    self.sets.add(i)
                    self.sets_all.remove(i)
                    dfs(self.dict_graph[i])

        result = []
        for key in self.dict:
            self.dict_graph = collections.defaultdict(set)
            a = self.dict[key]
            self.sets_all = set()
            for account in a:
                build_graph(account)
            print(self.dict_graph)
            print(self.sets_all)
            self.sets = set()
            for account in a:
                print(account)
                if account[0] in self.sets_all:
                    self.sets = set()
                    dfs(set(account))
                    print(self.sets)
                    result.append([key] + sorted(list(self.sets)))


        return result

    def accountsMerge_1(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        339ms
        """
        import collections
        if len(accounts) < 2:
            return []
        graph = collections.defaultdict(list)
        visited = [False] * len(accounts)

        for idx, account in enumerate(accounts):
            for i in range(1, len(account)):
                graph[account[i]].append(idx)

        res = []
        for i in range(len(accounts)):
            if not visited[i]:
                emails = set()
                for j in range(1, len(accounts[i])):
                    emails.add(accounts[i][j])
                visited[i] = True
                self.dfs(i, visited, accounts, emails, graph)
                tmp = [accounts[i][0]]
                tmp.extend(sorted(emails))
                res.append(tmp)

        return res

    def dfs(self, i, visited, accounts, emails, graph):
        cur = accounts[i]
        for i in range(1, len(cur)):
            emails.add(cur[i])
            for neg in graph[cur[i]]:
                if not visited[neg]:
                    visited[neg] = True
                    self.dfs(neg, visited, accounts, emails, graph)
        return

    def accountsMerge_3(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        259ms
        """
        n = len(accounts)
        par_map = [-1] * n

        em_2_id = {}
        for i in range(n):
            account = accounts[i]
            for email in account[1:]:
                if email not in em_2_id:
                    em_2_id[email] = i
                else:
                    id1 = em_2_id[email]
                    id2 = i
                    while par_map[id1] != -1:
                        id1 = par_map[id1]
                    while par_map[id2] != -1:
                        id2 = par_map[id2]
                    if id1 != id2:
                        id1, id2 = min(id1, id2), max(id1, id2)
                        par_map[id2] = id1

        ret = {}
        for email in em_2_id.keys():
            id_ = em_2_id[email]
            while par_map[id_] != -1:
                id_ = par_map[id_]
            if id_ not in ret:
                ret[id_] = []
            ret[id_].append(email)

        result = []
        for k in ret.keys():
            tmp = []
            tmp.append(accounts[k][0])
            ret[k].sort()
            for item in ret[k]:
                tmp.append(item)
            result.append(tmp)

        # finally tackle empty accounts
        for account in accounts:
            if len(account) == 1:
                result.append(account)
        return result


# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
#             ["John", "johnnybravo@mail.com"],
#             ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
#             ["Mary", "mary@mail.com"]]
# print(Solution().accountsMerge(accounts))
#
#
# accounts = [["David","David0@m.co","David1@m.co"],
#             ["David","David3@m.co","David4@m.co"],
#             ["David","David4@m.co","David5@m.co"],
#             ["David","David2@m.co","David3@m.co"],
#             ["David","David1@m.co","David2@m.co"]]
# print(Solution().accountsMerge(accounts))

accounts = [["David","David5@m.co","David8@m.co"],
            ["David","David1@m.co","David1@m.co","David8@m.co"],
            ["David","David0@m.co","David0@m.co","David5@m.co"]]
print(Solution().accountsMerge(accounts))