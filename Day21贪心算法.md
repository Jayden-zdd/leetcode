# 代码随想录算法第21天|贪心算法
## 学习的文章链接和视频链接
1. 理论基础 
https://programmercarl.com/%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html  
455. 分发饼干
https://programmercarl.com/0455.%E5%88%86%E5%8F%91%E9%A5%BC%E5%B9%B2.html  
376. 摆动序列  
https://programmercarl.com/0376.%E6%91%86%E5%8A%A8%E5%BA%8F%E5%88%97.html  
53. 最大子序和  
https://programmercarl.com/0053.%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%92%8C.html
## 看到题目的第一想法
1、不存在一块饼干给1个孩子后多余的给其他孩子情况，则就最大的给最大胃的孩子
2、三个数分别计算前2、后2的差值，相乘小于0就符合要求
## 实现过程中遇到哪些困难 
1、知道逻辑，没写，想直接看谈心算法的公式
2、尝试写了下，异常情况的处理：三个数据的平坡、尾部数据不好处理，绕晕了
## 看完代码随想录之后的想法 
贪心算法具体说不上来，就是局部最优到全局最优，感觉还是依赖数学推理能力
## 今日收获&学习时长
刷了2道题，学习时长3h，贪心算法不是重点，先忽略
```Python
# 455.分发饼干  
g.sort()
        s.sort()
        result = 0
        j = len(s) - 1 
        for i in range(len(g)-1,-1,-1):
            while j >= 0 and s[j] >= g[i]:
                result += 1
                j -= 1
                break
        return result
# 376. 摆动序列  
class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n 
        result = 1 #数组尾端默认有个1，比如[2,5]遍历2计算result=1，实际是2
        prediff = 0
        for i in range(n-1):
            curdiff = nums[i+1] - nums[i]
            if (prediff >= 0 and curdiff < 0 ) or (prediff <=0 and curdiff > 0): #prediff= 0 是有平坡的特殊处理，删除平坡左边的数据，比如[1,2,2,1]
                result += 1
                prediff = curdiff#摆动的时候更新prediff，比如[1,2,2,2,3,4]
        return result
    # 初始自我想法
    # def wiggleMaxLength(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     result = []
    #     i= 0
    #     while i < n-2:
    #         j = i + 1
    #         if j < n-1 and nums[j] == nums[i]:
    #             j += 1
    #         k = j + 1
    #         while k < n:
    #             res = cmpare(nums[i],nums[j],nums[k])
    #             if res:
    #                 result.append(nums[i])
    #                 result.append(nums[j])
    #                 i = k
    #                 break
    #             else:
    #                 k += 1
    #     return len(result)

    # def cmpare(a,b,c):
    #     if (b - a) * (b - c) < 0:
    #         return True
    #     else:
    #         return False

TODO：53   
```