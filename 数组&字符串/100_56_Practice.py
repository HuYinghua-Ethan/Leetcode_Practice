"""
合并区间
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

示例 1：
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2：
输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""

class Solution:
    def merge(self, intervals):
        if not intervals:
            return []
         # 先对区间按起始值排序
        intervals.sort(key=lambda x: x[0])
        merged = []
        current_interval = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= current_interval[1]:
                current_interval[1] = max(current_interval[0], intervals[i][1])
            else:
                merged.append(current_interval)
                current_interval = intervals[i]
        merged.append(current_interval)
        return merged
        

if __name__ == "__main__":
    intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    mySolution = Solution()
    result = mySolution.merge(intervals1)
    print(result)
