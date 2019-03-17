"""
  Find the minimum length word from a given dictionary words, which has all the letters from the string licensePlate. Such a word is said to complete the given string licensePlate

Here, for letters we ignore case. For example, "P" on the licensePlate still matches "p" on the word.

It is guaranteed an answer exists. If there are multiple answers, return the one that occurs first in the array.

The license plate might have the same letter occurring multiple times. For example, given a licensePlate of "PP", the word "pair" does not complete the licensePlate, but the word "supper" does.

Example 1:

Input: licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
Output: "steps"
Explanation: The smallest length word that contains the letters "S", "P", "S", and "T".
Note that the answer is not "step", because the letter "s" must occur in the word twice.
Also note that we ignored case for the purposes of comparing whether a letter exists in the word.

Example 2:

Input: licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
Output: "pest"
Explanation: There are 3 smallest length words that contains the letters "s".
We return the one that occurred first.

Note:

    licensePlate will be a string with length in range [1, 7].
    licensePlate will contain digits, spaces, or letters (uppercase or lowercase).
    words will have a length in the range [10, 1000].
    Every words[i] will consist of lowercase letters, and have length in range [1, 15].

"""
class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        229ms
        """
        import collections
        dicts = collections.defaultdict(int)
        for char in licensePlate.lower():
            if char.isalpha():
                dicts[char] += 1
        print(dicts)
        min_1 = 20
        min_word = ''
        for word in words:
            a = collections.Counter(word)
            flag = True
            for key in dicts:
                if a[key] >= dicts[key]:
                    continue
                else:
                    flag = False
                    break
            # print(flag)
            if flag:
                if len(word) < min_1:
                    min_1 = len(word)
                    min_word = word

        return min_word

print(Solution().shortestCompletingWord(licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]))
licensePlate = "GrC8950"
words = ["measure","other","every","base","according","level","meeting","none","marriage","rest"]
print(Solution().shortestCompletingWord(licensePlate, words))