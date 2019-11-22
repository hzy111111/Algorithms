#coding: utf-8
import unittest
"""
字符串匹配，字符串s，字符模式p。
‘*’：任意字符串
‘？’：单个字符
"""
class Solution:
    def isMatch(self, s, p):
        """
        :param s:目标字符串s,str
        :param p:模式字符串,str
        :return:dp[len(s)][len(p)],是否匹配，bool
        """
        dp = [[False for j in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True
        #填第一行。s=''时，只有'*'和''能匹配
        for j in range(1,len(p)+1):
            dp[0][j] = (p[j-1]=='*') and dp[0][j-1]
        #两层循环，填满矩阵，返回最后一个值
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j-1] or dp[i-1][j]#只要前面匹配成功，*可以为空或一个任意字符或任意字符
                else:
                    dp[i][j] = (p[j-1] == '?' or p[j-1] == s[i-1]) and dp[i-1][j-1]
        #print(dp) #打印矩阵
        return dp[len(s)][len(p)]

class TestSolution(unittest.TestCase):
    #出现空的情况
    def test_empty(self):
        solve = Solution()
        s = ""
        p = ""
        self.assertEqual(solve.isMatch(s, p), True)

        s = ""
        p = "*"
        self.assertEqual(solve.isMatch(s, p), True)

        s = "a"
        p = ""
        self.assertEqual(solve.isMatch(s, p), False)

        s = ""
        p = "?"
        self.assertEqual(solve.isMatch(s, p), False)
    #出现*的情况
    def test_star(self):
        solve = Solution()
        s = "abac"
        p = "*"
        self.assertEqual(solve.isMatch(s, p), True)

        s = "abac"
        p = "*b"
        self.assertEqual(solve.isMatch(s, p), False)

        s = "abac"
        p = "b*"
        self.assertEqual(solve.isMatch(s, p), False)

        s = "abac"
        p = "a*"
        self.assertEqual(solve.isMatch(s, p), True)
    #出现？或（？和*）的情况
    def test_star_que(self):
        solve = Solution()
        s = "abac"
        p = "a?ac"
        self.assertEqual(solve.isMatch(s, p), True)

        s = "abac"
        p = "a?c"
        self.assertEqual(solve.isMatch(s, p), False)

        s = "abac"
        p = "?*"
        self.assertEqual(solve.isMatch(s, p), True)

        s = "abac"
        p = "b?*"
        self.assertEqual(solve.isMatch(s, p), False)

if __name__=="__main__":
    unittest.main()



