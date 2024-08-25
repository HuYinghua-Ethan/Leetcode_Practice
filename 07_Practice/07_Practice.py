"""
42. 接雨水
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

1.使用两个指针，分别从数组的两端开始向中间移动。
2.维护两个变量，分别记录左边和右边的最大高度。
3.比较两个指针所指的高度，优先处理较低的一侧，因为较低的一侧决定了当前位置能接多少雨水。
4.计算当前位置能接的雨水量，并累加到结果中。
更新最大高度，并移动指针。

这个代码首先初始化两个指针 left 和 right，分别指向数组的两端。然后使用 left_max 和 right_max 记录左边和右边的最大高度。在每次循环中，比较 left_max 和 right_max，优先处理较低的一侧，计算当前位置能接的雨水量，并累加到 water_trapped 中。最后返回 water_trapped 作为结果。

通过这种方法，可以高效地计算出给定高度图的柱子能接多少雨水。

"""

class Solution(object):
    def trap(self, height):
        if not height:
            return 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water_trap = 0
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water_trap += (left_max - height[left])
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water_trap += (right_max - height[right])
        return water_trap


if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    my_solution = Solution()
    print(my_solution.trap(height))
    

