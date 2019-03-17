"""
Given an expression such as expression = "e + 8 - a + 5" and an evaluation map such as {"e": 1} (given in terms of evalvars = ["e"] and evalints = [1]), return a list of tokens representing the simplified expression, such as ["-1*a","14"]

    An expression alternates chunks and symbols, with a space separating each chunk and symbol.
    A chunk is either an expression in parentheses, a variable, or a non-negative integer.
    A variable is a string of lowercase letters (not including digits.) Note that variables can be multiple letters, and note that variables never have a leading coefficient or unary operator like "2x" or "-x".

Expressions are evaluated in the usual order: brackets first, then multiplication, then addition and subtraction. For example, expression = "1 + 2 * 3" has an answer of ["7"].

The format of the output is as follows:

    For each term of free variables with non-zero coefficient, we write the free variables within a term in sorted order lexicographically. For example, we would never write a term like "b*a*c", only "a*b*c".
    Terms have degree equal to the number of free variables being multiplied, counting multiplicity. (For example, "a*a*b*c" has degree 4.) We write the largest degree terms of our answer first, breaking ties by lexicographic order ignoring the leading coefficient of the term.
    The leading coefficient of the term is placed directly to the left with an asterisk separating it from the variables (if they exist.)  A leading coefficient of 1 is still printed.
    An example of a well formatted answer is ["-2*a*a*a", "3*a*a*b", "3*b*b", "4*a", "5*c", "-6"]
    Terms (including constant terms) with coefficient 0 are not included.  For example, an expression of "0" has an output of [].

Examples:

Input: expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]
Output: ["-1*a","14"]

Input: expression = "e - 8 + temperature - pressure",
evalvars = ["e", "temperature"], evalints = [1, 12]
Output: ["-1*pressure","5"]

Input: expression = "(e + 8) * (e - 8)", evalvars = [], evalints = []
Output: ["1*e*e","-64"]

Input: expression = "7 - 7", evalvars = [], evalints = []
Output: []

Input: expression = "a * b * c + b * a * c * 4", evalvars = [], evalints = []
Output: ["5*a*b*c"]

Input: expression = "((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))",
evalvars = [], evalints = []
Output: ["-1*a*a*b*b","2*a*a*b*c","-1*a*a*c*c","1*a*b*b*b","-1*a*b*b*c","-1*a*b*c*c","1*a*c*c*c","-1*b*b*b*c","2*b*b*c*c","-1*b*c*c*c","2*a*a*b","-2*a*a*c","-2*a*b*b","2*a*c*c","1*b*b*b","-1*b*b*c","1*b*c*c","-1*c*c*c","-1*a*a","1*a*b","1*a*c","-1*b*c"]

Note:

    expression will have length in range [1, 1000].
    evalvars, evalints will have equal lengths in range [0, 1000].

"""
class Solution(object):
    def basicCalculatorIV(self, expression, evalvars, evalints):
        """
        :type expression: str
        :type evalvars: List[str]
        :type evalints: List[int]
        :rtype: List[str]
        64ms
        """
        import collections
        dict_key = collections.defaultdict(int)
        for i in range(len(evalvars)):
            dict_key[evalvars[i]] = evalints[i]
        self.ex = expression.split(' ')
        # print(self.ex)
        def baskets(start, end, count):
            s = []
            while start < end:
                # print('ssssssss', self.ex[start], s, count)
                bagin = self.ex[start][0]
                if bagin == ')':
                    self.ex[start] = self.ex[start][1:]
                    if self.ex[start] == '':
                        start += 1
                    e = []
                    e.extend(j for i in s for j in i)
                    # print('gggggg', e)
                    return e, start
                if bagin not in ['-', '+', '*', '(']:
                    word = self.ex[start]
                    mark = len(word)
                    for i, char in enumerate(word):
                        if char == ')':
                            mark = i
                            break
                    self.ex[start] = word[mark + 1:]
                    b = word[0:mark]
                    if s == []:
                        s.append([b])
                    else:
                        m = s.pop()
                        if m == '-1*':
                            s.append([m + b])
                        elif m == '*':
                            val = s.pop()
                            new_ = []
                            for i in val:
                                new_.append(i + '*' + b)
                            s.append(new_)
                        else:
                            s.append([b])
                    if mark != len(word):
                        if self.ex[start] == '':
                            start += 1
                        e = []
                        e.extend(j for i in s for j in i)
                        # print('gggggg', e)
                        return e, start
                    start += 1
                elif bagin == '-':
                    s.append('-1*')
                    start += 1
                elif bagin == '*':
                    s.append('*')
                    start += 1
                elif bagin == '+':
                    s.append('+')
                    start += 1
                elif bagin == '(':
                    self.ex[start] = self.ex[start][1:]
                    a, start = baskets(start, end, count + 1)
                    if s == []:
                        s.append(a)
                    else:
                        m = s.pop()
                        if m == '-1*':
                            s.append([m + b for b in a])
                        elif m == '*':
                            val = s.pop()
                            new_ = []
                            for i in val:
                                new_.extend(i + '*' + b for b in a)
                            s.append(new_)
                        else:
                            s.append(a)
                else:
                    start += 1
            e = []
            e.extend(j for i in s for j in i)
            return e, start
        alls = baskets(0, len(self.ex), 0)[0]
        # print(alls)
        # print(len(alls))
        dicts = collections.defaultdict(int)
        for key in alls:
            key_list = key.split('*')
            num = 1
            ans = []
            for val in key_list:
                if val == '-1':
                    num *= -1
                elif val.isdigit():
                    num *= int(val)
                elif val in dict_key:
                    num *= dict_key[val]
                else:
                    ans.append(val)
            ans = sorted(ans)
            keys = ''
            for i in ans:
                keys += i + '*'
            dicts[keys[:-1]] += num
        result = []
        for key in sorted(dicts.keys(), key=lambda a:(-len(a), a)):
            if dicts[key] != 0:
                S = str(dicts[key])
                if key != '':
                    result.append(S + '*' + key)
                else:
                    result.append(S)
        # print(dicts)
        return result

# print(Solution().basicCalculatorIV(expression = "((a * b) + (c - d) * f) + h",
# evalvars = [], evalints = []))
# print(Solution().basicCalculatorIV("((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))",[], []))
print(Solution().basicCalculatorIV(expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]))
print(Solution().basicCalculatorIV(expression = "e - 8 + temperature - pressure",evalvars = ["e", "temperature"], evalints = [1, 12]))

print(Solution().basicCalculatorIV(expression = "(e + 8) * (e - 8)", evalvars = [], evalints = []))
print(Solution().basicCalculatorIV(expression = "7 - 7", evalvars = [], evalints = []))
print(Solution().basicCalculatorIV( expression = "a * b * c + b * a * c * 4", evalvars = [], evalints = []))
