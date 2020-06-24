#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   04.py
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

'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 我们总是把短数组作为第一个
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        integer_MIN_VALUE = -2**32
        integer_MAX_VALUE = 2**31-1

        m, n = len(nums1), len(nums2)
        # 计算分割线左边的所有元素需要满足的个数 m + (n - m +1) / 2
        totalLeft = (m + n + 1) // 2
        # 在 nums1 的区间 [0, m] 里面找恰当的分割线
        # 使得 nums1[i-1] <= nums2[j] && nums2[j-1] <= nums1[i]
        left, right = 0, m
        
        # 第一种方式
        while (left < right):
            i = left+(right-left+1) // 2
            j = totalLeft - i
            if (nums1[i-1] > nums2[j]):
                # 下一轮搜索的区间 [left, i-1]
                right = i -1
            else:
                # 下一轮搜索的区间 [i, right]
                left = i

        # 第二种方式
        # while (left < right):
        #     i = left + (right-left) // 2
        #     j = totalLeft-i
            
        #     if (nums2[j-1] > nums1[i]):
        #         left = i + 1
        #     else:
        #         right = i

        i = left
        j = totalLeft - i
        nums1_Left_Max = (integer_MIN_VALUE if i==0 else nums1[i-1])
        nums1_Right_Min = (integer_MAX_VALUE if i==m else nums1[i])
        nums2_Left_Max = (integer_MIN_VALUE if j==0 else nums2[j-1])
        nums2_Right_MIN = (integer_MAX_VALUE if j==n else nums2[j])

        if (m+n)%2 == 1:
            return max(nums1_Left_Max, nums2_Left_Max)
        else:
            return (max(nums1_Left_Max, nums2_Left_Max)+min(nums1_Right_Min, nums2_Right_MIN))/2
'''


class Solution(object):
    """ 划分数组 """
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        m, n = len(nums1), len(nums2)
        MIN_VALUE, MAX_VALUE = -2**32, 2**32-1
        left, right = 0, m
        median1, median2 = 0, 0
        while left<=right:
            i = (left+right) // 2
            j = (m+n+1) // 2 - i

            nums1_left  = (MIN_VALUE if i==0 else nums1[i-1])
            nums1_right = (MAX_VALUE if i==m else nums1[i])
            nums2_left  = (MIN_VALUE if j==0 else nums2[j-1])
            nums2_right = (MAX_VALUE if j==n else nums2[j])

            if nums1_left <= nums2_right:
                median1, median2 = max(nums1_left, nums2_left), min(nums1_right, nums2_right)
                left = i + 1
            else:
                right = i -1
        
        return (median1+median2)/2 if (m+n)%2==0 else median1


if __name__ == '__main__':
    start = time.time()
    
    nums1 = [1, 2]
    nums2 = [3, 4]
    sfmsa = Solution()
    result = sfmsa.findMedianSortedArrays(nums1, nums2)
    print(result)

    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))