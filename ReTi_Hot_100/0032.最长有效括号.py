#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0032.最长有效括号.py
@Time    :   2020-10-12
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

class Solution(object):
    def longestValidParentheses(self, s):
        """ 感谢:大佬的动态规划的方法 """
        n = len(s)
        if n == 0 or n == 1:
            return 0
        
        dp = [0] * n    # dp里面保存记录长度
        counter = 0
        for i in range(n):
            if i>0 and s[i]==")":   #
                if s[i-1] == "(":
                    dp[i] = dp[i-2] + 2
                elif s[i-1] == ")" and i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=="(":
                    dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
                else:
                    continue
                
                if dp[i] > counter:
                    counter = dp[i]
            else:   # 如果s[i]-上来就是(, 则dp[i]为0, 不可能组成有效的括号
                continue

        return counter


if __name__ == '__main__':
    start = time.time()
    
    slvp = Solution()
    s = ")()()"
    result = slvp.longestValidParentheses(s)
    print("result: {}".format(result))

    end = time.time()
    delta = end - start
    print("Finished time is {}".format(datetime.timedelta(seconds=delta)))