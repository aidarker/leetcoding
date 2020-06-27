#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0010.正则表达式匹配.py
@Time    :   2020-06-26
@Author  :   KouKai
@Version :   V1.0
@Remarks :   None
'''

import sys
import os
path = os.getcwd()
path = os.path.dirname(path)
sys.path.append(path)

import time
import datetime
import logging
logging.basicConfig(level = logging.INFO,format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)


# class Solution(object):
#     def isMatch(self, s, p):
#         """
#         :type s: str
#         :type p: str
#         :rtype: bool
#         """        
#         if not p: return not s
#         if not s and len(p) == 1: return False

#         m = len(s) + 1
#         n = len(p) + 1

#         dp = [[False for i in range(n)] for j in range(m)]
        
#         dp[0][0] = True
#         dp[0][1] = False
#         for c in range(2, n):
#             j = c-1
#             if p[j] == '*':
#                 dp[0][c] = dp[0][c-2]
        
#         for r in range(1, m):
#             i = r-1
#             for c in range(1, n):
#                 j = c-1
#                 if s[i] == p[j] or p[j] == '.':
#                     dp[r][c] = dp[r-1][c-1]
#                 elif p[j] == '*':
#                     if p[j-1] == s[i] or p[j-1] == '.':
#                         dp[r][c] = dp[r-1][c] or dp[r][c-2]
#                     else:
#                         dp[r][c] = dp[r][c-2]
#                 else:
#                     dp[r][c] = False

#         return dp[m-1][n-1]


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        if not s and len(p) == 1: return False

        m, n = len(s), len(p)
        # dp[i][j] 表示 s[:i] 与 p[:j] 是否匹配，各自前 i、j 个是否匹配
        dp = [[False for j in range(n + 1)] for i in range(m + 1)]
        print("m:{}\tn:{}\trow(dp):{}\tcol(dp):{}".format(m, n, len(dp), len(dp[0])))

        dp[0][0] = True

        # s 为空串
        for j in range(1, n + 1):
            # 若 p 的第 j 个字符 p[j - 1] 是 '*'
            # 说明第 j - 1、j 位可有可无
            # 那么如果前 j - 2 个已经匹配上，前 j 个也可以匹配上
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j-2]
            
            print("j-1:{}\tp[{}]:{}\tdp[0][{}]:{}".format(j-1, j-1, p[j-1], j, dp[0][j]))

        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[j - 1] == s[i - 1] or p[j-1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if p[j - 2] == s[i - 1] or p[j-2] == '.':
                        dp[i][j] = dp[i][j - 2] or dp[i - 1][j - 2] or dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 2]

        return dp[m][n]


if __name__ == '__main__':
    start = time.time()
    
    s = "aab"
    p = "c*a*b"
    
    sim = Solution()
    result = sim.isMatch(s, p)
    print(result)

    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))