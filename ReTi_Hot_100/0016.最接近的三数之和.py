#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0016.最接近的三数之和.py
@Time    :   2020-06-28
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


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if 3 > n or n > 10**3 or -10**4 > target or target > 10**4:
            return
        
        nums.sort()
        closeSum = nums[0]+nums[1]+nums[2]  # 定义一个最近的值
        
        for i in range(n):
            if -10**3 > nums[i] or nums[i]>10**3:
                return
            
            if i > 0 and nums[i] == nums[i-1]:
                continue

            L = i + 1
            R = n - 1
            while L < R:
                threeSum = nums[i]+nums[L]+nums[R]  # 计算三个数的值

                if threeSum == target:
                    return target
                
                if abs(threeSum-target) < abs(closeSum-target): # 进行判断
                    closeSum = threeSum
                elif threeSum > target:
                    R -= 1
                else:
                    L += 1
        return closeSum


if __name__ == '__main__':
    start = time.time()
    
    nums = [-1,2,1,-4]
    target = 1
    stsc = Solution()
    result = stsc.threeSumClosest(nums, target)
    print("result : {}".format(result))

    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))