"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。

要解决这个问题，我们可以使用双指针的方法来降低时间复杂度。具体步骤如下：

1.首先对数组进行排序。
2.遍历数组，对于每一个元素，使用双指针法寻找另外两个元素，使得三者之和为0。
3.为了避免重复的三元组，需要在遍历和移动指针时跳过重复的元素。
这个代码首先对数组进行排序，然后遍历数组，对于每一个元素，使用双指针法寻找另外两个元素，使得三者之和为0。
为了避免重复的三元组，代码在遍历和移动指针时跳过重复的元素。最终返回所有和为0且不重复的三元组。

跳过重复的元素是为了确保最终结果中不包含重复的三元组。具体原因如下：

1.避免重复结果：在排序后的数组中，如果当前元素与前一个元素相同，那么以当前元素为起点的所有可能的三元组都会与前一个元素为起点的三元组相同。因此，跳过重复元素可以避免生成重复的三元组。

2.提高效率：跳过重复元素可以减少不必要的计算，从而提高算法的效率。如果不跳过重复元素，算法会多次计算相同的三元组，这显然是浪费时间的。

举个例子，假设数组为 [-1, -1, 0, 1, 2, -4]，排序后为 [-4, -1, -1, 0, 1, 2]。如果不跳过重复元素，当遍历到第二个 -1 时，会生成与第一个 -1 相同的三元组，导致结果中包含重复的三元组。
通过跳过重复元素，可以确保每个三元组都是唯一的，从而满足题目要求。


在这段代码中，if i > 0 and nums[i] == nums[i - 1]: continue 用于跳过与前一个元素相同的当前元素。
在找到一个有效的三元组后，while left < right and nums[left] == nums[left + 1]: left += 1 和 while left < right and nums[right] == nums[right - 1]: right -= 1 用于跳过与当前 left 和 right 指针所指元素相同的元素，从而避免生成重复的三元组。

"""


class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result


                
if __name__ == '__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    my_solution = Solution()
    result = my_solution.threeSum(nums)
    print("三元组有 ", result)





