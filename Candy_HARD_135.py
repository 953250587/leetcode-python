"""
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
"""
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if len(ratings)<=1:
            return len(ratings)
        self.num=[1]
        temp = ratings[0]
        self.ratings=[temp]
        for rating in ratings[1:]:
            if temp==rating:
                self.num[-1]+=1
            else:
                temp=rating
                self.ratings.append(rating)
                self.num.append(1)
        if len(self.ratings)<=1:
            return len(ratings)
        print(len(self.ratings),len(ratings))
        # print(self.ratings)
        # print(self.num)

        self.lows=[]
        self.highs=[]
        self.point=set()
        l=len(self.ratings)
        self.price = [-1]*l
        if self.ratings[0]>self.ratings[1]:
            self.highs.append(0)
        else:
            self.lows.append(0)
            self.price[0] = 1
        for i in range(1,l-1):
            if self.ratings[i-1]<self.ratings[i] and self.ratings[i+1]<self.ratings[i]:
                self.highs.append(i)
                self.point.add(i)
            elif self.ratings[i-1]>self.ratings[i] and self.ratings[i+1]>self.ratings[i]:
                self.lows.append(i)
                self.price[i] = 1
                self.point.add(i)
        if self.ratings[-2]<self.ratings[-1]:
            self.highs.append(l-1)
        else:
            self.lows.append(l-1)
            self.price[l-1] = 1
        # print(self.highs)
        # print(self.lows)
        print(self.price)

        l_h=len(self.highs)
        l_l=len(self.lows)
        if self.lows[0]<self.highs[0]:
            for i in range(l_h):
                if i+1<l_l:
                    a=self.lows[i+1]-self.highs[i]
                else:
                    a=0
                b=self.highs[i]-self.lows[i]
                if self.num[self.highs[i]]<2 or self.highs[i]==0 or self.highs[i]==l-1:
                    self.price[self.highs[i]]=max(b,a)+1
                else:
                    self.price[self.highs[i]]=(a+b)/2.0+1
        elif self.lows[0]>self.highs[0]:
            for i in range(l_h):
                if i-1>=0:
                    a=self.highs[i]-self.lows[i-1]
                else:
                    a=0
                if i<l_l:
                    b=self.lows[i]-self.highs[i]
                else:
                    b=0
                if self.num[self.highs[i]] < 2 or self.highs[i] == 0 or self.highs[i] == l-1:
                    self.price[self.highs[i]]=max(a,b)+1
                else:
                    self.price[self.highs[i]]=(a+b)/2.0+1
        # print(self.price)
        for i in self.lows:
            start=i-1
            while start>=0 and self.price[start]==-1:
                self.price[start]=self.price[start+1]+1
                start-=1
            start=i+1
            while start<l and self.price[start] == -1:
                self.price[start] = self.price[start - 1] + 1
                start += 1
        print(self.num)
        print(self.price)
        self.max_1=0
        for i in range(l):
            if self.num[i]>=2 and i in self.point:
                self.max_1+=(self.price[i]*2+self.num[i]-2)
            elif self.num[i]>=2:
                self.max_1+=self.price[i]+self.num[i]-1
            else:
                self.max_1+=self.price[i]
        return int(self.max_1)

    def candy_1(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        176ms
        """
        self.ratings=ratings
        if len(ratings) <= 1:
            return len(ratings)

        self.lows = []
        self.highs = []
        self.point = set()
        l = len(self.ratings)
        self.price = [-1] * l
        if self.ratings[0] > self.ratings[1]:
            self.highs.append(0)
        else:
            self.lows.append(0)
            self.price[0] = 1
        for i in range(1, l - 1):
            if (self.ratings[i - 1] <= self.ratings[i] and self.ratings[i + 1] < self.ratings[i])\
                    or (self.ratings[i - 1] < self.ratings[i] and self.ratings[i + 1] <= self.ratings[i]):
                self.highs.append(i)
                self.point.add(i)
            elif (self.ratings[i - 1] >= self.ratings[i] and self.ratings[i + 1] >= self.ratings[i]):
                self.lows.append(i)
                self.price[i] = 1
                self.point.add(i)
        if self.ratings[-2] < self.ratings[-1]:
            self.highs.append(l - 1)
        else:
            self.lows.append(l - 1)
            self.price[l - 1] = 1
        print(self.highs)
        print(self.lows)
        print(self.price)
        self.dicts=[]
        l_h=0
        l_l=0
        count=0
        while l_h<len(self.highs) or l_l<len(self.lows):
            if l_h<len(self.highs) and  l_l<len(self.lows) and self.highs[l_h]<self.lows[l_l]:
                self.dicts.append(self.highs[l_h]+1)
                l_h+=1
            elif l_h < len(self.highs) and l_l < len(self.lows) and self.highs[l_h] > self.lows[l_l]:
                self.dicts.append(-self.lows[l_l]-1)
                l_l+=1
            elif l_h<len(self.highs):
                self.dicts.append(self.highs[l_h]+1)
                l_h+=1
            else:
                self.dicts.append(-self.lows[l_l]-1)
                l_l+=1
            count+=1
        print(l_h,l_l)
        print(self.dicts)
        c=len(self.dicts)
        for i in range(c):
            if i-1>=0 and i+1<c:
                if self.dicts[i-1]<0 and self.dicts[i]>0 and self.dicts[i+1]<0:
                    self.price[self.dicts[i]-1]=max(self.dicts[i]+self.dicts[i-1],-(self.dicts[i]+self.dicts[i+1]))+1
                elif self.dicts[i-1]<0 and self.dicts[i]>0:
                    self.price[self.dicts[i]-1]=self.dicts[i]+self.dicts[i-1]+1
                elif self.dicts[i]>0 and self.dicts[i+1]<0:
                    self.price[self.dicts[i]-1] = -(self.dicts[i]+self.dicts[i+1])+1
            elif i==0:
                if self.dicts[i]>0 and self.dicts[i+1]<0:
                    self.price[self.dicts[i]-1] = -(self.dicts[i] + self.dicts[i + 1])+1
            else:
                if self.dicts[i - 1] < 0 and self.dicts[i] > 0:
                    self.price[self.dicts[i]-1] = self.dicts[i] + self.dicts[i - 1]+1
        print(self.price)
        for i in self.lows:
            start=i-1
            while start>=0 and self.price[start]==-1:
                self.price[start]=self.price[start+1]+1
                start-=1
            start=i+1
            while start<l and self.price[start] == -1:
                self.price[start] = self.price[start - 1] + 1
                start += 1
        print(self.price)
        return sum(self.price)

    def candy_2(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        65ms
        """
        if len(ratings) == 0:
            return 0
        candy = [1]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                candy.append(candy[i - 1] + 1)
            else:
                candy.append(1)
        for i in range(len(ratings) - 1)[::-1]:
            if ratings[i] > ratings[i + 1] and candy[i] <= candy[i + 1]:
                candy[i] = candy[i + 1] + 1
            # if ratings[i] > ratings[i + 1]:
            #     candy[i] = max(candy[i], candy[i + 1] + 1)
        result = sum(candy)
        return result

print(Solution().candy_1([2,1]))
# print(Solution().candy([0,1,2,1,0,-1]))
# print(Solution().candy([2,2]))
# print(Solution().candy([1,2,4,4,3]))
# print(Solution().candy_1([2,2,1,1,1,2,2]))
# print(Solution().candy_1([2,1,1,2,1,1,2,2,3,3,2,3,2,1,0,1]))
# print(Solution().candy_1([2,1,2,1,1,2,2,3,3,2,3,2,1,0,1]))
# print(Solution().candy([1,2,3,4,5]))
# print(Solution().candy([5,4,3,2,1]))
# print(Solution().candy_1([58,21,72,77,48,9,38,71,68,77,82,47,25,94,89,54,26,54,54,99,64,71,76,63,81,82,60,64,29,51,87,87,72,12,16,20,21,54,43,41,83,77,41,61,72,82,15,50,36,69,49,53,92,77,16,73,12,28,37,41,79,25,80,3,37,48,23,10,55,19,51,38,96,92,99,68,75,14,18,63,35,19,68,28,49,36,53,61,64,91,2,43,68,34,46,57,82,22,67,89]))
