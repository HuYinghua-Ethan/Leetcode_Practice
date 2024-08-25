"""
438. 找到字符串中所有字母异位词
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。


代码思路：
可以使用滑动窗口算法结合普通的字典来实现找到字符串 s 中所有 p 的异位词的子串。这种方法不依赖于 collections 模块，更加基础。

具体步骤如下：
创建两个字典，分别用于记录字符串 p 中每个字符的频率，以及当前窗口中每个字符的频率。
初始化两个指针（left 和 right），表示当前窗口的左右边界。
移动右指针，扩大窗口，更新当前窗口的字符频率。
如果窗口大小等于 p 的长度，检查两个频率字典是否相同，如果相同，则找到一个异位词，记录左指针的位置。
移动左指针，缩小窗口，更新当前窗口的字符频率。


"""


class Solution(object):
    def findAnagrams(self, s, p):
        p_count = {} # 用于存储字符串 p 中每个字符的频率
        s_count = {} # 用于存储当前窗口每个字符的频率
        result = []  # 用于存储结果（异位词的起始索引）
        left = 0  # 窗口的左边界
        window_size = len(p) # 窗口的大小，等于字符串 p 的长度

        # 初始化 p_count
        for char in p:
            p_count[char] = p_count.get(char, 0) + 1  # dict.get(键， 默认值) 返回value, 若键不存在则返回默认值
        for right in range(len(s)):
            # 更新 s_count
            s_count[s[right]] = s_count.get(s[right], 0) + 1

            if right - left + 1 == window_size:  # 窗口大小等于 p 的长度
                # 检查两个字典是否相同
                if s_count == p_count:
                    result.append(left)
                
                # 移动左指针，更新 s_count
                s_count[s[left]] -= 1    
                if s_count[s[left]] == 0:
                    del s_count[s[left]]
                left += 1

        return result


if __name__ == "__main__":
    s = "cbaebabacd"
    p = "abc"
    my_solution = Solution()
    print(my_solution.findAnagrams(s, p))  # 输出：[0, 6]






