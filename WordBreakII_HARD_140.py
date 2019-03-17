"""
 Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        69ms
        """
        self.s = s
        self.l = len(s)
        self.set = set(wordDict)
        self.dict = {}
        def dfs(start, count):
            if start >= self.l:
                return ['']
            if start in self.dict:
                return self.dict[start]
            result = []
            for i in range(start + 1, self.l + 1):
                key = self.s[start: i]
                if key in self.set:
                    a = dfs(i, count + 1)
                    if a:
                        for b in a:
                            result.append(key + ' ' + b)

            if result == []:
                self.dict[start] = False
            else:
                self.dict[start] = result
            return result
        a = dfs(0, 0)
        for i in range(len(a)):
            a[i] = a[i][:-1]
        return a

    def wordBreak_1(self, s, wd):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        43ms
        """
        if not wd: return []
        wd = set(wd)
        lens = set(len(w) for w in wd)
        self.dic = {0: ['']}

        def search(i):
            if i not in self.dic:
                self.dic[i] = [rest + (rest and ' ') + s[i - span: i]
                               for span in lens if s[i - span: i] in wd for rest in search(i - span)]
            return self.dic[i]

        return search(len(s))
s = "catsanddog"
dict = ["cat", "cats", "and", "sand", "dog"]
print(Solution().wordBreak(s, dict))

s = "abcd"
dict = ["a","abc","b","cd"]
print(Solution().wordBreak(s, dict))


