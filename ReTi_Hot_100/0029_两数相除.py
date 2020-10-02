#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0028_实现strStr.py
@Time    :   2020-09-11
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
    def divide(self, dividend, divisor):
        MIN_VALUE, MAX_VALUE = -2**31, 2**31-1

        def recursion(dividend, divisor):
            if dividend < divisor:
                return 0

            if dividend == divisor:
                return 1

            nn = 1
            dd = divisor
            while True:
                if dividend > dd:
                    n = nn
                    nn += nn
                    d = dd
                    dd += dd
                elif dividend == dd:
                    return nn
                else:
                    return n + recursion(dividend-d, divisor)
                
        positive = True if (dividend>0 and divisor>0) or (dividend<0 and divisor<0) else False
        ans = recursion(abs(dividend), abs(divisor))

        if positive:
            if ans > MAX_VALUE:
                return MAX_VALUE
            else:
                return ans
        else:
            return -ans


if __name__ == '__main__':
    start = time.time()

    sd = Solution()
    result = sd.divide(7, -3)
    print(result)

    end = time.time()
    delta = end - start
    print("Finished time is {}".format(datetime.timedelta(seconds=delta)))

