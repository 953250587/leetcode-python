"""
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.
"""
class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        132ms
        """
        dicts={}
        num=0
        for i in list1:
            dicts[i]=num
            num+=1
        num=0
        min_mark=3000
        word=[]
        for i in list2:
            if i in dicts.keys():
                if dicts[i]+num<min_mark:
                    word=[]
                    word.append(i)
                    min_mark=dicts[i]+num
                elif dicts[i]+num==min_mark:
                    word.append(i)
            num+=1
        return word


    #思路一样，写法简单
    def findRestaurant_1(self, A, B):
        Aindex = {u: i for i, u in enumerate(A)}
        best, ans = 1e9, []

        for j, v in enumerate(B):
            i = Aindex.get(v, 1e9)
            if i + j < best:
                best = i + j
                ans = [v]
            elif i + j == best:
                ans.append(v)
        return ans
print(Solution().findRestaurant(["Shogun","Tapioca Express","Burger King","KFC"]
,["KFC","Burger King","Tapioca Express","Shogun"]))

