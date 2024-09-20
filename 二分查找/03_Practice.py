"""
给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
如果数组中不存在目标值 target，返回 [-1, -1]。
你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。

示例 1：
输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]


如果是查找 target 最左边的位置，调整右边界
如果是查找 target 最右边的位置，调整左边界

"""


class Solution:
    def searchRange(self, nums, target):
        start = findBoundray(nums, target, True)
        if start == -1:
            return [-1, -1]
        end = findBoundray(nums, target, False)
        return [start, end]
        

def findBoundray(nums, target, is_first):
    left, right = 0, len(nums) - 1
    boundray_position = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            boundray_position = mid
            if is_first:
                right = mid - 1
            else:
                left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return boundray_position
            

if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    my_solution = Solution()
    print(my_solution.searchRange(nums, target))  # 输出: [3, 4]
    target = 6
    print(my_solution.searchRange(nums, target))  # 输出: [-1, -1]


 