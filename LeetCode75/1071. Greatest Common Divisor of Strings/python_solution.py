class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if not str1 or not str2:
            return ""

        if str1 + str2 != str2 + str1:
            return ""
        num1 = len(str1)
        num2 = len(str2)

        while num2 != 0:
            temp = num2
            num2 = num1 % num2
            num1 = temp

        return str1[:num1]
