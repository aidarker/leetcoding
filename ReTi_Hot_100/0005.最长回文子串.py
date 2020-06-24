#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   05.最长回文子串.py
@Time    :   2020-06-22
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


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)

        if n < 2:
            return s
        
        # 构造一个矩阵存放所有结果
        M = [[False for _ in range(n)] for _ in range(n)]
        
        ans = ""
        # 初始化值，最少的长度是自己
        # 枚举子串的长度 l+1
        for l in range(n):
            # 枚举子串的起始位置 i，这样可以通过 j=i+l 得到子串的结束位置
            for i in range(n):
                j = i + l
                if j >= len(s):
                    break
                if l == 0:
                    M[i][j] = True
                elif l == 1:
                    M[i][j] = (s[i] == s[j])
                else:
                    M[i][j] = (M[i+1][j-1] and s[i]==s[j])
                
                if M[i][j] and l+1>len(ans):
                    ans = s[i:j+1]
        return ans


if __name__ == '__main__':
    start = time.time()
    
    s = "babad"
    slp = Solution()
    result = slp.longestPalindrome(s)
    print(result)

    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))