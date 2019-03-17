"""
 Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

For example,

123 -> "One Hundred Twenty Three"
12345 -> "Twelve Thousand Three Hundred Forty Five"
1234567 -> "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
"""
class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        82ms
        """
        def number2String(num):
            dicts = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six',
                     7: 'Seven', 8: 'Eight', 9: 'Nine'}
            dicts_2 = {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen',
                       15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen',
                       2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty',
                       7: 'Seventy', 8: 'Eighty', 9: 'Ninety'}
            if num == 0:
                return ''
            a = str(num)
            if len(a) == 1:
                return dicts[num]
            if len(a) == 2:
                if a[0] == '1':
                    return dicts_2[num]
                elif a[0] == '0':
                    return dicts[int(a[1])]
                else:
                    if a[1] != '0':
                        return dicts_2[int(a[0])] + ' ' + dicts[int(a[1])]
                    else:
                        return dicts_2[int(a[0])]
                    # return dicts_2[int(a[0])] + ' ' + dicts[int(a[1])]
            if len(a) == 3:
                s = dicts[int(a[0])] + ' ' + 'Hundred'
                a = a[1:]
                if a[0] == '1':
                    return s + ' ' + dicts_2[int(a)]
                elif a[0] == '0':
                    if a[1] != '0':
                        return s + ' ' + dicts[int(a[1])]
                    else:
                        return s
                else:
                    if a[1] != '0':
                        return s + ' ' + dicts_2[int(a[0])] + ' ' + dicts[int(a[1])]
                    else:
                        return s + ' ' + dicts_2[int(a[0])]
        result = []
        if num == 0:
            return 'Zero'
        while num != 0:
            result.append(num % 1000)
            num //= 1000
        f = ['', 'Thousand', 'Million', 'Billion']
        print(result)
        l = len(result)
        ans = ''
        for i in range(l - 1, 0, -1):
            a = number2String(result[i])
            if a != '':
                ans +=  a + ' ' + f[i] + ' '
        ans += number2String(result[0])
        return ans.strip()

    def numberToWords_1(self, num):
        """
        :type num: int
        :rtype: str
        42ms
        """
        if num == 0:
            return "Zero"

        b = 10 ** 9
        m = 10 ** 6
        t = 10 ** 3
        self.d = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        self.t = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen',
                  'Nineteen']
        self.y = ['', '', 'Twenty', 'Thirty', 'Forty', "Fifty", "Sixty", 'Seventy', 'Eighty', 'Ninety']

        return (
        self.h(num // b, 'Billion') + self.h((num % b) // m, 'Million') + self.h((num % m) // t, 'Thousand') + self.h(
            num % t, '')).strip()

    def h(self, num, tag):
        if num == 0:
            return ''

        h = num // 100
        r = num % 100
        res = ''
        if h > 0:
            res = self.d[h] + ' Hundred'

        if r < 20:
            if r < 10:
                res = (res + ' ' + self.d[r]).strip()
            else:
                res = (res + ' ' + self.t[r - 10]).strip()
        else:
            u = r // 10
            v = r % 10
            res = (res + ' ' + self.y[u] + ' ' + self.d[v]).strip()

        return (res + ' ' + tag).strip() + ' '

    def numberToWords_2(self, num):
        """
        :type num: int
        :rtype: str
        42ms
        """
        v1 = "Zero One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
        v2 = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()
        v3 = "Thousand Million Billion".split()

        index = -1
        res = ""
        while num:
            temp = ""
            token = num % 1000
            num = num // 1000
            if token > 99:
                temp += v1[token // 100] + " Hundred "
                token = token % 100
            if token > 19:
                temp += v2[token // 10 - 2] + " "
                token = token % 10
            if token > 0:
                temp += v1[token]
            temp = temp.strip()
            if index >= 0 and temp:  # 貌似必须这么写。。真是无语啊
                temp = temp + " " + v3[index]
            res = temp + " " + res.strip()
            index += 1

        return res.strip() if res else v1[0]




print(Solution().numberToWords(20))
print(Solution().numberToWords(1))


print(Solution().numberToWords(100))
print(Solution().numberToWords(110))
print(Solution().numberToWords(120001))
# print(Solution().numberToWords(1234567))
# print(Solution().numberToWords(2147483647))
