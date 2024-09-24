"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
子数组是数组中的一个连续部分。

示例 1：
输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

思路：
1.初始化两个变量: max_current 代表以当前元素结尾的最大子数组和，max_global 代表到目前为止找到的最大子数组和。

2.遍历数组: 从第一个元素开始遍历数组，对于每一个元素，更新 max_current 为当前元素与 max_current + current_element 的较大值。
这是因为我们要决定是否将当前元素加入到已有的子数组中，还是以当前元素作为新的子数组的起点。

3.更新全局最大值: 每次更新 max_current 的时候，也要检查是否更新 max_global。

4.返回结果: 遍历结束后，max_global即为所求的最大子数组和。

"""

class Solution:
    def maxSubArray(self, nums):
        max_current = max_global = nums[0]
        for i in range(len(nums)):
            max_current = max(nums[i], max_current + nums[i])  # 更新当前最大子数组和
            if max_current > max_global:
                max_global = max_current  # 更新全局最大值
        return max_global
            
        

if __name__ == "__main__":
    nums = nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    my_solution = Solution()
    output = my_solution.maxSubArray(nums)
    print(output)
    
