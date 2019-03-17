"""
 In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the senate wants to make a decision about a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

    Ban one senator's right:
    A senator can make another senator lose all his rights in this and all the following rounds.
    Announce the victory:
    If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and make the decision about the change in the game.

Given a string representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party respectively. Then if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party, you need to predict which party will finally announce the victory and make the change in the Dota2 game. The output should be Radiant or Dire.

Example 1:

Input: "RD"
Output: "Radiant"
Explanation: The first senator comes from Radiant and he can just ban the next senator's right in the round 1.
And the second senator can't exercise any rights any more since his right has been banned.
And in the round 2, the first senator can just announce the victory since he is the only guy in the senate who can vote.

Example 2:

Input: "RDD"
Output: "Dire"
Explanation:
The first senator comes from Radiant and he can just ban the next senator's right in the round 1.
And the second senator can't exercise any rights anymore since his right has been banned.
And the third senator comes from Dire and he can ban the first senator's right in the round 1.
And in the round 2, the third senator can just announce the victory since he is the only guy in the senate who can vote.

Note:

    The length of the given string will in the range [1, 10,000].

"""
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        95MS
        """
        l = len(senate)
        senate_list = []
        Radiant_c = 0
        Dire_c = 0
        for i in range(l):
            senate_list.append(senate[i])
            if senate[i] == 'R':
                Radiant_c += 1
            else:
                Dire_c += 1
        start = 0
        count = 0
        while Radiant_c > 0 and Dire_c > 0:
            if senate_list[start] == 'R':
                count += 1
                if count > 0:
                    senate_list.append('R')
                else:
                    Radiant_c -= 1
            else:
                count -= 1
                if count < 0:
                    senate_list.append('D')
                else:
                    Dire_c -= 1
            start += 1
        if Dire_c == 0:
            return 'Radiant'
        else:
            return 'Dire'

    def predictPartyVictory_1(self, senate):
        """
        :type senate: str
        :rtype: str
        75MS
        """
        delta = 0
        while (len(set(senate)) > 1):
            tmp = ''
            for s in senate:
                if s == 'R':
                    if delta >= 0: tmp += 'R'
                    delta += 1
                else:
                    if delta <= 0: tmp += 'D'
                    delta -= 1
            senate = tmp
        return {'R': 'Radiant', 'D': 'Dire'}[senate[0]]
print(Solution().predictPartyVictory("D"))
print(Solution().predictPartyVictory("RDD"))
print(Solution().predictPartyVictory("DRR"))