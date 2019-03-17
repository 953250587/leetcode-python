"""
 You are given a string expression representing a Lisp-like expression to return the integer value of.

The syntax for these expressions is given as follows.

An expression is either an integer, a let-expression, an add-expression, a mult-expression, or an assigned variable. Expressions always evaluate to a single integer.

(An integer could be positive or negative.)

A let-expression takes the form (let v1 e1 v2 e2 ... vn en expr), where let is always the string "let", then there are 1 or more pairs of alternating variables and expressions, meaning that the first variable v1 is assigned the value of the expression e1, the second variable v2 is assigned the value of the expression e2, and so on sequentially; and then the value of this let-expression is the value of the expression expr.

An add-expression takes the form (add e1 e2) where add is always the string "add", there are always two expressions e1, e2, and this expression evaluates to the addition of the evaluation of e1 and the evaluation of e2.

A mult-expression takes the form (mult e1 e2) where mult is always the string "mult", there are always two expressions e1, e2, and this expression evaluates to the multiplication of the evaluation of e1 and the evaluation of e2.

For the purposes of this question, we will use a smaller subset of variable names. A variable starts with a lowercase letter, then zero or more lowercase letters or digits. Additionally for your convenience, the names "add", "let", or "mult" are protected and will never be used as variable names.

Finally, there is the concept of scope. When an expression of a variable name is evaluated, within the context of that evaluation, the innermost scope (in terms of parentheses) is checked first for the value of that variable, and then outer scopes are checked sequentially. It is guaranteed that every expression is legal. Please see the examples for more details on scope.

Evaluation Examples:

Input: (add 1 2)
Output: 3

Input: (mult 3 (add 2 3))
Output: 15

Input: (let x 2 (mult x 5))
Output: 10

Input: (let x 2 (mult x (let x 3 y 4 (add x y))))
Output: 14
Explanation: In the expression (add x y), when checking for the value of the variable x,
we check from the innermost scope to the outermost in the context of the variable we are trying to evaluate.
Since x = 3 is found first, the value of x is 3.

Input: (let x 3 x 2 x)
Output: 2
Explanation: Assignment in let statements is processed sequentially.

Input: (let x 1 y 2 x (add x y) (add x y))
Output: 5
Explanation: The first (add x y) evaluates as 3, and is assigned to x.
The second (add x y) evaluates as 3+2 = 5.

Input: (let x 2 (add (let x 3 (let x 4 x)) x))
Output: 6
Explanation: Even though (let x 4 x) has a deeper scope, it is outside the context
of the final x in the add-expression.  That final x will equal 2.

Input: (let a1 3 b2 (add a1 1) b2)
Output 4
Explanation: Variable names can contain digits after the first character.

Note:
The given string expression is well formatted: There are no leading or trailing spaces, there is only a single space separating different components of the string, and no space between adjacent parentheses. The expression is guaranteed to be legal and evaluate to an integer.
The length of expression is at most 2000. (It is also non-empty, as that would not be a legal expression.)
The answer and all intermediate calculations of that answer are guaranteed to fit in a 32-bit integer.


"""


class Solution(object):
    def evaluate(self, expression):
        """
        :type expression: str
        :rtype: int
        72ms
        """
        dicts = {}
        expressions = []
        s = ''
        for char in expression:
            if char == '(' or char == ')':
                if s != '':
                    expressions.append(s)
                    s = ''
                expressions.append(char)
            elif char == ' ':
                if s != '':
                    expressions.append(s)
                s = ''
            else:
                s += char
        expression.isdigit()
        print(expressions)
        # print('-12'.isdigit())
        end = len(expressions)
        def dfs(start, dicts):
            while start < end:
                # print(dicts)
                if expressions[start] == '(':
                    ans, start = dfs(start + 1, dicts.copy())
                    return ans, start + 1
                elif expressions[start].isdigit():
                    return int(expressions[start]), start + 1
                elif expressions[start][0] == '-' and expressions[start][1:].isdigit():
                    return -int(expressions[start][1:]), start + 1
                elif expressions[start] in dicts:
                    return dicts[expressions[start]], start + 1
                elif expressions[start] == 'let':
                    start += 1
                    while expressions[start] != '(' and start + 1 < end and expressions[start + 1] != ')':
                        dicts[expressions[start]], start = dfs(start + 1, dicts.copy())
                        # print('ss', start, dicts)
                    if expressions[start] == '(':
                        # print('t', start)
                        ans, start = dfs(start, dicts.copy())
                        return ans, start
                    else:
                        # print('t1', start)
                        if expressions[start].isdigit():
                            return int(expressions[start]), start + 1
                        elif expressions[start][0] == '-' and expressions[start][1:].isdigit():
                            return -int(expressions[start][1:]), start + 1
                        else:
                            return dicts[expressions[start]], start + 1
                elif expressions[start] == 'add':
                    start += 1
                    a, start = dfs(start, dicts.copy())
                    # print('a', a, start)
                    b, start = dfs(start, dicts.copy())
                    return a + b, start
                elif expressions[start] == 'mult':
                    start += 1
                    a, start = dfs(start, dicts.copy())
                    # print('m', a, start)
                    b, start = dfs(start, dicts.copy())
                    return a * b, start
        return dfs(0, dicts)[0]

    def evaluate_1(self, expression):
        """
        :type expression: str
        :rtype: int
        70ms
        """
        return self.cals(expression, {})

    def cals(self, s, dic):
        # print(s,dic)
        tt = 0
        while s[tt] == ' ': tt += 1
        s = s[tt:]
        if s[0] != '(':
            try:
                return int(s)
            except:
                return dic[s]
        p = s.find(" ")
        if s[1] != 'l':
            tmp = s.find(" ", p + 1)
            if s[p + 1] != '(':
                t = s[p + 1:tmp]
                try:
                    a = int(t)
                except:
                    a = dic[t]
            else:
                ctl = 1
                ctr = 0
                p += 1
                q = p
                while ctr != ctl:
                    p += 1
                    if s[p] == '(':
                        ctl += 1
                    elif s[p] == ')':
                        ctr += 1
                a = self.cals(s[q:p + 1], dic.copy())
                tmp = p + 1
            if s[1] == 'm':
                return a * self.cals(s[tmp + 1:-1], dic.copy())
            else:
                return a + self.cals(s[tmp + 1:-1], dic.copy())
        else:
            p += 1
            while s[p] != '(':
                if s.find(' ', p + 2) == -1:
                    if '0' <= s[p] <= '9' or s[p] in ['-', '+']:
                        return int(s[p:-1])
                    return dic[s[p:-1]]
                tmp = s.find(" ", p)
                if s[tmp + 1] != '(':
                    tmp2 = s.find(" ", tmp + 1)
                    try:
                        dic[s[p:tmp]] = int(s[tmp + 1:tmp2])
                    except:
                        dic[s[p:tmp]] = int(dic[s[tmp + 1:tmp2]])
                    p = tmp2 + 1
                else:
                    ctl = 1
                    ctr = 0
                    tmp2 = tmp + 1
                    while ctr != ctl:
                        tmp2 += 1
                        if s[tmp2] == '(':
                            ctl += 1
                        elif s[tmp2] == ')':
                            ctr += 1
                    dic[s[p:tmp]] = self.cals(s[tmp + 1:tmp2 + 1], dic.copy())
                    p = tmp2 + 2
            return self.cals(s[p:-1], dic)


print(Solution().evaluate('(add 1 2)'))
print(Solution().evaluate('(mult 3 (add 2 3))'))
print(Solution().evaluate('(let x 2 (mult x 5))'))
print(Solution().evaluate('(let x 2 (mult x (let x 3 y 4 (add x y))))'))
print(Solution().evaluate('(let x 3 x 2 x)'))
print(Solution().evaluate('(let x 1 y 2 x (add x y) (add x y))'))
print(Solution().evaluate('(let x 2 (add (let x 3 (let x 4 x)) x))'))
print(Solution().evaluate('(let a1 3 b2 (add a1 1) b2)'))
print(Solution().evaluate(('(add (add 4 5) (mult 5 (add 4 4))')))
print(Solution().evaluate("(let x 7 -12)"))