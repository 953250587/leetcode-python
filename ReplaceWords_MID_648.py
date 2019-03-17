"""
 In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.

Example 1:

Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Note:

    The input will only have lower-case letters.
    1 <= dict words number <= 1000
    1 <= sentence words number <= 1000
    1 <= root length <= 100
    1 <= sentence words length <= 1000

"""
class Solution(object):
    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        186ms
        """
        Trie = {}
        for d in dict:
            a = Trie
            for c in d:
                if c not in a:
                    a[c] = {'isRoot': False}
                a = a[c]
            a['isRoot'] = True
        print(Trie)
        sentence_tuple = sentence.split(' ')
        result = []
        for word in sentence_tuple:
            a = Trie
            root = ''
            flag = True
            for char in word:
                if char not in a:
                    break
                else:
                    root += char
                    if a[char]['isRoot']:
                        result.append(root + ' ')
                        flag =False
                        break
                    else:
                        a = a[char]
            if flag:
                result.append(word + ' ')
        return ''.join(result)[:-1]


class Trie(object):
    def __init__(self, words):
        self.root = {}
        for word in words:
            self.add(word)

    def add(self, word):
        level = self.root
        for c in word:
            if c not in level:
                level[c] = {}
            level = level[c]
        level['stop'] = True

    def find(self, word):
        level = self.root
        for i in range(len(word)):
            if 'stop' in level:
                return word[:i]
            if word[i] in level:
                level = level[word[i]]
                i += 1
            else:
                break
        return ''

    def replaceWords(self, roots, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """

        def replace(word):
            best = word
            for r in cache[ord(word[0]) - 97]:
                if len(r) < len(best) and word.startswith(r):
                    best = r
            return best

        # cache = collections.defaultdict(list)
        cache = [[] for _ in range(26)]
        for r in roots:
            cache[ord(r[0]) - 97] += r,
        return ' '.join(map(replace, sentence.split()))


class Solution_1(object):
    def replaceWords(self, d, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        trie = Trie(d)
        words = sentence.split(' ')
        for i in range(len(words)):
            root = trie.find(words[i])
            if len(root) > 0:
                words[i] = root
        return ' '.join(words)

    def replaceWords_1(self, roots, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        89ms
        """

        def replace(word):
            best = word
            for r in cache[ord(word[0]) - 97]:
                if len(r) < len(best) and word.startswith(r):
                    best = r
            return best

        # cache = collections.defaultdict(list)
        cache = [[] for _ in range(26)]
        for r in roots:
            cache[ord(r[0]) - 97] += r,
        return ' '.join(map(replace, sentence.split()))
dict = ['c', 'ca', "cat", "batterys", "rat"]
sentence = "the cattle was rattled by the battery"
print(Solution().replaceWords(dict, sentence))

