# 代码随想录算法第22天|回溯算法
## 学习的文章链接和视频链接
1、https://docs.qq.com/doc/DUEhsb0pUUm1WT2NP?nlc=1  
2、https://docs.qq.com/doc/DUExTYXVzU1BiU2Zl?nlc=1  
3、https://docs.qq.com/doc/DUElpbnNUR3hIbXlY?nlc=1  
4、https://docs.qq.com/doc/DUG1yVHdlWEdNYlhZ?nlc=1  
## 看到题目的第一想法
for循环遍历，但是几层for循环无法确定，所以不会
## 实现过程中遇到哪些困难 
for循环层数是变量，不好处理
## 看完代码随想录之后的想法 
1. 什么时候用回溯算法？  
暴力解法的for循环次数不是个定值，是个变量；
2. 回溯算法本质？  
回溯算法就是换成n插树结构，通过横向for循环，纵向递归方法来暴力解决问题，同时配合剪枝操作来优化，主要涉及组合、排列、子集问题
3. 回溯算法解题步骤？  
回溯三部曲：回溯函数入参和返回，返回一般为void；终止条件；单层逻辑处理
4. 回溯算法解决组合、子集、排列区别？  
* 组合：需要用startindex避免重复，结果是叶子节点，result保存在终止条件内
* 子集：结果不是叶子节点，是所有节点，所以result.append写在终止条件之前
* 排列：需要用used记录当前值，结果是叶子节点，result保存在终止条件内，最终used也要回溯
## 今日收获&学习时长
刷了4道题，学习时长3h，一轮刷题先不管剪枝优化，先保证题做出来;再次复习了list的copy、deepcopy
```Python
# 77组合
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backtracking(n, k, 1, [], result)
        return result

    def backtracking(self, n, k, startindex, path, result):
        if len(path) == k:
            # result.append(path) path是一个可变对象，result的最终结果都一样,[:]等同于浅copy,path里面的值是不可变对象
            result.append(path[:])
            return
        for i in range(startindex, n + 1):
            path.append(i)
            self.backtracking(n, k, i + 1, path, result)
            path.pop()
# 216 组合总和
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
        self.backtraking(self, k, n, 1, [], result)
        return result

    def backtraking(self, k, target_num, start_index, path, result):
        if len(path) == k and sum(path) == target_num:
            result.append(path[:])
            return
        for i in range(start_index, 9 + 1):
            path.append(i)
            self.backtraking(k, target_num, i + 1, path, result)
            path.pop()
# 78子集
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.backtraking(nums, 0, [], result)
        return result

    def backtraking(self, nums, start_index, path, result):
        result.append(path[:])  # 子集是保存所有节点的值，所以写在终止条件之前
        if len(path) == len(nums):
            return
        for i in range(start_index, len(nums)):
            path.append(nums[i])
            self.backtraking(nums, i + 1, path, result)
            path.pop()
# 46全排列
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)
        self.backtraking(nums, [], used, result)
        return result

    def backtraking(self, nums, path, used, result):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            else:
                used[i] = True
                path.append(nums[i])
                self.backtraking(nums, path, used, result)
                path.pop()
                used[i] = False  #一起回溯
# copy、deepcopy
list_o = [1, 2, 3, 4, ['a', 'b']]
list_1 = list_o[:]
list_o.append(5)
list_o[4].append("c")
print(list_o) #[1, 2, 3, 4, ['a', 'b', 'c'], 5]
print(list_1) # [1, 2, 3, 4, ['a', 'b', 'c']]
```



