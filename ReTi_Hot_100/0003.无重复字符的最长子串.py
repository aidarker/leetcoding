#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   03.无重复字符的最长字串.py
@Time    :   2020-06-21
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
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_dict = dict()
        i, char_long = 0, 0
        for j in range(len(s)):
            if s[j] in char_dict:
                i = max(char_dict[s[j]], i)    # 原字母发生变化后的位置
            char_long = max(char_long, j-i+1)   # 统计字串的长度
            char_dict[s[j]] = j+1  # 利用字典保存字母的最新位置
            print("j:{}\ti:{}\tchar_long:{}\tchar_dict:{}".format(j, i, char_long, char_dict))
        return char_long
        

if __name__ == '__main__':
    start = time.time()
    
    s = "aab"
    slols = Solution()
    result = slols.lengthOfLongestSubstring(s)
    print(result)
    
    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))