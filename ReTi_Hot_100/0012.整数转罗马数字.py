#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0012.整数转罗马数字.py
@Time    :   2020-06-27
@Author  :   KouKai
@Version :   V1.0
@Remarks :   None
i = 0
while num > 0:
    value = (10**i) * (num % 10)
    i += 1
    num = num // 10
    print(value)
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
    def intToRoman(self, num: int) -> str:
        """ 取巧的地方就是提前把顺序排好 """
        nums   = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_nums = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        ans = ''
        
        for i in range(13):
            while num >= nums[i]:
                ans += roman_nums[i]
                num -= nums[i]
        return ans


if __name__ == '__main__':
    start = time.time()
    
    sitr = Solution()
    num = 3
    result = sitr.intToRoman(num)
    print("result = {}".format(result))

    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))