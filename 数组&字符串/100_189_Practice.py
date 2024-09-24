"""
轮转数组
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。



示例 1:
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]

"""


"""
方法一：数组切片
1.处理 k 的值: 如果 k 大于数组长度，实际上可以使用 k % len(nums) 来计算真实需要轮转的步数，以避免多余的轮转。

2.切片操作:
将数组的最后 k 个元素取出。
将剩下的元素取出。
将这两个部分拼接起来。
"""

# class Solution:
#     def rotate(self, nums, k):
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         k = k % n
#         nums[:] = nums[-k:] + nums[:-k]
        
        

# if __name__ == "__main__":
#     nums = [1, 2, 3, 4, 5, 6, 7]
#     k = 3
#     mySolution = Solution()
#     mySolution.rotate(nums, k)
#     print(nums)


"""
方法二：数组切片
1.反转整个数组。
2.反转前 k 个元素。
3.反转剩下的 n-k 个元素。
"""

class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        # 步骤 1: 反转整个数组
        reverse(nums, 0, n - 1)
        # 步骤 2: 反转前 k 个元素
        reverse(nums, 0, k - 1)
        # 步骤 3: 反转后 n-k 个元素
        reverse(nums, k, n - 1)
        

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]  
        start += 1
        end -= 1
    

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    mySolution = Solution()
    mySolution.rotate(nums, k)
    print(nums)
