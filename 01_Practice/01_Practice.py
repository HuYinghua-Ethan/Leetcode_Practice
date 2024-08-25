"""
两数之和

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
你可以按任意顺序返回答案。

代码思路：
要解决这个问题，可以使用哈希表（字典）来提高查找效率。具体步骤如下：
1.创建一个哈希表，用于存储数组中的元素及其对应的下标。
2.遍历数组，对于每个元素，计算其与目标值的差值。
3.检查差值是否已经在哈希表中，如果在，则找到了两个数，返回它们的下标。
4.如果不在哈希表中，将当前元素及其下标存入哈希表。

"""


class Solution(object):
    def twoSum(self, nums, target):
        my_dict = {}
        for i in range(len(nums)):
            if target - nums[i] in my_dict:
                return [my_dict[target - nums[i]], i]
            my_dict[nums[i]] = i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    result = []
    my_solution = Solution()
    result = my_solution.twoSum(nums, target)
    print("两个整数的下标为 :", result)
            

