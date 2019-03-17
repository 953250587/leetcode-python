"""
Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are +, - and *.


Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
"""
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        106ms
        """
        def operation(input):
            count=0
            operationlist=[]
            for i in input:
                if i.isdigit():
                    pass
                else:
                    operationlist.append(count)
                count+=1
            # print('position',operationlist)
            return operationlist

        def calc_Compute(input):
            operation_lists=operation(input)
            if len(operation_lists)==0:
                return [int(input)]
            if len(operation_lists)==1:
                i=operation_lists[0]
                result=eval(str(input[0:i]) + input[i] + str(input[i+1:]))
                return [result]
            all_together = []
            for i in range(len(operation_lists)):
                left = []
                right = []
                left.extend(calc_Compute(input[0:operation_lists[i]]))
                right.extend(calc_Compute(input[operation_lists[i]+1:]))
                for l in left:
                    for r in right:
                         all_together.append(eval(str(l) + input[operation_lists[i]] + str(r)))
            return all_together
        # operation(input)
        return calc_Compute(input)

    def calculate(self, l, r, oper):
        if oper == "*":
            return l * r
        elif oper == "+":
            return l + r
        else:
            return l - r

    def diffWaysToCompute_1(self, inpt):
        """
        :type input: str
        :rtype: List[int]
        58ms
        """
        ret = []
        if inpt.isdigit():
            ret.append(int(inpt))
            return ret
        else:
            for i in range(len(inpt)):
                if inpt[i] in "*+-":
                    ret1 = self.diffWaysToCompute(inpt[:i])
                    ret2 = self.diffWaysToCompute(inpt[i + 1:])

                    for l in ret1:
                        for r in ret2:
                            ret.append(self.calculate(l, r, inpt[i]))

        return ret

print(Solution().diffWaysToCompute("20*3-4*5"))
# print(eval('5*3-10*2'))
# print([i for i in range(1,5,2)])
# a=3;b=4
# str=str(str(a)+'+'+str(b))
# print(eval(str))