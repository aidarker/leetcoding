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


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        :remark: 感谢大牛的提示
        """
        if len(s) % 2 != 0:
            return False
        
        dic = {'{': '}',  '[': ']', '(': ')', '#':'#'}
        stack = ['#']
        for char in s:
            if char in dic:
                stack.append(char)
            elif dic[stack.pop()] != char:
                return False
        return len(stack) == 1


if __name__ == '__main__':
    start = time.time()
    
    s = "()[]{}"
    siv = Solution()
    result = siv.isValid(s)
    print("result = {}".format(result))

    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))