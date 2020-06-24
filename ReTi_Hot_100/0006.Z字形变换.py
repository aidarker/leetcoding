#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   06.Z字形的变形.py
@Time    :   2020-06-23
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
    def convert(self, s: str, numRows: int) -> str:
        """  """
        if numRows < 2:
            return s
        n = len(s)
        interval = 2*numRows - 2
        ans =""
        for i in range(numRows):
            j = 0
            while j+i<n:
                ans += s[j+i]
                if i!=0 and i!=numRows-1 and j+interval-i<n:
                    ans += s[j+interval-i]
                j += interval
        return ans


if __name__ == '__main__':
    start = time.time()
    
    s = "LEETCODEISHIRING"
    numRows = 4
    sc = Solution()
    result = sc.convert(s, numRows)
    print(result)

    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))