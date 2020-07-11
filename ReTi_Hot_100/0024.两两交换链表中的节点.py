#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0024.py
@Time    :   2020-07-11
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
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        


if __name__ == '__main__':
    start = time.time()
    
    #  1->2->3->4, 你应该返回 2->1->4->3.

    head = ListNode(1)
    p1 = ListNode(2)
    p2 = ListNode(3)
    p3 = ListNode(4)

    head.next = p1
    p1.next = p2
    p2.next = p3

    while head:
        print(head.val)
        head = head.next
    
    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))