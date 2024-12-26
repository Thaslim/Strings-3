"""
form triplets and itreratively form to strings
TC: O(1)
SP: O(1)
"""
class Solution:
    def numberToWords(self, num: int) -> str:
        below_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "" ,"Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        suffix = [ "","Thousand", "Million", "Billion"]
        res = ""
        def helper(num):    
            if num<20:
                return below_20[num]
            if num <100:
                return tens[num//10]+ " " + below_20[num%10]
            else:
                return below_20[num//100] +" Hundred " + helper(num%100)

        if num==0:
            return "Zero"
        res = ""
        i = 0
        while num >0:
            triplet = num%1000
            if triplet > 0:
                res = helper(triplet).strip() + " "+ suffix[i]+" "+res
            num//=1000
            i+=1
        return res.strip()

        