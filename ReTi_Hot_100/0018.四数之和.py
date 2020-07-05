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
        
        nums.sort() # 排序

        for a in range(n-3):
            if(a>0 and nums[a]==nums[a-1]):
                continue
            for b in range(a+1, n-2):
                if (b>a+1 and nums[b]==nums[b-1]):
                    continue
                c = b+1
                d = n-1
                while c<d:
                    sum = nums[a]+nums[b]+nums[c]+nums[d]
                    if sum == target:
                        res.append([nums[a],nums[b],nums[c],nums[d]])
                        while c<d and nums[c]==nums[c+1]:
                            c += 1
                        while c<d and nums[d]==nums[d-1]:
                            d -= 1
                        c += 1
                        d -= 1
                    elif sum < target:
                        c += 1
                    else:
                        d -= 1
        
        return res

        
if __name__ == '__main__':
    start = time.time()
    
    nums = [-3,-2,-1,0,0,1,2,3]
    target = 0
    sfs = Solution()
    result = sfs.fourSum(nums, target)
    print("result = {}".format(result))
    
    end = time.time()
    delta = end - start
    logger.info("Finished time is {}".format(datetime.timedelta(seconds=delta)))