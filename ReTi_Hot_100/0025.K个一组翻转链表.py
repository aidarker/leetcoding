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


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverse(self, head):
        pre = None
        curr = head
        while curr:
            nextNode = curr.next
            curr.next = pre
            pre = curr
            curr = nextNode
        return pre

    def reverseKGroup(self, head, k):
        """ 首先判断是否为空的情况 """
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head
        pre, end = dummy, dummy

        while end.next:
            # 取出待翻转的部分
            i = 0
            while i < k and end:
                end = end.next
                i += 1
            if not end: break

            # 断开链表
            startNode = pre.next
            nextNode = end.next
            end.next = None
            pre.next = self.reverse(startNode)  # 处理翻转
            startNode.next = nextNode   # startNode 转到翻转这部分节点的最后了, 连接断开的链表
            # 挪动以进行下一组处理
            pre = startNode
            end = pre
        return dummy.next


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

    k = 2
    srskg = Solution()
    result = srskg.reverseKGroup(head, 2)
    while result:
        print(result.val)
        result = result.next
        
    end = time.time()
    delta = end - start
    print("Finished time is {}".format(datetime.timedelta(seconds=delta)))