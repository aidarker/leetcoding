#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0023.合并k有序链表.py
@Time    :   2020-07-05
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
    """ 利用合并2个有序链表的方式 """
    def mergeKLists(self, lists):
        if not lists: return
        n = len(lists)
        if n == 1: 
            return lists[0]
        else:
            return self.merge(lists, 0, n-1)

    def merge(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = left + (right - left) // 2    # 分界点
        l1 = self.merge(lists, left, mid)   # l1
        l2 = self.merge(lists, mid+1, right)    # l2
        return self.mergeTwoLists(l1, l2)


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
    l11 = ListNode(4)
    l111 = ListNode(5)
    l1.next = l11
    l11.next = l111

    l2 = ListNode(1)
    l22 = ListNode(3)
    l222 = ListNode(4)
    l2.next = l22
    l22.next = l222

    l3 = ListNode(2)
    l33 = ListNode(6)
    l3.next = l33

    lists = [l1, l2, l3]
    smkl = Solution()
    result = smkl.mergeKLists(lists)

    while result:
        print(result.val)
        result = result.next
    
    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))