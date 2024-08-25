"""
11.盛最多水的容器
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
返回容器可以储存的最大水量。

输入：[1,8,6,2,5,4,8,3,7]
输出：49 


代码思路：
要解决这个问题，我们可以使用双指针法。双指针法的基本思路是从数组的两端开始，逐步向中间移动，以找到能够容纳最多水的两条线。具体步骤如下：
初始化两个指针，分别指向数组的两端，即 left = 0 和 right = n - 1。
计算当前两个指针所指向的线构成的容器的容量，即 min(height[left], height[right]) * (right - left)。
更新最大容量。
移动指针：如果 height[left] < height[right]，则移动左指针 left += 1，否则移动右指针 right -= 1。
重复步骤 2-4，直到两个指针相遇。
这种方法的时间复杂度是 O(n)，因为每个指针最多移动 n 次。


"""


class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_capacity = 0
        while left < right:
            current_capacity =  min(height[left], height[right]) * (right - left)
            max_capacity = max(max_capacity, current_capacity)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_capacity


if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    my_solution = Solution()
    max_water_capacity = my_solution.maxArea(height)
    print("容器可以储存的最大水量为 :", max_water_capacity)







