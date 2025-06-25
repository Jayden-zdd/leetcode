# 代码随想录算法第一天|leetcode704二分查找
## 学习的文章链接和视频链接
基础理论：https://programmercarl.com/%E6%95%B0%E7%BB%84%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html
题目链接：https://leetcode.cn/problems/binary-search/
文章讲解：https://programmercarl.com/0704.%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.html
视频讲解：https://www.bilibili.com/video/BV1fA4y1o715
## 看到题目的第一想法
1. for循环遍历输出下标，时间复杂度O(n);
2. 仔细一看需要logN，就想到二分法，写的过程中未关闭copilot插件，导致有提示就写出来了
## 实现过程中遇到哪些困难 
1. 第一时间还怀疑len(nums)是偶数还是奇数有点关系，演练后确认无关
2. mid中间index向下取整时已忘记基本语法，顺便回顾
* 向上取整math.ceil(4.4)、
* 向下取整math.floor(-0.3)=-1, 整除符号//
* 四舍五入round(4.4)，小数末尾为5的处理方法：当末尾的5的前一位为奇数：向绝对值更大的方向取整（5.5=>6）；当末尾的5的前一位为偶数：去尾取整（6.5=>6）
* 向0取整int(4.4)、int(-0.9)=0
## 看完代码随想录之后的想法 
在copilot的帮助下虽然写出来提交了ac，但是看完视频才发现坑在哪，左闭右开，左闭右闭才是核心
## 今日收获&学习时长
刷了一道题，回顾了python的取整，写文档也也回顾的md文档的格式，学习时长1.5h
```Python
# 时间复杂度o（n），循环遍历
class Solution1:
    def search(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

# 时间复杂度o(logn) ，左闭右闭区间
class Solution2:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:  # 注意=场景，左闭右闭区间
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return -1

# 时间复杂度o(logn)，左闭右开区间，right初始值、后续赋值不同
class Solution3:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:  
            mid = (left + right) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                right = mid
            else:
                left = mid + 1
        return -1

if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    solution = Solution1()
    result = solution.search(nums, target)
    print(result)  # Output: 4
    print(round(5.5))  # Output: 6
    print(round(6.5))  # Output: 6
```