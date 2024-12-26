"""
Maintain calc, tail, currnum and recursively evaluate expression if a paranthesis is encountered
TC: O(n) n = len(string)
SP: O(d) (due to recursion) d max number of paranthesis
"""

class Solution:
    def calculate(self, s: str) -> int:
        
        signs = {"+", "-", "*", "/"}
        def helper(i):
            calc = tail = currnum = 0
            lastsign = "+"
            while i < len(s):
                c = s[i]
                if c.isdigit():
                    currnum = currnum*10 + int(c)
                if c=="(":
                    i, currnum = helper(i+1)
                if c in signs or c ==")" or i== len(s)-1:
                    if lastsign == "+":
                        calc+=currnum
                        tail = currnum
                    elif lastsign == "-":
                        calc-=currnum
                        tail = -currnum
                    elif lastsign=="*":
                        calc = calc-tail + tail*currnum
                        tail = currnum*tail
                    else:
                        calc = calc-tail + int(tail/currnum)
                        tail = int(tail/currnum)
                    lastsign = c
                    currnum = 0
                if c==")"or i== len(s)-1:
                    return i, calc
                i+=1
        return helper(0)[1]
                    
calc = Solution()
print(calc.calculate("(1+(4+5+2)-3)+(6+8)"))