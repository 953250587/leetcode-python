"""
Sometimes people repeat letters to represent extra feeling, such as "hello" -> "heeellooo", "hi" -> "hiiii".  Here, we have groups, of adjacent letters that are all the same character, and adjacent characters to the group are different.  A group is extended if that group is length 3 or more, so "e" and "o" would be extended in the first example, and "i" would be extended in the second example.  As another example, the groups of "abbcccaaaa" would be "a", "bb", "ccc", and "aaaa"; and "ccc" and "aaaa" are the extended groups of that string.

For some given string S, a query word is stretchy if it can be made to be equal to S by extending some groups.  Formally, we are allowed to repeatedly choose a group (as defined above) of characters c, and add some number of the same character c to it so that the length of the group is 3 or more.  Note that we cannot extend a group of size one like "h" to a group of size two like "hh" - all extensions must leave the group extended - ie., at least 3 characters long.

Given a list of query words, return the number of words that are stretchy.

Example:
Input:
S = "heeellooo"
words = ["hello", "hi", "helo"]
Output: 1
Explanation:
We can extend "e" and "o" in the word "hello" to get "heeellooo".
We can't extend "helo" to get "heeellooo" because the group "ll" is not extended.

Notes:

    0 <= len(S) <= 100.
    0 <= len(words) <= 100.
    0 <= len(words[i]) <= 100.
    S and all words in words consist only of lowercase letters

"""


class Solution(object):
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        65ms
        """
        def split_s(S):
            start_char = S[0]
            result = []
            count = 0
            for char in S:
                if char == start_char:
                    count += 1
                else:
                    result.append([start_char, count])
                    count = 1
                    start_char = char
            result.append([start_char, count])
            return result
        s = split_s(S)
        ans = 0
        for word in words:
            w = split_s(word)
            # print(s)
            # print(w)
            if len(w) != len(s):
                continue
            else:
                flag = True
                for i in range(len(w)):
                    if w[i][0] == s[i][0]:
                        if (s[i][1] >= 3 and w[i][1] <= s[i][1]) or (s[i][1] == w[i][1]):
                            pass
                        else:
                            # print(s[i][1], w[i][1])
                            flag = False
                            break
                    else:
                        flag = False
                        break
                if flag:
                    ans += 1
        return ans
print(Solution().expressiveWords(S = "heeellooo", words = ["hello", "hi", "helo"]))
print(Solution().expressiveWords("ggkyyyyffffbbhddddrxxsiixccqqqqkmmmiiiiiivvvyyuuujccuuuhhhhwssssnnttoyuuuussggttttfeeeebbbbeedddddqq",["ggkyyfbbhdrxxsiixccqkmmiiivvvyyujccuuuhhwsnnttoyuuussggtttfeeebbbeedddqq","ggkyyfffbbhddrxxsiixccqqkmmmiiiivvvyyuujccuuuhhhwsnnttoyuuussggtttfebeedddddqq","ggkyyyyffbbhdrxxsiixccqkmmiiiivyyujccuhhwsssnnttoyuuussggtfebeeddddqq","ggkyyfffbbhdddrxxsiixccqkmmmiiiiivyyujccuuhhwsssnnttoyuuussggtfebbeeddddqq","ggkyyyyfffbbhdddrxxsiixccqkmmmiiivvvyyuujccuhhwssnnttoyuuussggtfeeebbbeedddddqq","ggkyyyyfffbbhddrxxsiixccqqkmiiiiivyyuuujccuuuhwsnnttoyuussggtfeebbbeedddddqq","ggkyyffbbhdddrxxsiixccqqkmiiiiivvyyuujccuhwsnnttoyussggtttfeeebbbeedddqq","ggkyyyfbbhddrxxsiixccqqqkmiiivvvyyuuujccuhhwsnnttoyuussggttfebeeddddqq","ggkyyyfbbhdrxxsiixccqqqkmmiiiivvyyujccuuhwsnnttoyussggtfeebbeedddqq","ggkyyyfbbhdddrxxsiixccqkmmmiiiivyyuujccuhhhwsssnnttoyuussggttfeeebeedddqq","ggkyyyfbbhdrxxsiixccqkmmiiiiivyyujccuhhhwssnnttoyussggtttfeebeedddqq","ggkyyyfffbbhddrxxsiixccqqqkmmmiiivvyyuuujccuuhhhwssnnttoyuussggttfeebeedddddqq","ggkyyfffbbhdrxxsiixccqqkmmiiiiivvyyuuujccuuuhhwsnnttoyuussggttfeebbeedddddqq","ggkyyfffbbhdddrxxsiixccqkmiiiivyyuuujccuuhwssnnttoyuussggtfebeedddddqq","ggkyyyyfffbbhddrxxsiixccqqkmmiiivyyuujccuuuhhwssnnttoyussggtfebbbeedddddqq","ggkyyyyffbbhdrxxsiixccqkmmiiiivyyujccuhwsssnnttoyussggtttfebeeddddqq","ggkyyyfbbhddrxxsiixccqqkmiiiiivvyyuuujccuhhhwsssnnttoyuuussggttfeeebbbeedddqq","ggkyyyyffbbhdddrxxsiixccqkmmmiiiivvvyyuuujccuuhhhwssnnttoyussggtttfeeebbbeeddddqq","ggkyyyfbbhdddrxxsiixccqqqkmiiivvvyyuujccuuhhwsnnttoyuuussggtfeebbbeedddqq","ggkyyyffbbhdddrxxsiixccqqqkmiiiivvyyuuujccuuhwssnnttoyuussggttfeebbbeedddqq","ggkyyyyfbbhdddrxxsiixccqkmmmiiiiivvvyyujccuuhhwsnnttoyuuussggttfebbbeedddddqq","ggkyyyfbbhdddrxxsiixccqqqkmmiiiivvyyuujccuuhhwssnnttoyuuussggttfebeeddddqq","ggkyyyyfbbhddrxxsiixccqkmmiiivvvyyuujccuuhhhwsnnttoyussggtfeeebbbeedddqq","ggkyyyfffbbhdrxxsiixccqqkmiiiiivvyyujccuuhwsnnttoyussggtttfeebbeedddddqq","ggkyyyyfffbbhddrxxsiixccqqqkmiiiivyyuuujccuuuhhwsssnnttoyuuussggttfebbeedddqq","ggkyyffbbhddrxxsiixccqkmiiivvyyujccuuhwssnnttoyuuussggtttfeebbeedddddqq","ggkyyyfffbbhdddrxxsiixccqqkmmmiiiiivvyyuuujccuuuhhwssnnttoyussggtttfeeebbeeddddqq","ggkyyyyfbbhddrxxsiixccqkmmmiiivvvyyujccuuhhhwssnnttoyuuussggtfeeebbeedddddqq","ggkyyyyfffbbhdddrxxsiixccqkmmmiiiivyyuuujccuhhhwsssnnttoyuussggtttfeeebbeedddddqq","ggkyyyyfbbhdrxxsiixccqqkmmiiiiivyyuujccuuuhhwsnnttoyuussggttfebbeedddqq","ggkyyyfbbhdrxxsiixccqkmiiiivvyyujccuhhhwsnnttoyussggttfeeebbeedddddqq","ggkyyyfffbbhddrxxsiixccqqqkmiiivyyuujccuuuhhwssnnttoyuuussggtfeebeedddqq","ggkyyffbbhdrxxsiixccqqkmmiiiiivyyuujccuhhhwsnnttoyuuussggtfebeedddddqq","ggkyyyfffbbhddrxxsiixccqkmiiiiivvvyyuujccuuuhhwsnnttoyuuussggttfeeebbeeddddqq","ggkyyyfffbbhdddrxxsiixccqqkmmmiiiivvyyuujccuuhwssnnttoyuussggtfebeedddqq","ggkyyfbbhdddrxxsiixccqqkmiiiiivyyujccuuuhhwsssnnttoyuuussggtttfeeebeeddddqq","ggkyyyyffbbhdddrxxsiixccqqkmmiiiiivvyyuuujccuuhhhwssnnttoyuussggtfeebbbeedddddqq","ggkyyffbbhdrxxsiixccqkmmiiiivyyuujccuuhhhwssnnttoyuussggtfeebeeddddqq","ggkyyyffbbhddrxxsiixccqkmmiiiiivvyyujccuuuhhwssnnttoyuussggtttfeeebbbeeddddqq","ggkyyyfffbbhdrxxsiixccqqqkmiiiivvvyyuujccuhhhwsssnnttoyuuussggtttfebbeeddddqq","ggkyyffbbhdrxxsiixccqqkmiiiiivyyuuujccuuuhwsnnttoyuuussggttfeeebbeeddddqq","ggkyyyfbbhdrxxsiixccqqkmiiivyyujccuuuhhhwsnnttoyussggtfebbbeeddddqq","ggkyyfffbbhddrxxsiixccqqkmmiiivyyuujccuuuhhwsnnttoyuussggtttfeeebbeedddddqq","ggkyyyyfbbhdrxxsiixccqqkmmmiiiiivvvyyujccuuuhhhwssnnttoyuussggtttfeebbeeddddqq","ggkyyyffbbhdrxxsiixccqqqkmiiiivvvyyuuujccuuhhhwsssnnttoyussggtttfeebeeddddqq","ggkyyyyfbbhddrxxsiixccqkmiiiiivvvyyuuujccuuuhhwssnnttoyuussggttfeeebeeddddqq","ggkyyyyffbbhdrxxsiixccqqkmmiiivvvyyuujccuuhhhwsnnttoyuussggttfeeebbbeedddqq","ggkyyfffbbhddrxxsiixccqkmiiiiivvyyuuujccuuuhwsssnnttoyuuussggtttfebeedddddqq","ggkyyyfbbhdrxxsiixccqkmmmiiiiivvyyuuujccuuuhwssnnttoyuussggttfeeebbeedddddqq","ggkyyyffbbhdrxxsiixccqkmmiiiivyyujccuuuhhwssnnttoyussggtttfebbbeeddddqq","ggkyyyffbbhdrxxsiixccqqkmmmiiiivvvyyuujccuhwssnnttoyussggtfebeeddddqq","ggkyyyffbbhdddrxxsiixccqqkmiiivvyyuujccuuhhhwssnnttoyussggtfeebbeeddddqq","ggkyyyffbbhdrxxsiixccqqqkmmiiiivvvyyujccuhhhwsnnttoyuuussggttfebbbeedddqq","ggkyyyfbbhddrxxsiixccqqkmiiiiivvyyuujccuuhhwsssnnttoyuuussggtfebbbeeddddqq","ggkyyffbbhddrxxsiixccqqkmmiiiiivvyyujccuhhhwsssnnttoyuuussggtttfeebbbeedddddqq","ggkyyyfffbbhdrxxsiixccqqkmiiivvyyuujccuhhwsssnnttoyuussggttfeeebbeedddqq","ggkyyyfffbbhdrxxsiixccqkmmmiiiivvyyuujccuuuhwssnnttoyussggtfebbbeeddddqq","ggkyyyyffbbhdrxxsiixccqqkmiiiivvvyyuuujccuuhwsnnttoyuussggttfebbbeedddddqq","ggkyyyyffbbhddrxxsiixccqqkmmmiiiiivvyyuuujccuhwsssnnttoyuussggtfeeebbeeddddqq","ggkyyyyfbbhdddrxxsiixccqqkmmiiivyyujccuuuhhwsssnnttoyussggtfebbeedddqq","ggkyyyffbbhdrxxsiixccqkmiiiiivvyyuujccuhhwssnnttoyussggtfebeedddqq","ggkyyyffbbhdrxxsiixccqkmmiiivyyujccuuhhhwsssnnttoyuuussggtttfeeebbbeeddddqq","ggkyyyyfffbbhdddrxxsiixccqqqkmmmiiiiivvyyujccuuhhhwssnnttoyuuussggtttfebbbeedddqq","ggkyyyfbbhdddrxxsiixccqqkmmiiivvvyyujccuuuhhhwssnnttoyuussggtttfebbbeeddddqq","ggkyyyfbbhdrxxsiixccqqqkmmmiiivvyyuuujccuuhhwsssnnttoyuuussggtttfebeedddqq","ggkyyyyfbbhddrxxsiixccqkmmiiiiivvvyyuuujccuuhhwssnnttoyuuussggtfeeebeedddddqq","ggkyyyyfffbbhdddrxxsiixccqqkmiiiivvyyujccuuhhwsssnnttoyussggtfebbbeedddqq","ggkyyyffbbhdrxxsiixccqqkmmmiiivvyyuuujccuhhhwsssnnttoyussggtttfebbbeeddddqq","ggkyyyfffbbhdddrxxsiixccqqkmmmiiiiivvvyyuuujccuuuhhwsnnttoyuussggttfeebeedddddqq","ggkyyyyfffbbhdddrxxsiixccqqqkmmmiiiivvyyuuujccuuuhhhwsssnnttoyussggtfeebbbeedddddqq","ggkyyyfbbhdddrxxsiixccqkmiiiiivyyuuujccuhhhwsnnttoyuussggtttfeebeedddqq","ggkyyyfbbhdrxxsiixccqqqkmmmiiiiivyyujccuhhwsnnttoyuussggttfeebbeedddqq","ggkyyyyffbbhdrxxsiixccqqqkmmiiivvyyujccuhhhwssnnttoyussggttfeeebbbeedddddqq","ggkyyyfffbbhdrxxsiixccqqqkmiiiiivyyujccuhhwsssnnttoyuuussggtfeebbbeeddddqq","ggkyyyffbbhdrxxsiixccqqkmiiiivvyyuuujccuhhhwssnnttoyussggttfeeebbbeedddqq","ggkyyyyffbbhdrxxsiixccqkmiiiiivvyyuujccuhhwssnnttoyuussggtfeeebeedddqq","ggkyyyfbbhdddrxxsiixccqkmmmiiivvyyujccuuhhhwsssnnttoyuussggtttfeebeedddddqq","ggkyyyyfffbbhdddrxxsiixccqqqkmmmiiiiivvvyyuuujccuuhwssnnttoyuuussggtfeeebbeedddddqq","ggkyyfbbhdrxxsiixccqkmiiiivvyyujccuuuhhhwssnnttoyuussggttfebbeedddqq","ggkyyyfbbhddrxxsiixccqqqkmmiiiivyyuujccuuhhwsnnttoyuussggttfebbeedddddqq","ggkyyyyfbbhdddrxxsiixccqkmmiiivyyujccuhwsssnnttoyussggttfeebbbeedddqq","ggkyyyyfbbhdrxxsiixccqkmiiiiivvvyyuuujccuuuhhwsnnttoyuuussggtfeebeeddddqq","ggkyyffbbhddrxxsiixccqqkmmiiiivyyuujccuuhhwsssnnttoyuussggtttfeeebbeedddqq","ggkyyyfffbbhddrxxsiixccqqqkmmiiivvvyyuujccuhhwsnnttoyuussggttfebbbeeddddqq","ggkyyfffbbhdrxxsiixccqkmmmiiivvvyyuuujccuuuhwsssnnttoyussggttfeeebeedddddqq","ggkyyyyffbbhdrxxsiixccqqqkmmiiiiivvyyuuujccuhhwsnnttoyuuussggtttfeeebbeedddqq","ggkyyyyfffbbhdrxxsiixccqkmmiiivvvyyuujccuhhwsssnnttoyuuussggttfeebbeedddddqq","ggkyyyyfffbbhdddrxxsiixccqqqkmiiivvyyuuujccuuhhhwssnnttoyuuussggttfebbbeedddddqq","ggkyyffbbhdrxxsiixccqqqkmmmiiiiivvvyyujccuuuhwsssnnttoyuussggtttfeeebbbeeddddqq","ggkyyyyfffbbhdddrxxsiixccqkmmmiiiiivyyujccuuuhwsnnttoyuuussggtttfeeebeedddddqq","ggkyyfffbbhdrxxsiixccqkmmmiiiiivvyyuujccuuuhwsssnnttoyussggtfebbeedddddqq","ggkyyyyfbbhddrxxsiixccqqqkmiiivyyuujccuuhhhwssnnttoyussggttfeeebbbeedddddqq","ggkyyffbbhddrxxsiixccqkmmiiivvvyyuuujccuuhhwsssnnttoyuuussggtfeeebbeedddddqq","ggkyyffbbhdddrxxsiixccqkmiiiivvvyyuujccuuhhhwsssnnttoyuuussggttfebbeedddqq","ggkyyyyffbbhdrxxsiixccqkmmmiiiiivyyuujccuuuhwsnnttoyuuussggtttfebeeddddqq","ggkyyffbbhddrxxsiixccqkmmmiiiivyyuuujccuuhhhwsssnnttoyuuussggtfeeebeedddqq","ggkyyyyfbbhdrxxsiixccqkmmmiiivyyuujccuhwsnnttoyuuussggtttfeeebbeeddddqq","ggkyyyyfffbbhdddrxxsiixccqqkmiiivvyyuujccuhhhwsnnttoyuuussggttfeeebbeedddqq","ggkyyyyfffbbhdddrxxsiixccqqkmmmiiivvyyuuujccuuuhwssnnttoyuussggtttfeebeedddqq","ggkyyyyfffbbhdddrxxsiixccqkmiiiiivyyuujccuuuhhwssnnttoyussggtttfeeebeeddddqq"]))