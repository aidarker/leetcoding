#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   2_两数相加.py
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


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = p = ListNode(None)
        sum = 0
        while l1 or l2 or sum:
            sum += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            print("l1.val:{}\tl2.val:{}\tsum:{}".format(l1.val, l2.val, sum))
            p.next = ListNode(sum % 10) # 将累加求和的值保存在下一个结点位置
            print("p.next.val:{}".format(p.next.val))
            p = p.next
            sum //= 10  # 下取整求进位
            print("sum//:{}".format(sum))
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next


if __name__ == '__main__':
    start = time.time()
    l1 = ListNode(2)
    l11 = ListNode(4)
    l111 = ListNode(3)
    l1.next = l11
    l11.next = l111

    l2 = ListNode(5)
    l22 = ListNode(6)
    l222 = ListNode(4)
    l2.next = l22
    l22.next = l222
    
    atn = Solution()
    atn.addTwoNumbers(l1, l2)
    
    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))