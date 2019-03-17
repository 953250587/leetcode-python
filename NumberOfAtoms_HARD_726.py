"""
Given a chemical formula (given as a string), return the count of each atom.

An atomic element always starts with an uppercase character, then zero or more lowercase letters, representing the name.

1 or more digits representing the count of that element may follow if the count is greater than 1. If the count is 1, no digits will follow. For example, H2O and H2O2 are possible, but H1O2 is impossible.

Two formulas concatenated together produce another formula. For example, H2O2He3Mg4 is also a formula.

A formula placed in parentheses, and a count (optionally added) is also a formula. For example, (H2O2) and (H2O2)3 are formulas.

Given a formula, output the count of all elements as a string in the following form: the first name (in sorted order), followed by its count (if that count is more than 1), followed by the second name (in sorted order), followed by its count (if that count is more than 1), and so on.

Example 1:

Input:
formula = "H2O"
Output: "H2O"
Explanation:
The count of elements are {'H': 2, 'O': 1}.

Example 2:

Input:
formula = "Mg(OH)2"
Output: "H2MgO2"
Explanation:
The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.

Example 3:

Input:
formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
Explanation:
The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.

Note:
All atom names consist of lowercase letters, except for the first character which is uppercase.
The length of formula will be in the range [1, 1000].
formula will only consist of letters, digits, and round parentheses, and is a valid formula as defined in the problem.
"""


class Solution(object):
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        37ms
        """
        import collections
        dict_atoms = collections.defaultdict(int)
        end = len(formula)

        def dfs(start, count):
            dicts = collections.defaultdict(int)
            if start >= end:
                return start
            while start < end:
                # print(dicts, count)
                if formula[start].isupper():
                    s = formula[start]
                    start += 1
                    while start < end and formula[start].islower():
                        s += formula[start]
                        start += 1
                    a = ''
                    while start < end and formula[start].isdigit():
                        a += formula[start]
                        start += 1
                    if a == '':
                        a = '1'
                    dicts[s] += int(a)
                elif formula[start] == '(':
                    start, new_dicts = dfs(start + 1, count + 1)
                    for key in new_dicts:
                        dicts[key] += new_dicts[key]
                elif formula[start] == ')':
                    a = ''
                    while start + 1 < end and formula[start + 1].isdigit():
                        a += formula[start + 1]
                        start += 1
                    if a == '':
                        a = '1'
                    for key in dicts:
                        dicts[key] *= int(a)
                    return start + 1, dicts

            return start, dicts

        _, dict_atoms = dfs(0, 0)
        keys = sorted(dict_atoms.keys())
        ans = ''
        for key in keys:
            s = str(dict_atoms[key]) if dict_atoms[key] != 1 else ''
            ans += key + s
        return ans

    def countOfAtoms_1(self, formula):
        """
        36ms
        :param formula:
        :return:
        """
        import collections
        N = len(formula)
        stack = [collections.Counter()]
        i = 0
        while i < N:
            if formula[i] == '(':
                stack.append(collections.Counter())
                i += 1
            elif formula[i] == ')':
                top = stack.pop()
                i += 1
                i_start = i
                while i < N and formula[i].isdigit(): i += 1
                multiplicity = int(formula[i_start: i] or 1)
                for name, v in top.items():
                    stack[-1][name] += v * multiplicity
            else:
                i_start = i
                i += 1
                while i < N and formula[i].islower(): i += 1
                name = formula[i_start: i]
                i_start = i
                while i < N and formula[i].isdigit(): i += 1
                multiplicity = int(formula[i_start: i] or 1)
                stack[-1][name] += multiplicity

        return "".join(name + (str(stack[-1][name]) if stack[-1][name] > 1 else '')
                       for name in sorted(stack[-1]))
# print(Solution().countOfAtoms(formula = "H2O"))
# print(Solution().countOfAtoms(formula = "Mg(OH)2"))
print(Solution().countOfAtoms("K4(ON(SO3)2)2"))
print(Solution().countOfAtoms("K4(ON(SO3)2)K4(ON(SO3)2)12"))
print(Solution().countOfAtoms("Be32"))