"""
给你一个满足下述两条属性的 m x n 整数矩阵：

每行中的整数从左到右按非严格递增顺序排列。
每行的第一个整数大于前一行的最后一个整数。
给你一个整数 target ，如果 target 在矩阵中，返回 true ；否则，返回 false 。

输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true


由于矩阵每行的元素是非严格递增的，并且每行的第一个元素大于前一行的最后一个元素，
我们可以将整个矩阵视为一个有序的线性数组，
从而使用二分查找来加速查找过程。
"""




class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1
        while left <= right:
            mid = (left + right) // 2
            mid_value = matrix[mid // cols][mid % cols]
            if mid_value == target:
                return True
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1
        return False


if __name__ == "__main__":
    matrix = [[1,3,5,7],
          [10,11,16,20],
          [23,30,34,60]]
    target = 20
    my_solution = Solution()
    print(my_solution.searchMatrix(matrix, target))  # 输出: True



