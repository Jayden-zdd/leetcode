# 代码随想录算法第11天|队列
## 学习的文章链接和视频链接
150. 逆波兰表达式求值 
本题不难，但第一次做的话，会很难想到，所以先看视频，了解思路再去做题 
题目链接/文章讲解/视频讲解：https://programmercarl.com/0150.%E9%80%86%E6%B3%A2%E5%85%B0%E8%A1%A8%E8%BE%BE%E5%BC%8F%E6%B1%82%E5%80%BC.html  
239. 滑动窗口最大值 （有点难度，可能代码写不出来，但一刷至少需要理解思路）
之前讲的都是栈的应用，这次该是队列的应用了。
本题算比较有难度的，需要自己去构造单调队列，建议先看视频来理解。 
题目链接/文章讲解/视频讲解：https://programmercarl.com/0239.%E6%BB%91%E5%8A%A8%E7%AA%97%E5%8F%A3%E6%9C%80%E5%A4%A7%E5%80%BC.html 
347. 前K个高频元素（有点难度，可能代码写不出来，一刷至少需要理解思路）
大/小顶堆的应用， 在C++中就是优先级队列 
本题是 大数据中取前k值 的经典思路，了解想法之后，不算难。
题目链接/文章讲解/视频讲解：https://programmercarl.com/0347.%E5%89%8DK%E4%B8%AA%E9%AB%98%E9%A2%91%E5%85%83%E7%B4%A0.html  
## 看到题目的第一想法
1、第一个继续栈就行了
2、暴力解法超时
3、list转成dict（出现次数：元素），排序查找
## 实现过程中遇到哪些困难 
1、操作元素加减乘除不会，搜索了下需要from operator import add、sub、mul，但是远不如lambda表达式方便
3、list=>dict不会操作
## 看完代码随想录之后的想法 
1、大致看了思路，二刷再看吧
## 今日收获&学习时长
刷了1道题，学习时长1h，还是复习的栈
```Python
# 20 有效括号
stack = []
        op_map = {'+': lambda a,b: a+b,'-':lambda a,b:a-b, '*':lambda a,b:a*b,'/':lambda a,b: int(a/b)}

        for token in tokens:
            if token in ['+','-','*','/']:
                last = stack.pop()
                first = stack.pop()
                temp = op_map[token](first,last)
                stack.append(temp)
            else:
                stack.append(int(token))
        return stack.pop()
# TODO：队列的应用
```