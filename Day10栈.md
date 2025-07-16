# 代码随想录算法第10天|栈
## 学习的文章链接和视频链接
1、https://programmercarl.com/0020.%E6%9C%89%E6%95%88%E7%9A%84%E6%8B%AC%E5%8F%B7.html
2、https://programmercarl.com/1047.%E5%88%A0%E9%99%A4%E5%AD%97%E7%AC%A6%E4%B8%B2%E4%B8%AD%E7%9A%84%E6%89%80%E6%9C%89%E7%9B%B8%E9%82%BB%E9%87%8D%E5%A4%8D%E9%A1%B9.html
3、https://programmercarl.com/0232.%E7%94%A8%E6%A0%88%E5%AE%9E%E7%8E%B0%E9%98%9F%E5%88%97.html
4、https://programmercarl.com/0225.%E7%94%A8%E9%98%9F%E5%88%97%E5%AE%9E%E7%8E%B0%E6%A0%88.html
## 看到题目的第一想法
1、栈实现队列、队列实现栈明白原理，代码写不出来
2、有效括号思路有，但是实现有点阻塞
## 实现过程中遇到哪些困难 
1、//和%弄混， //是取整操作，%才是取模
2、if not A表示A空执行
## 看完代码随想录之后的想法 
1、有效括号精髓在于左括号时进栈有括号，理清所有不匹配问题：多了左、多了右、左右不匹配
## 今日收获&学习时长
刷了2道题，学习时长1h，有左右对称关系的联想下栈
```Python
# 20 有效括号
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) % 2 == 1:
            return False
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            elif stack and c == stack[-1]:
                stack.pop()
            elif not stack or c != stack[-1]:
                return False
        if not stack:
            return True
        else:
            return False
# 1047 删除字符串相邻元素
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if not stack or c != stack[-1]:
                stack.append(c)
            else:
                stack.pop()
        return ''.join(stack)
# TODO：栈和队列的实现
```