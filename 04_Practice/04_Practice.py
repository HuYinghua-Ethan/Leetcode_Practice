"""
283. 移动零
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意 ，必须在不复制数组的情况下原地对数组进行操作。
示例 1:
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]

代码思路：
要解决这个问题，我们可以使用双指针法。一个指针用于遍历数组，另一个指针用于记录非零元素的位置。具体步骤如下：
初始化两个指针，current 用于遍历数组，non_zero 用于记录非零元素的位置。
遍历数组，当遇到非零元素时，将其与 non_zero 指针所指向的元素交换，并移动 non_zero 指针。
遍历结束后，所有非零元素都已按顺序排列在数组的前部，而 non_zero 指针之后的所有位置都应填充为零。

"""

class Solution(object):
    def moveZeroes(self, nums):
        last_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[last_zero_index], nums[i] = nums[i], nums[last_zero_index]
                last_zero_index += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12, 9, 6, 0]
    my_solution = Solution()
    my_solution.moveZeroes(nums)
    print(nums)




