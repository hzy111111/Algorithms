#coding: utf-8
"""
字符串匹配，字符串s，字符模式p。
‘*’：任意字符串
‘？’：单个字符
"""
class Solution:
    def isMatch(self, s, p):
        dp = [[False for j in range(len(p)+1)] for i in range(len(s)+1)]
        dp[0][0] = True
        #填第一行。s=''时，只有'*'和''能匹配
        for j in range(1,len(p)+1):
            dp[0][j] = (p[j-1]=='*') and dp[0][j-1]
        #两层循环，填满矩阵，返回最后一个值
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1]=='*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j-1] or dp[i-1][j]#只要前面匹配成功，*可以为空或一个任意字符或任意字符
                else:
                    dp[i][j]=(p[j-1]=='?' or p[j-1]==s[i-1]) and dp[i-1][j-1]
        print(dp)
        return dp[len(s)][len(p)]

solve = Solution()
s="aabc"
p="a*?"
print(solve.isMatch(s, p))



