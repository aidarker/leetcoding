#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0031_下一个排列.py
@Time    :   2020-10-12
@Author  :   KouKai
@Version :   V1.0
@Remarks :   None
'''

import datetime
import time
import sys
import os
path = os.getcwd()
path = os.path.dirname(path)
sys.path.append(path)


class Solution(object):
    def nextPermutation(self, nums):
        """ """
        n = len(nums)
        if n < 2:
            return nums
        
        i = n-1
        while i > 0 and nums[i-1] >= nums[i]:   # 要是前者大于等于后者 则不是要调整的目标 继续前移  ！第一遍出错就是这儿没有等于
            i -= 1
        if i == 0 and nums[i] == max(nums):     # 此数为最大数
            nums.reverse()
            return nums
        else:
            j = n-1
            while j > i-1 and nums[j] <= nums[i-1]:
                j -= 1
            
            # 交换位置
            nums[i-1], nums[j] = nums[j], nums[i-1]

            re = nums[i:]
            for h in range(len(re)):
                nums[n-1-h] = re[h]
            
            return nums


# class Solution:
#     def nextPermutation(self, nums):
#         """
#         Do not return anything, modify nums in-place instead.
#         """

#         if len(nums) < 2:
#             return

#         for i in range(len(nums) - 2, -1, -1):
#             if nums[i] < nums[i + 1]:
#                 for j in range(len(nums) - 1, i, -1):
#                     if nums[j] > nums[i]:
#                         nums[i], nums[j] = nums[j], nums[i]
#                         break
#                 nums[i + 1:] = sorted(nums[i + 1:])
#                 return
        
#         nums.sort()
#         return nums


if __name__ == '__main__':
    start = time.time()

    snp = Solution()
    nums = [1, 1, 5]
    result = snp.nextPermutation(nums)
    print("result: {}".format(result))

    end = time.time()
    delta = end - start
    print("Finished time is {}".format(datetime.timedelta(seconds=delta)))
