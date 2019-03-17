"""
 In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring", and use the dial to spell a specific keyword in order to open the door.

Given a string ring, which represents the code engraved on the outer ring and another string key, which represents the keyword needs to be spelled. You need to find the minimum number of steps in order to spell all the characters in the keyword.
Initially, the first character of the ring is aligned at 12:00 direction. You need to spell all the characters in the string key one by one by rotating the ring clockwise or anticlockwise to make each character of the string key aligned at 12:00 direction and then by pressing the center button.
At the stage of rotating the ring to spell the key character key[i]:

    You can rotate the ring clockwise or anticlockwise one place, which counts as 1 step. The final purpose of the rotation is to align one of the string ring's characters at the 12:00 direction, where this character must equal to the character key[i].
    If the character key[i] has been aligned at the 12:00 direction, you need to press the center button to spell, which also counts as 1 step. After the pressing, you could begin to spell the next character in the key (next stage), otherwise, you've finished all the spelling.

Example:

Input: ring = "godding", key = "gd"
Output: 4
Explanation:
 For the first key character 'g', since it is already in place, we just need 1 step to spell this character.
 For the second key character 'd', we need to rotate the ring "godding" anticlockwise by two steps to make it become "ddinggo".
 Also, we need 1 more step for spelling.
 So the final output is 4.

Note:

    Length of both ring and key will be in range 1 to 100.
    There are only lowercase letters in both strings and might be some duplcate characters in both strings.
    It's guaranteed that string key could always be spelled by rotating the string ring.

"""
class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        284ms
        """
        import collections
        dicts = collections.defaultdict(set)
        for i, char in enumerate(ring):
            dicts[char].add(i)
        recommend = {}
        l = len(ring)
        L = len(key)
        def dfs(pos, count):
            if (pos, count) in recommend:
                return recommend[(pos, count)]
            if count >= L:
                return 0
            cur_key = key[count]
            min_need_num = float('inf')
            for posibility_pos in dicts[cur_key]:
                a = abs(pos - posibility_pos)
                num = dfs(posibility_pos, count + 1) + min(a, l - a)
                min_need_num = min(min_need_num, num)
            recommend[(pos, count)] = min_need_num
            return min_need_num

        return dfs(0, 0) + L

    def findRotateSteps_1(self, ring, key):
        """
        168ms
        :param ring:
        :param key:
        :return:
        """
        import collections
        rl = len(ring)
        d = collections.defaultdict(list)
        for i, c in enumerate(ring):
            d[c].append(i)
        prev = [(1 + min(i, rl - i), i) for i in d[key[0]]]
        for k in key[1:]:
            cur = []
            for i in d[k]:
                steps = 1 + min(s + min(abs(i - i2), rl - abs(i - i2)) for s, i2 in prev)
                cur.append((steps, i))
            prev = cur
        return min(x[0] for x in prev)
print(Solution().findRotateSteps(ring = "godding", key = "gd"))
print(Solution().findRotateSteps("ababcab","acbaacba"))



