"""
 Implement a MyCalendarThree class to store your events. A new event can always be added.

Your class will have one method, book(int start, int end). Formally, this represents a booking on the half open interval [start, end), the range of real numbers x such that start <= x < end.

A K-booking happens when K events have some non-empty intersection (ie., there is some time that is common to all K events.)

For each call to the method MyCalendar.book, return an integer K representing the largest integer such that there exists a K-booking in the calendar.
Your class will be called like this: MyCalendarThree cal = new MyCalendarThree(); MyCalendarThree.book(start, end)

Example 1:

MyCalendarThree();
MyCalendarThree.book(10, 20); // returns 1
MyCalendarThree.book(50, 60); // returns 1
MyCalendarThree.book(10, 40); // returns 2
MyCalendarThree.book(5, 15); // returns 3
MyCalendarThree.book(5, 10); // returns 3
MyCalendarThree.book(25, 55); // returns 3
Explanation:
The first two events can be booked and are disjoint, so the maximum K-booking is a 1-booking.
The third event [10, 40) intersects the first event, and the maximum K-booking is a 2-booking.
The remaining events cause the maximum K-booking to be only a 3-booking.
Note that the last event locally causes a 2-booking, but the answer is still 3 because
eg. [10, 20), [10, 40), and [5, 15) are still triple booked.

Note:
The number of calls to MyCalendarThree.book per test case will be at most 400.
In calls to MyCalendarThree.book(start, end), start and end are integers in the range [0, 10^9].
"""

import bisect
class MyCalendarThree(object):
    def __init__(self):
        self.recom = []

    def bisect_insort(self, list, t):
        low, high = 0, len(list) - 1
        while low <= high:
            mid = (low + high) // 2
            if list[mid][0] < t:
                low = mid + 1
            elif list[mid][0] >= t:
                high = mid - 1
        return low

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        1674ms
        """
        left, right = start, end
        recom = self.recom
        add_recom = []
        i = self.bisect_insort(recom, left)

        if i >= len(recom):
            if i - 1 >= 0 and recom[i - 1][1] > start:
                add_recom.append([start, recom[i - 1][1], recom[i - 1][2] + 1])
                add_recom.append([recom[i - 1][1], end, 1])
                recom[i - 1][1] = start
            else:
                add_recom.append([start, end, 1])
        else:
            if i - 1 >= 0 and recom[i - 1][1] > start:
                if recom[i - 1][1] <= end:
                    add_recom.append([start, recom[i - 1][1], recom[i - 1][2] + 1])
                    new_left = recom[i - 1][1]
                    recom[i - 1][1] = start
                else:
                    add_recom.append([start, end, recom[i - 1][2] + 1])
                    add_recom.append([end, recom[i - 1][1], recom[i - 1][2]])
                    new_left = recom[i - 1][1]
                    recom[i - 1][1] = start

            else:
                new_left = left

            flag = True
            while i < len(recom) and recom[i][0] < right:
                flag = False
                if new_left < recom[i][0]:
                    add_recom.append([new_left, recom[i][0], 1])
                if recom[i][1] < right:
                    recom[i][2] += 1
                    new_left = recom[i][1]
                    flag = True
                elif recom[i][1] == right:
                    recom[i][2] += 1
                else:
                    add_recom.append([right, recom[i][1], recom[i][2]])
                    recom[i][1] = right
                    recom[i][2] += 1
                i += 1
            if flag:
                if new_left < right:
                    add_recom.append([new_left, right, 1])
            # print('add_recom', add_recom, 'i', i)
        for a in add_recom:
            bisect.insort_left(recom, a)
        # print([start, end], recom)
        self.m = 0
        for i in recom:
            self.m = max(self.m, i[-1])
        return self.m




        # Your MyCalendarThree object will be instantiated and called as such:
        # obj = MyCalendarThree()
        # param_1 = obj.book(start,end)
obj = MyCalendarThree()
# print(obj.bisect_insort([[1,1],[1,1],[1,1],[1,1],[3,1],[3,1],[4,1]], 1))
# print(obj.bisect_insort([[1,1],[1,1],[1,1],[1,1],[3,1],[3,1],[4,1]], 2))
# print(obj.book(10, 20))
# print(obj.book(50, 60))
# print(obj.book(10, 40))
# print(obj.book(5, 15))
# print(obj.book(5, 10))
# print(obj.book(25, 55))
a = ["MyCalendarThree","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book","book"]
b = [[],[2057,2137],[6250,6329],[1418,1476],[2643,2722],[9479,9573],[1027,1113],[1357,1414],[6412,6491],[6063,6144],[2720,2817],[5062,5116],[5494,5586],[3748,3803],[3148,3213],[95,173],[3956,4011],[8780,8833],[2939,3027],[569,658],[3772,3834],[1406,1473],[2163,2227],[3592,3661],[7826,7921],[6707,6771],[1250,1310],[1709,1760],[647,740],[5951,6047],[6277,6352],[4443,4495],[1099,1189],[8967,9049],[5418,5481],[1536,1624],[2935,2988],[5728,5817],[8598,8664],[393,479],[7439,7507],[5582,5678],[1076,1128],[573,634],[3604,3672],[1857,1943],[917,1001],[6286,6377],[6949,7006],[1340,1422],[9613,9703],[2175,2256],[2891,2979],[4096,4161],[972,1038],[5658,5719],[6008,6071],[757,848],[3479,3556],[1081,1142],[646,745],[8814,8886],[9453,9547],[4421,4489],[7674,7742],[5206,5267],[4496,4559],[8058,8131],[5347,5414],[7196,7261],[2753,2803],[2177,2243],[5229,5284],[5237,5314],[8826,8908],[6066,6145],[9222,9314],[6950,7038],[8701,8774],[7040,7130],[2836,2935],[2156,2230],[2061,2134],[3867,3955],[2897,2972],[8609,8661],[5399,5454],[3058,3118],[7516,7588],[5828,5897],[9272,9360],[2157,2214],[1513,1597],[7044,7101],[8230,8305],[7978,8034],[2919,2995],[1124,1186],[4335,4407],[9374,9425],[3660,3723],[3427,3485],[3559,3636],[5303,5391],[7688,7744],[5447,5513],[5042,5135],[1255,1305],[3544,3610],[4135,4216],[4199,4287],[5547,5637],[1925,2020],[7444,7525],[8326,8401],[9586,9668],[9827,9917],[8396,8492],[7109,7161],[7799,7886],[8266,8335],[7750,7817],[1569,1668],[6038,6135],[2712,2791],[3630,3726],[6439,6514],[6375,6439],[3373,3460],[6804,6872],[6815,6891],[8471,8566],[3417,3492],[7257,7319],[5671,5732],[6381,6473],[3400,3460],[4863,4952],[6564,6638],[3134,3186],[763,845],[2502,2552],[2194,2265],[5776,5856],[8351,8416],[2648,2746],[9255,9353],[4254,4332],[3389,3473],[8260,8313],[2277,2352],[813,865],[3989,4063],[1336,1405],[7192,7242],[8724,8802],[2904,2961],[9104,9174],[9040,9098],[5832,5885],[5559,5621],[4302,4362],[8974,9032],[8037,8133],[6895,6948],[8532,8593],[4112,4192],[1501,1596],[2672,2751],[8608,8696],[9297,9353],[4010,4106],[3741,3812],[7909,7990],[565,648],[624,722],[7951,8021],[7545,7598],[9468,9545],[8430,8524],[498,567],[8995,9061],[6748,6835],[7033,7128],[4202,4253],[9384,9439],[6990,7079],[8093,8182],[5868,5940],[8443,8495],[1502,1576],[1827,1898],[7271,7363],[8878,8977],[2918,3011],[9125,9209],[2396,2468],[8638,8728],[9518,9601],[5411,5500],[2002,2072],[207,286],[262,320],[7109,7171],[398,471],[1422,1511],[9036,9121],[7864,7955],[2408,2485],[4525,4620],[8658,8715],[6190,6278],[6157,6250],[3680,3755],[7117,7211],[184,274],[8528,8592],[2570,2628],[6099,6159],[4544,4618],[5095,5171],[7264,7360],[6232,6288],[8810,8869],[3638,3734],[7108,7181],[7590,7670],[5216,5299],[6197,6283],[9443,9531],[529,615],[3672,3750],[268,352],[6273,6336],[5800,5876],[8142,8241],[232,316],[1758,1839],[4811,4894],[4619,4687],[6460,6530],[5567,5626],[1101,1191],[1887,1946],[1152,1247],[6293,6360],[7372,7443],[2098,2161],[4473,4556],[4298,4385],[3308,3363],[2196,2246],[4142,4227],[3218,3286],[7236,7315],[3338,3408],[763,831],[9414,9506],[9252,9304],[7561,7656],[4476,4526],[6906,6972],[5892,5950],[3492,3584],[7783,7846],[6282,6374],[2098,2173],[5176,5230],[7105,7158],[6456,6548],[2927,2997],[89,180],[9391,9486],[2433,2488],[6940,7013],[562,647],[1405,1468],[9801,9865],[3380,3462],[8726,8810],[7093,7172],[7352,7406],[5448,5526],[1815,1907],[8936,8994],[9703,9779],[7348,7410],[7169,7262],[5619,5671],[1767,1857],[2435,2492],[1180,1240],[7039,7125],[2640,2694],[2871,2931],[409,486],[2928,2980],[582,648],[1725,1812],[3807,3891],[9863,9929],[5160,5243],[6580,6637],[1789,1853],[2770,2860],[5529,5594],[3772,3839],[5201,5262],[5130,5217],[4197,4281],[1642,1734],[4442,4506],[905,960],[8957,9027],[3995,4089],[4265,4360],[2804,2863],[1733,1812],[2967,3062],[9270,9362],[7319,7418],[7765,7830],[3438,3514],[6789,6866],[9415,9504],[3096,3162],[1413,1481],[1616,1675],[4591,4651],[3600,3670],[2118,2171],[3206,3285],[5456,5512],[3147,3211],[8236,8308],[9265,9327],[6862,6935],[4334,4416],[9281,9373],[5532,5595],[6008,6071],[152,241],[2492,2572],[7387,7458],[1010,1066],[6847,6938],[7384,7434],[8343,8419],[6461,6555],[2567,2655],[4402,4466],[8012,8073],[9149,9219],[5510,5592],[2042,2096],[3759,3818],[5966,6023],[8923,8991],[9076,9170],[7764,7848],[1190,1265],[5046,5134],[2940,2998],[7805,7890],[3286,3384],[2734,2809],[5070,5163],[6242,6292],[2645,2695],[9204,9292],[6941,7033],[1196,1262],[7036,7106],[5976,6059],[7003,7084],[664,750],[2636,2698],[1621,1708],[7478,7543],[5773,5823],[1093,1183],[6304,6366],[7129,7187],[9289,9359],[5636,5715],[2373,2434],[3418,3498],[9330,9387],[6121,6206],[5260,5340],[3483,3547],[414,508],[9906,9971],[3254,3335],[1730,1825],[9689,9751],[5217,5312],[1693,1777],[2588,2642],[6886,6937]]
# b = [[],[26,35],[26,32],[25,32],[18,26],[40,45],[19,26],[48,50],[1,6],[46,50],[11,18]]
ans = [0,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
for i in range(len(a)):
    if a[i] == 'book':
        # if b[i][1] == 471:
        #     print(b[i][0], b[i][1])
        #     print(obj.recom)
        c =obj.book(b[i][0], b[i][1])
        # if b[i][1] == 471:
        #     print(b[i][0], b[i][1])
        #     print(obj.recom)
        if c != ans[i]:
            print(obj.recom)
            break

import bisect


class MyCalendarThree(object):
    def __init__(self):
        self.pos = [float('-inf'), float('inf')]
        self.value = [0]
        self.k = 0

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        196ms
        """
        i = bisect.bisect_left(self.pos, start)
        if self.pos[i] != start:
            self.pos.insert(i, start)
            self.value.insert(i, self.value[i - 1])
        elif self.value[i] + 1 == self.value[i - 1]:
            self.pos.pop(i)
            self.value.pop(i - 1)
            i -= 1

        while True:
            self.value[i] += 1
            if self.k < self.value[i]:
                self.k = self.value[i]
            if end == self.pos[i + 1]:
                if self.value[i] == self.value[i + 1]:
                    self.pos.pop(i + 1)
                    self.value.pop(i + 1)
                break
            elif end < self.pos[i + 1]:
                self.pos.insert(i + 1, end)
                self.value.insert(i + 1, self.value[i] - 1)
                break
            i += 1

        return self.k