#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0033.搜索旋转排序数组.py
@Time    :   2020-10-23
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

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """ 利用二分查找思想+条件判断 """
        if not nums:
            return -1
        
        low, high = 0, len(nums)-1
        while low<=high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid
            
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    high = mid -1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums)-1]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

if __name__ == '__main__':
    start = time.time()
    
    s = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    result = s.search(nums, target)
    print(result)

    end = time.time()
    delta = end - start
    print("Finished time is {}".format(datetime.timedelta(seconds=delta)))