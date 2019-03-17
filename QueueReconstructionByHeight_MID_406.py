"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

"""
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if people==[]:
            return []
        result=[]
        min_1=float('inf')
        self.sets=set()
        for p in people:
            if p[1]==0:
                min_1=min(min_1,p[0])
        people.remove([min_1,0])
        result.append([min_1,0])
        print(people)


        while len(people)>0:
            min_2 = float('inf')
            for p in people:
                if p[0]<=min_1:
                    p[1]-=1
                if p[1]==0:
                    min_2=min(min_2,p[0])
            people.remove([min_2, 0])
            result.append([min_2, 0])
            min_1=min_2
        for i in range(len(result)):
            for j in range(0,i):
                if result[j][0]>=result[i][0]:
                    result[i][1]+=1
        return result

    def reconstructQueue_1(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        if not people: return []

        # obtain everyone's info
        # key=height, value=k-value, index in original array
        peopledct, height, res = {}, [], []

        for i in range(len(people)):
            p = people[i]
            if p[0] in peopledct:
                peopledct[p[0]] += (p[1], i),
            else:
                peopledct[p[0]] = [(p[1], i)]
                height.append(p[0]),

        height.sort()  # here are different heights we have

        # sort from the tallest group
        for h in height[::-1]:
            peopledct[h].sort()
            for p in peopledct[h]:
                res.insert(p[0], people[p[1]])

        return res

    def reconstructQueue_2(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        169ms
        """
        if not people:
            return []

        ret = []
        people = sorted(people, key=lambda x: (x[0], 0 - x[1]))
        print(people)

        for p in people[::-1]:
            if not ret:
                ret.append(p)
            else:
                ret.insert(p[1], p)
            print(ret)

        return ret


p=[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

print(Solution().reconstructQueue_2(p))