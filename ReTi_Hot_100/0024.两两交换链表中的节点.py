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
        if not head or not head.next:
            return head
        
        p = head       # 第1个节点
        q = head.next # 第2个节点

        p.next = self.swapPairs(q.next)  # 每次递归都负责交换一对节点;下一次递归则是传递的是下一对需要交换的节点.若链表中还有节点,则继续递归.
        q.next = p   # 交换了两个节点以后,返回secondNode,因为它是交换后的新头;在所有节点交换完成以后,我们返回交换后的头,实际上是原始链表的第二个节点.
        return q

def create_listnode():
    head = ListNode(1)
    p = head

    for i in range(2, 6):
        q = ListNode(i)
        p.next = q
        p = q
    return head


if __name__ == '__main__':
    start = time.time()
    
    head = create_listnode()

    ssp = Solution()
    result = ssp.swapPairs(head)

    while result:
        print(result.val)
        result = result.next

    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))