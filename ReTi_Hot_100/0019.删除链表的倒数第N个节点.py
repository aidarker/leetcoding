#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0019.删除链表的倒数第N个节点.py
@Time    :   2020-07-04
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
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first, second = dummy, dummy
        for _ in range(n+1):
            first = first.next
        while first != None:
            first = first.next
            second = second.next
        second.next = second.next.next
        return dummy.next


if __name__ == '__main__':
    start = time.time()

    head = ListNode(1)
    h1 = ListNode(2)
    h2 = ListNode(3)
    h3 = ListNode(4)
    h4 = ListNode(5)

    head.next = h1
    h1.next = h2
    h2.next = h3
    h3.next = h4

    srNfe = Solution()
    n = 2
    result = srNfe.removeNthFromEnd(head, n)
    while result:
        print(result.val)
        result = result.next
    
    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))