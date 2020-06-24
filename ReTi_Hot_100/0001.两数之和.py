#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   
@Time    :   2020-06-05
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
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 第一种方法
        # for i, value in enumerate(nums):
        #     for j in range(i+1, len(nums)):
        #         if (target - value) == nums[j]:
        #             return i, j

        # 第二种方法
        dict = {}
        lens = len(nums)
        for i in range(lens):
            if target - nums[i] in dict:
                return [dict[target - nums[i]], i]
            elif nums[i] not in dict:
                dict[nums[i]] = i

if __name__ == "__main__":
    st = Solution()
    nums = [2, 5, 7, 15]
    target = 9
    result = st.twoSum(nums, target)
    print(result)
