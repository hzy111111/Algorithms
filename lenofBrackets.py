#coding: utf-8
import unittest
"""
求一个字符串的有效括号长度
输入：字符串s
输出：有效括号长度
"""
class Solution:
    def lenofbrackets(self, s):
        n = len(s)
        if n == 0:
            return 0
        dp = [0 for i in range(n+1)]#初始化dp
        count = 0#count 记录括号对
        #填dp[0]
        if s[0] == '(':
            dp[0] = 1
        elif s[0] == ')':
            dp[0] = 0
        #循环填满dp[]
        for i in range(1, n):
            if s[i]=='(':
                dp[i] = dp[i-1]+1
            elif s[i]==')'and dp[i-1]!=0:#dp[]不为0说明前面出现'('
                dp[i] = dp[i-1]-1
                count += 2
        return count

class TestSolution(unittest.TestCase):
    def test(self):
        solve = Solution()
        #s为空时
        s = ''
        self.assertEqual(solve.lenofbrackets(s), 0)

        #‘(’开头
        s = '((('
        self.assertEqual(solve.lenofbrackets(s), 0)
        s = '((()))'
        self.assertEqual(solve.lenofbrackets(s), 6)

        #‘）’开头
        s = '))))'
        self.assertEqual(solve.lenofbrackets(s), 0)
        s = '))(()())'
        self.assertEqual(solve.lenofbrackets(s), 6)

        s = ')(('
        self.assertEqual(solve.lenofbrackets(s), 0)

if __name__=="__main__":
    unittest.main()
