#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   21_合并两个有序列表.py
@Time    :   2020-06-05
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


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l2.next, l1)
            return l2


if __name__ == '__main__':
    start = time.time()
    l1 = ListNode(1)
    l11 = ListNode(2)
    l111 = ListNode(4)
    l1.next = l11
    l11.next = l111

    l2 = ListNode(1)
    l22 = ListNode(3)
    l222 = ListNode(4)
    l2.next = l22
    l22.next = l222
    
    atn = Solution()
    result = atn.mergeTwoLists(l1, l2)
    
    while result:
        print(result.val)
        result = result.next

    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))