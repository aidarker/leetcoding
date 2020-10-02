#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@File    :   0030_串联所有单词的子串.py
@Time    :   2020-10-02
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
    def findSubString(self, s, words):
        """ """
        if not words:
            return []
        w_len, s_len = len(words[0]), len(s)
        t_len = w_len * len(words)  # 子串的长度
        
        word_dict = {}  # words的哈希表
        for word in words:
            word_dict[word] = word_dict.get(word, 0) + 1
        
        ans = []
        for offset in range(w_len):
            lo, lo_max = offset, s_len-t_len
                       
            while lo<=lo_max:
                tmp_dict = word_dict.copy()
                match = True
                for hi in range(lo+t_len, lo, -w_len):  # 从尾到头搜索单词
                    word = s[hi-w_len: hi]
                    if word not in tmp_dict or tmp_dict.get(word, 0) == 0:
                        match = False
                        break
                    tmp_dict[word] -= 1
                if match:
                    ans.append(lo)
                lo = hi
        return ans


if __name__ == '__main__':
    start = time.time()
    
    # s = "barfoothefoobarman"
    # words = ["foo","bar"]
    s = "wordgoodgoodgoodbestword"
    words = ["word","good","best","word"]
    sfss = Solution()
    result = sfss.findSubString(s, words)
    print(result)

    end = time.time()
    delta = end - start
    print("Finished time is {}".format(datetime.timedelta(seconds=delta)))