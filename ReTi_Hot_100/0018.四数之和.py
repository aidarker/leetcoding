#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0018.四数之和.py
@Time    :   2020-06-29
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
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n=len(nums)
        res=[]
        if(not nums or n<4):
            return res
        
        nums.sort()
        for i in range(n):
            if(i>0 and nums[i]==nums[i-1]):
                continue
            
            L = i + 1
            R = n - 1
            while L < R:
                if(nums[i] + nums[L] + nums[R] == 0):
                    res.append([nums[i],nums[L],nums[R]])
                    
                    while(L<R and nums[L]==nums[L+1]):  L += 1 # 为了排除三个相等数据,超过原始该数据的个数
                    while(L<R and nums[R]==nums[R-1]):  R -= 1 # 为了排除三个相等数据,超过原始该数据的个数
                    L += 1
                    R -= 1
                elif(nums[i] + nums[L] + nums[R] > 0):
                    R -= 1
                else:
                    L += 1
        return res

        
if __name__ == '__main__':
    start = time.time()
    
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    sfs = Solution()
    sfs.fourSum(nums, target)
    
    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))