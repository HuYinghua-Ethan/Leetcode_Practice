"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
请必须使用时间复杂度为 O(log n) 的算法。


示例 1:
输入: nums = [1,3,5,6], target = 5
输出: 2


"""

class Solution:
    def searchInsert(self, nums, target):
        i, j = 0, len(nums) - 1
        while i <= j:
            m = (i + j) // 2
            if nums[m] < target:
                i = i + 1
            elif nums[m] > target:
                j = j - 1
            else:
                return m
        return i
        

if __name__ == "__main__":
    nums = [1,3,5,6]
    target = 4
    my_solution = Solution()
    print(my_solution.searchInsert(nums, target))
    


# 使用递归的方法实现二分查找
# class Solution:
#     def searchInsert(self, nums, target, left, right):
#         if left > right:
#             return left
#         mid = (left + right) // 2
#         if nums[mid] == target:
#             return mid
#         elif nums[mid] < target:
#             return self.searchInsert(nums, target, mid+1, right)
#         else:
#             return self.searchInsert(nums, target, left, mid-1)




# if __name__ == "__main__":
#     nums = [1,3,5,6]
#     target = 4
#     my_solution = Solution()
#     left = 0
#     right = len(nums) - 1
#     print(my_solution.searchInsert(nums, target, left, right))
    




















