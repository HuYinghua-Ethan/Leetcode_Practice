"""
3. 无重复字符的最长子串
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串的长度。

示例 :
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

代码思路：
要找出字符串中不含有重复字符的最长子串的长度，可以使用滑动窗口算法。滑动窗口算法通过维护一个窗口，该窗口包含的字符没有重复，并且通过调整窗口的左右边界来找到最长的无重复字符子串。

具体步骤如下：

使用两个指针（left 和 right）来表示当前窗口的左右边界。
使用一个集合（或字典）来记录当前窗口中出现的字符。
移动右指针，扩大窗口，直到遇到重复字符。
如果遇到重复字符，移动左指针，缩小窗口，直到窗口中没有重复字符。
记录每次窗口的最大长度。



"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_set = set()
        left = 0
        max_length = 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        return max_length


if __name__ == "__main__":
    s = "abcabcbb"
    my_solution = Solution()
    max_length = my_solution.lengthOfLongestSubstring(s)
    print("不含有重复字符的 最长 子串的长度为 ", max_length)



