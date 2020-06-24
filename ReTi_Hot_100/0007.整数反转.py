#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   7_整数反转.py
@Time    :   2020-06-03
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
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = 0
        temp = abs(x)
        while (temp != 0):
            rev = rev*10 + temp%10   # 对于负数也是可以的
            temp //= 10
        
        if -2147483648 < rev < 2147483647 and x < 0:
            return -rev
        elif -2147483648 < rev < 2147483647 and x >= 0:
            return rev
        else:
            return 0
        


if __name__ == '__main__':
    start = time.time()
    
    rs = Solution()
    num = -123
    print("反转前 : {}".format(num))
    result = rs.reverse(num)
    print("反转后 : {}".format(result))

    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))