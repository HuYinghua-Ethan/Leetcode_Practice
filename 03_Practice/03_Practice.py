"""
128. 最长连续序列
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

示例：
输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。

代码思路：
要解决这个问题，我们可以使用哈希集合（HashSet）来实现时间复杂度为 O(n) 的算法。具体步骤如下：
将数组中的所有元素放入一个哈希集合中，这样可以实现 O(1) 的查找时间。
遍历数组中的每个元素，对于每个元素，检查其前一个元素（即 num - 1）是否在哈希集合中。如果不在，说明当前元素是一个潜在的连续序列的起点。
从当前元素开始，不断检查其下一个元素（即 num + 1）是否在哈希集合中，直到找不到下一个元素为止。记录这个连续序列的长度。
更新最长连续序列的长度。


"""


class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        
        nums_set = set(nums)
        longest_streak = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                current_streak = 1
                
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak, current_streak)
        return longest_streak
        



if __name__ == "__main__":
    nums = [100, 4, 200, 1, 3, 2]
    my_solution = Solution()
    print(f"最长数字连续序列长度为{my_solution.longestConsecutive(nums)}")


