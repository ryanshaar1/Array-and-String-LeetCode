class Solution(object):
    def gcd(self,a, b):
        while b:
            a, b = b, a % b
        return a
    def gcdOfStrings(self, str1, str2):
        if str1 + str2 != str2 + str1:
            return ""  
        gcd_length = self.gcd(len(str1), len(str2))
        return str1[:gcd_length]
        