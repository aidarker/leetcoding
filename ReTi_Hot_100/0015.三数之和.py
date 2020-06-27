#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0015.三数之和.py
@Time    :   2020-06-27
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


class Solution:
    def threeSum(self, nums):
        
        n=len(nums)
        res=[]
        if(not nums or n<3):
            return []
        
        nums.sort()

        for i in range(n):
            if nums[i] > 0:
                return res
            
            if(i>0 and nums[i]==nums[i-1]):
                continue
            
            L= i + 1
            R= n - 1
            while L < R:
                if(nums[i] + nums[L] + nums[R] == 0):
                    res.append([nums[i],nums[L],nums[R]])
                    
                    while(L<R and nums[L]==nums[L+1]):
                        L=L+1
                    
                    while(L<R and nums[R]==nums[R-1]):
                        R=R-1
                    
                    L=L+1
                    R=R-1
                
                elif(nums[i] + nums[L] + nums[R] > 0):
                    R=R-1
                
                else:
                    L=L+1
        return res


if __name__ == '__main__':
    start = time.time()
    
    nums = [3,0,-2,-1,1,2]
    sts = Solution()
    result = sts.threeSum(nums)
    print("result = {}".format(result))

    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))