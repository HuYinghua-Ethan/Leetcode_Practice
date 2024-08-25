"""
49.字母异位词分组
给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
字母异位词 是由重新排列源单词的所有字母得到的一个新单词。

 
示例 1:
输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]

代码思路：
1.同一个组的元素映射到同一组
2.属于不同组的元素不会映射到同一组
{排序后的字符串：源字符串集合}

"""

def groupAnagrams(strs):
    # 创建一个空字典，用于存储字母异位词组
    anagram_dict = {}
    
    # 遍历字符串数组
    for s in strs:
        sorted_s = ''.join(sorted(s))
        # 如果该键不存在于字典中，则创建一个新列表，并将当前字符串添加到该列表中
        if sorted_s not in anagram_dict:
            anagram_dict[sorted_s] = [s]
        # 如果该键已经存在于字典中，则将当前字符串添加到对应的列表中
        else:
            anagram_dict[sorted_s].append(s)
    
    # 将字典中的所有值（即列表）收集到一个结果列表中并返回
    return list(anagram_dict.values())
            
            
    
if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(groupAnagrams(strs))















