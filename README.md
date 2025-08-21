# 基础数据类型
## 不可变数据
### number
* 向上取整math.ceil(4.4)
* 向下取整math.floor(-0.3)=-1, 整除符号//
* 四舍五入round(4.4)，小数末尾为5的处理方法：当末尾的5的前一位为奇数：向绝对值更大的方向取整（5.5=>6）；当末尾的5的前一位为偶数：去尾取整（6.5=>6）
* 向0取整int(4.4)、int(-0.9)=0
### string
1. 初始化
str = '' or str='hello'
2. 增删改查
* str3 = str1 + str2
* 删除修改不支持
* str[1] or str[1:4]
3. 内置函数
* 翻转字符转s[::-1] or ''.join(reversed(list))
* string.count(str, beg=0, end=len(string))返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数
* string.endswith(obj, beg=0, end=len(string))返回True和False
* string.find(str, beg=0, end=len(string))检测 str 是否包含在 string 中，如果 beg 和 end 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1
* string.index(str, beg=0, end=len(string))跟find()方法一样，只不过如果str不在 string中会报一个异常.
* string.join(seq)以 string 作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串
* string.replace(str1, str2,  num=string.count(str1))把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次.
* string.split(str="", num=string.count(str))以 str 为分隔符切片 string，如果 num 有指定值，则仅分隔 num+1 个子字符串，split()默认为所有的空字符，包括空格、换行(\n)、制表符(\t)
* format,"welcome to shanghai, dear {name}".format(name="baby")
### tuple
## 可变数据类型
### list
1. 初始化
a = []，b = [1,2,3]
2. 增删改查
* a.append('a')
* del a[0]根据下标删除;a.pop()移除列表中的一个元素（默认最后一个元素），并且返回该元素的值;a.remove(obj)根据值删除
* a[1] = 'b'
* a[1]
3. 操作符
* a + b
* a * 4 a的值复制4遍
4. 切片
* a[start,stop,step]，step正数的时候[::2]start尽可能小，stop尽可能大;step负数的时候[::-2]，反过来start尽可能大，stop尽可能小
* b = a[:]等价于浅copy
* list切片index超出长度不会报错，比如x=[1,2,3],x[1:6]会返回[2,3]
5. 内置函数
* 翻转字符串
    * list[::-1] 生成新的list
    * list.reverse() 原list直接更新
    * reversed(list)只是个迭代器，需要写成list(reversed(list)),也是生成新的list
* a.count(obj)统计某个元素在列表中出现的次数
* a.extend(b)不等价于a+b，extend的返回还是a，a+b的返回是c
* a.index(obj)从列表中找出某个值第一个匹配项的索引位置
* a.insert(index, obj)将对象插入列表
* a.reverse()反向列表中元素
* a.sort(cmp=None, key=None, reverse=False)对原列表进行排序
### Dict：无序的不重复元素序列
1. 初始化
a = {} or a = dict() or seq=('Google', 'Runoob', 'Taobao')，dict = dict.fromkeys(seq, 10)
2. 增删改查
tinydict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}
* a['Sex'] = 'Man'
* del a['Class'],如果key不存在会报错；a.clear()；dict.pop(key[,default])删除字典 key（键）所对应的值，返回被删除的值；dict.popitem()返回并删除字典中的最后一对键和值
* a['Age'] = 8
* a["Name"],如果key不存在会报错
3. 内置方法
* dict.get(key, default=None)返回指定键的值，如果键不在字典中返回 default 设置的默认值
* key in dict如果键在字典dict里返回true，否则返回false
* dict.keys() 返回一个视图对象
* dict.values() 返回一个视图对象
* dict.items() 以列表返回一个视图对象
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
# 数据类型转换
| 源类型      | 构造目标类型          | 示例代码                                      |
| ----------- | --------------------- | --------------------------------------------- |
| str         | list/tuple/set        | `list(s), tuple(s), set(s)`                   |
| list        | str                   | `"" .join(list)`                              |
| tuple       | str                   | `"" .join(tuple)`                             |
| list        | tuple/set             | `tuple(list), set(list)`                      |
| tuple       | list/set              | `list(tuple), set(tuple)`                     |
| list/tuple  | dict                  | `dict([('a', 1)])`                            |
| dict        | str/json              | `str(d), json.dumps(d)`                       |
| dict        | list/tuple/set（只键）   | `list(d), tuple(d), set(d)`                   |
| dict        | list/tuple/set（键值对） | `list(d.items()), tuple(d.items()), set(d.items())` |
| set         | list/tuple/str        | `list(set), tuple(set), "".join(set)`         |
# 常用内置函数
* abs() 绝对值, ord('a') 字母的ascii码值，chr(97) = 'a'，
* divmod(7, 2) = (3, 1) 函数把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)
* enumerate(sequence, [start=0])将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标,for index,value in enumerate(list)
* reverse() 函数用于反向列表中元素a.reverse()
* cmp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。
* map(function,iterable) 会根据提供的函数对指定序列做映射,第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表,map(square, [1,2,3,4,5]),map(lambda x: x ** 2, [1, 2, 3, 4, 5]
# 面试常遇到
* id()内存地址，a is b等价于id(a) == id(b)，==判断值是否相等
* *args 用于收集** 未命名的位置参数**，将它们打包成一个元组（tuple）传递给函数；**kwargs 用于收集 ** 命名的关键字参数 **，将它们打包成一个字典（dict）传递给函数
* filter、map、reduce 的作用
    * filter 函数用于过滤序列，它接收一个函数和一个序列，把函数作用在序列的每个元素上，然后根据返回值是True还是False决定保留还是丢弃该元素list(filter(lambda x: x % 2 == 1, range(10))) = [1, 3, 5, 7, 9]
    * map函数传入一个函数和一个序列，并把函数作用到序列的每个元素上，返回一个可迭代对象。list(map(lambda x: x % 2, range(10)))=[0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    * reduce函数用于递归计算，同样需要传入一个函数和一个序列，并把函数和序列元素的计算结果与下一个元素进行计算reduce(lambda x, y: x + y, range(101)) = 5050
* zip将可迭代对象打包成元组，list(zip(list1, list2))
* 生成器、迭代器
    * 迭代器是实现了迭代协议的对象，用于逐个访问集合中的元素，无需一次性加载所有数据到内存；主要实现__iter__（）方法返回迭代器自身，__next__（）方法返回下一个元素，常见迭代器文件对象（每次读取一行）、enumerate()、zip()等函数的返回值
    * 生成器是特殊的迭代器，通过yield关键字简化了迭代器的创建；return返回后终止函数并返回具体值，yield暂停函数下次调用会从暂停处继续，最终返回生成器对象，需要迭代获取值
* 闭包、装饰器
    * 闭包是一种函数嵌套结构，内部函数调用了外部函数的变量，外部函数的返回是内部函数；外部函数执行结束，内部变相也不会被销毁，会被内部函数记住并持续使用
    * 装饰器：允许在不修改原函数代码的前提下，为函数或类添加额外功能。它本质上是一个接收函数作为参数并返回新函数的可调用对象，广泛用于日志记录、性能测试、权限验证等场景
    ```python
    # 定义装饰器
    def my_decorator(func):
        def wrapper():
            print("函数执行前的操作")  # 额外功能
            func()  # 调用原函数
            print("函数执行后的操作")  # 额外功能
        return wrapper
    # 应用装饰器,@my_decorator 等价于 say_hello = my_decorator(say_hello)，即原函数被装饰器返回的 wrapper 函数替代
    @my_decorator      
    def say_hello():    
        print("Hello, World!")
    say_hello()
    ```
* GLI和进程、线程、协程
    * GLI是全局解释器锁，主要作用是python解释器执行代码时会获取GLI锁，线程执行一段时间or遇到io操作才释放GLI让其他线程执行；
    * CPU 密集型任务（如大量计算）：多线程效率低，因为线程切换会争夺 GIL，反而增加开销。此时更适合用多进程（每个进程都有自己的Python解释器和独立的 GIL）；
    * 低并发I/O 密集型任务（如网络请求、文件读写）：多线程影响较小，因为线程在等待 I/O 时会释放 GIL，其他线程可获取锁执行，低并发时比较合适
    * 高并发I/O密集型任务（如高并发服务器、爬虫）：优先使用协程asyncio实现协程，async定义协程函数，await暂停当前协程，让执行权给其他协程
* python内存管理，python内存是自动进行，主要通过实现内存分配释放、引用计数、垃圾回收机制管理，无需开发者手动操作
    * 内存分配：小型对象如整数、短字符串会内存中预分配一块地址；大型对象是直接向操作系统申请内存
    * 引用计数：每个对象被引用的次数，当次数为0时自动释放内存，比如函数执行结束局部变量引用-1，对象在容器中移除pop或者删除变量del都会-1
    * 垃圾回收机制：引用计数没法解决循环引用问题，通过标记-清除算法（标记阶段：从根对象（如全局变量、栈中的变量）出发，标记所有可达对象；清除阶段：未被标记的对象（不可达，如循环引用的孤立对象）被判定为垃圾，释放其内存）和分代回收（新创建的对象为 0 代，回收频率最高）处理循环引用
* python对象：对象由属性和方法组成，类是对象的抽象模版，实例是类的具体实现，对象的三大核心封装、继承、多态
    * 封装：隐藏对象内部细节，暴露必要的接口操作私有属性和方法，私有属性和方法以双下划线__开头，只能在类内部访问
    ```python
    class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance  # 私有属性（外部无法直接访问）
    # 公有方法：操作私有属性
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return f"存款成功，余额：{self.__balance}"
        return "存款金额必须为正数"
    account = BankAccount(1000)
    print(account.deposit(500))   # 存款成功，余额：1500
    print(account.__balance)      # 报错（外部无法直接访问私有属性）
    ```
    * 继承：子类可以继承父类的属性和方法，并可以代码复用扩展新功能；python重写就是同名函数、同入参列表实现覆盖父类的实现；重载不支持，同名方法会覆盖前一个
    ```python
    # 父类
    class Animal:
        def __init__(self, name):
            self.name = name
        def speak(self):
            return "动物发出声音"
    # 子类继承父类
    class Dog(Animal):
        # 重写父类方法
        def speak(self):
            super().greet()  # 调用父类的方法，动物发出声音
            return f"{self.name}汪汪叫"
    dog = Dog("旺财") #继承属性和方法
    print(dog.speak())  # 旺财汪汪叫
    ```
    * 多态：不同类的对象调用同名方法时，会表现出不同的行为，即 “同一接口，多种实现”，用统一接口处理不同对象，避免大量if-else判断，如果没有多态，make_sound 可能需要写成 if isinstance(animal, Dog): ... elif isinstance(animal, Cat): 
    ```python
    # 父类（可选，非必须）
    class Animal:
        def speak(self):
            # 父类方法可作为默认实现或抽象声明
            raise NotImplementedError("子类必须实现speak方法")
    # 子类1：狗
    class Dog(Animal):
        def speak(self):  # 重写speak方法
            return "汪汪汪"
    # 子类2：猫
    class Cat(Animal):
        def speak(self):  # 重写speak方法
            return "喵喵喵"
    # 子类3：鸭子（即使不继承Animal，只要有speak方法也能参与多态）
    class Duck:
        def speak(self):
            return "嘎嘎嘎"
    # 统一接口：接收任意"会叫"的对象
    def make_sound(animal):
        print(animal.speak())  # 调用同名方法，表现不同行为
    # 创建不同对象
    dog = Dog()
    cat = Cat()
    duck = Duck()
    # 调用同一接口，输出不同结果（多态）
    make_sound(dog)   # 汪汪汪
    make_sound(cat)   # 喵喵喵
    make_sound(duck)  # 嘎嘎嘎
    ```
* python类的实例方法、类方法、静态方法
    ```Python
    class Person:  # 定义类
        species = "人类"  # 类属性（所有实例共享）
        def __init__(self, name):  # 初始化方法（构造函数）
            self.name = name  # 实例属性（每个实例独有），self表示实例本身
        #1、实例方法
        def greet(self):
            return f"你好，我是{self.name}"
        #2、类方法：访问类属性
        @classmethod
        def get_species(cls):
            return f"物种：{cls.species}"  # cls表示类本身
        #2、类方法：修改类属性
        @classmethod
        def set_species(cls, new_species):
            cls.species = new_species
        # 通过类调用print(Person.get_species())  # 物种：人类 Person.set_species("智人")
        # 通过实例调用（同样操作类属性） p = Person("Bob") print(p.get_species())
        #3、静态方法
        @staticmethod
        def add(a, b):
            return a + b
        # 通过类调用print(MathUtils.add(2, 3))      
        # 通过实例调用mu = MathUtils() print(mu.add(4, 5))  
    ```
    * 实例方法：第一个参数必须是self，通过p.greet()访问和修改实例属性或者调用其他实例方法，只能通过实例调用
    * 类方法： @classmethod装饰器，第一个参数必须是 cls（代表类本身，名称约定为 cls），主要用于操作类属性，可以通过类和实例调用
    * 静态方法：用@staticmethod装饰器，没有强制的第一个参数，与类和实例都无关，更像是类内部的 “普通函数”，仅为了代码组织而放在类中，可以通过类和实例调用
* 设计模式
    * 单例模式：一个类只有一个实例，并提供一个全局访问点来访问这个实例；应用场景如下
        1. 资源共享：应用程序需要一个全局的配置管理器来存储和管理配置信息、亦或是使用单例模式管理数据库连接池
        2. 只有一个实例：说管理应用程序中的缓存，确保只有一个缓存实例，避免重复的缓存创建和管理，或者使用单例模式来创建和管理线程池
        ```python
        # 饿汉模式
        class Singleton:
        instance = None
        def __init__(self):
            if Singleton.instance is not None:
                raise Exception("Only one instance of Singleton class is allowed")
            else:
                Singleton.instance = self
        # 懒汉模式
        class Singleton:
        __instance: Singleton = None
        @staticmethod
        def getInstance():
            if Singleton.__instance is None:
        Singleton.__instance = Singleton()
            return Singleton.__instance


