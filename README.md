# 基础数据类型
## 不可变数据
### number
* 向上取整math.ceil(4.4)
* 向下取整math.floor(-0.3)=-1, 整除符号//
* 四舍五入round(4.4)，小数末尾为5的处理方法：当末尾的5的前一位为奇数：向绝对值更大的方向取整（5.5=>6）；当末尾的5的前一位为偶数：去尾取整（6.5=>6）
* 向0取整int(4.4)、int(-0.9)=0
### string
* split()默认为所有的空字符，包括空格、换行(\n)、制表符(\t)
### tuple
## 可变数据类型
### list
1. 初始化
a = []，b = [1,2,3]
2. 增删改查
* a.append('a')
* del a[0]
* a[1] = 'b'
* a[1]
3. 操作符
* a + b
* a * 4 a的值复制4遍
4. 切片
* a[start,stop,step]，step正数的时候[::2]start尽可能小，stop尽可能大;step负数的时候[::-2]，反过来start尽可能大，stop尽可能小
* b = a[:]等价于浅copy
5. 内置函数
* a.count(obj)统计某个元素在列表中出现的次数
* a.extend(b)不等价于a+b，extend的返回还是a，a+b的返回是c
* a.index(obj)从列表中找出某个值第一个匹配项的索引位置
* a.insert(index, obj)将对象插入列表
* a.pop()移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
* a.remove(obj)
* a.reverse()反向列表中元素
* a.sort(cmp=None, key=None, reverse=False)对原列表进行排序
### Dict：无序的不重复元素序列
1. 初始化
a = {} or a = dict()
2. 增删改查
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
* a['Sex'] = 'Man'
* del a['Class'],如果key不存在会报错
* a['Age'] = 8
* a["Name"],如果key不存在会报错
    * a.clear()
3. 内置方法
* dict.get(key, default=None)返回指定键的值，如果键不在字典中返回 default 设置的默认值
* key in dict如果键在字典dict里返回true，否则返回false
* dict.items() 以列表返回一个视图对象
* dict.keys() 返回一个视图对象
* dict.values() 返回一个视图对象
* dict.pop(key[,default])删除字典 key（键）所对应的值，返回被删除的值。
* dict.popitem()返回并删除字典中的最后一对键和值。
### Set
1. 初始化
a = set() or a = {'a','b',1,2} or a= set(("Google", "Runoob", "Taobao"))
2. 增删改查
* a.add('c') or a.update('c')
* a.discard('b')
    * a.remove('b') #若b不存在会报错，使用a.remove会报错，
    * a.pop()随机删除一个数
    * a.clear()清空集合
3. 集合运算
* 交集&
* 并集|
* 差集-
# 常用内置函数
* abs() 绝对值, ord('a') 字母的ascii码值，chr(97) = 'a'，
* divmod(7, 2) = (3, 1) 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)
* enumerate(sequence, [start=0])将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标,for index,value in enumerate(list)
* reverse() 函数用于反向列表中元素a.reverse()
* cmp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。
* map(function,iterable) 会根据提供的函数对指定序列做映射,第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表,map(square, [1,2,3,4,5]),map(lambda x: x ** 2, [1, 2, 3, 4, 5]


