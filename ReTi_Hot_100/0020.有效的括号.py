#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   20.有效的括号.py
@Time    :   2020-06-19
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


class Solution:
    def generateParenthesis(self, n):
        """ 感谢官方提供的回溯方法 """
        res = []
        def backtrack(S, left, right):
            if len(S) == 2*n:
                res.append("".join(S))
                return
            if left<n:
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()
            if right<left:
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()

        backtrack([], 0, 0)
        return res


if __name__ == '__main__':
    start = time.time()
    
    n = 3
    sgp = Solution()
    result = sgp.generateParenthesis(n)
    print("result = \n{}".format(result))

    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))