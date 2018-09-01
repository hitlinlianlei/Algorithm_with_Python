# reference https://blog.csdn.net/littlebai07/article/details/79100081
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        tmp = 0
        dic = dict()
        '''
        i 是当前字符位置，i - tmp是当前字符串起始位置。出现重复字符时，
        先判断字符上一次出现位置是否在当前字符串内，如果不在，则Map中更
        新位置并且tmp + +；如果在，则tmp截断，从上一次出现 + 1的位置开始计算。
        '''
        for i in range(len(s)):
            if s[i] not in dic.keys():
                dic[s[i]] = i
                tmp += 1
            else:
                t = dic[s[i]]
                if t + tmp < i:
                    tmp += 1
                else:
                    tmp = i - t
                dic[s[i]] = i
            print(dic,tmp)
            if tmp > max_len:
                max_len = tmp
        return max_len
test = Solution()
s = 'aaababc'
print(s)
print(test.lengthOfLongestSubstring(s))
'''
aaabbc
{'a': 0} 1
{'a': 1} 1
{'a': 2} 1
{'b': 3, 'a': 2} 2
{'b': 4, 'a': 2} 1
{'b': 4, 'a': 2, 'c': 5} 2
2
'''