"""
Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.
"""
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        def isNumber(self, s):
            """
            :type s: str
            :rtype: bool
            """
            # define a DFA
            state = [{},
                     {'blank': 1, 'sign': 2, 'digit': 3, '.': 4},
                     {'digit': 3, '.': 4},
                     {'digit': 3, '.': 5, 'e': 6, 'blank': 9},
                     {'digit': 5},
                     {'digit': 5, 'e': 6, 'blank': 9},
                     {'sign': 7, 'digit': 8},
                     {'digit': 8},
                     {'digit': 8, 'blank': 9},
                     {'blank': 9}]
            currentState = 1
            for c in s:
                if c >= '0' and c <= '9':
                    c = 'digit'
                if c == ' ':
                    c = 'blank'
                if c in ['+', '-']:
                    c = 'sign'
                if c not in state[currentState].keys():
                    return False
                currentState = state[currentState][c]
            if currentState not in [3, 5, 8, 9]:
                return False
            return True

        def isNumber_1(self, s):
            """
            :type s: str
            :rtype: bool
            62ms
            """
            s = s.strip()  # remove the space
            # s = s.split(" ")
            if len(s) == 0:
                return False

            dot = False
            eNum = False
            sign = False
            digit = False
            i = 0
            while i < len(s):
                if s[i].isdigit():
                    i += 1
                    digit = True
                    sign = True
                elif not dot and s[i] == '.':
                    i += 1
                    dot = True
                    sign = True
                elif digit and (s[i] == 'e' or s[i] == 'E') and not eNum:
                    i += 1
                    dot = True
                    eNum = True
                    digit = False
                    sign = False
                elif not sign and (s[i] == '+' or s[i] == '-'):
                    i += 1
                    sign = True
                else:
                    return False
            if digit:
                return True
            else:
                return False

print(Solution().isNumber('0'))
print(Solution().isNumber('000.1'))
print(Solution().isNumber('abc'))
print(Solution().isNumber('1 a'))
print(Solution().isNumber('2e10'))
print(Solution().isNumber(' 008'))
print(Solution().isNumber('00 '))
print(Solution().isNumber('3/4'))
print(Solution().isNumber('.'))
print(Solution().isNumber('e1'))
print(Solution().isNumber('0e1'))
print(Solution().isNumber(' .1'))
print(Solution().isNumber(' 0.'))
print(Solution().isNumber('1.'))
print(Solution().isNumber('  '))
print(Solution().isNumber('.e1'))
print(Solution().isNumber('-1.'))
print(Solution().isNumber(". 1"))
print(Solution().isNumber("0 .1"))
print(Solution().isNumber("01 e1"))
print(Solution().isNumber("01e 1"))
print(Solution().isNumber(".-4"))
print(Solution().isNumber("-4 e-4"))
print(Solution().isNumber("6 + 1"))
print(Solution().isNumber(".6+1"))