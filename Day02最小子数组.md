# 代码随想录算法第二天|leetcode209最小连续子数组
## 学习的文章链接和视频链接
题目链接：https://leetcode.cn/problems/minimum-size-subarray-sum/  
文章讲解：https://programmercarl.com/0209.%E9%95%BF%E5%BA%A6%E6%9C%80%E5%B0%8F%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84.html  
视频讲解：https://www.bilibili.com/video/BV1tZ4y1q7XE  
## 看到题目的第一想法
看错题目，我以为是最短数组，结果要求是连续的
## 实现过程中遇到哪些困难 
todo
## 看完代码随想录之后的想法 
todo
## 今日收获&学习时长
```Python
# 时间复杂度o（n），循环遍历
# 思考错了，题目要求是子数据则需要连续，我思考的是最短的数组
class Solution1:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        nums.sort(reverse=True)
        sum = 0
        for i in range(len(nums)):
            sum = sum + nums[i]
            if sum >= target:
                result = i + 1
                break
            else:
                continue
        if sum < target:
            result = 0
        return result

# 暴力解法，截取每个满足条件的子数组，计算长度，取最小；时间复杂度O(n2)超时
class Solution2:
    def minSubContinueArray(self, target, nums):
        result = 100001
        for i in range(len(nums)):
            sum_ = 0
            for j in range(i,len(nums)):
                sum_ =  sum_ + nums[j]
                if sum_ >= target:
                    sub_len = j - i + 1
                    result =  min(result,sub_len)
                    break
        return 0 if result == 10001 else result


# 滑动窗口
class Solution3:
    def minSubContinueArray(self, target, nums):
        return 0

if __name__ == "__main__":
    solution = Solution()
    target = 213
    nums = [12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]
    print(solution.minSubArrayLen(target, nums))
```