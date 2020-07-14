#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0025.py
@Time    :   2020-07-14
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
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or not head.next: return head
        
        p = head
        q = head.next




if __name__ == '__main__':
    start = time.time()
    
    head = ListNode(1)
    p1 = ListNode(2)
    p2 = ListNode(3)
    p3 = ListNode(4)
    p4 = ListNode(5)

    head.next = p1
    p1.next = p2
    p2.next = p3
    p3.next = p4

    k = 2
    srskg = Solution()
    srskg.reverseKGroup(head, k)
        
    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))