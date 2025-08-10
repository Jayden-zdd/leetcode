import time
from functools import wraps


# 函数执行时间
def calculate_execution_time(func):
    """计算函数执行时间的装饰器"""

    @wraps(func)  # 保留原函数的元信息
    def wrapper(*args, **kwargs):
        # 记录开始时间
        start_time = time.perf_counter()

        # 执行原函数
        result = func(*args, **kwargs)

        # 记录结束时间并计算差值
        end_time = time.perf_counter()
        execution_time = end_time - start_time

        # 输出执行时间信息
        print(f"函数 {func.__name__} 执行时间: {execution_time:.6f} 秒")

        # 返回原函数的执行结果
        return result

    return wrapper


# 使用示例
@calculate_execution_time
def example_function(n):
    """示例函数：计算1到n的和"""
    total = 0
    for i in range(n):
        total += i
    return total


# 调用函数
example_function(1000000)  # 输出类似: 函数 example_function 执行时间: 0.045678 秒


# 函数添加log
import logging
from functools import wraps
from datetime import datetime

# 配置日志：设置格式、级别和输出方式
logging.basicConfig(
    level=logging.INFO,  # 日志级别：DEBUG/INFO/WARNING/ERROR/CRITICAL
    format="%(asctime)s - %(levelname)s - %(message)s",  # 日志格式
    handlers=[
        logging.StreamHandler()  # 输出到控制台，可添加FileHandler输出到文件
        # logging.FileHandler("app.log", encoding="utf-8")  # 输出到文件
    ],
)


def log_decorator(func):
    """为函数添加日志的装饰器，记录调用、参数、返回值和异常"""

    @wraps(func)  # 保留原函数的元信息（如函数名、文档字符串）
    def wrapper(*args, **kwargs):
        # 记录函数开始调用的日志
        func_name = func.__name__
        logging.info(f"开始调用函数: {func_name}")
        logging.info(f"参数: args={args}, kwargs={kwargs}")

        try:
            # 执行原函数并获取返回值
            result = func(*args, **kwargs)
            # 记录函数成功执行及返回值
            logging.info(f"函数 {func_name} 执行成功，返回值: {result}")
            return result
        except Exception as e:
            # 记录函数执行异常
            logging.error(f"函数 {func_name} 执行失败，异常: {str(e)}", exc_info=True)
            # 重新抛出异常，不影响原函数的异常处理逻辑
            raise

    return wrapper


# 示例1：普通函数
@log_decorator
def add(a, b):
    """计算两个数的和"""
    return a + b


add(3, 5)
# 输出日志：
# 2023-10-01 12:00:00,123 - INFO - 开始调用函数: add
# 2023-10-01 12:00:00,124 - INFO - 参数: args=(3, 5), kwargs={}
# 2023-10-01 12:00:00,124 - INFO - 函数 add 执行成功，返回值: 8


# 示例2：带关键字参数的函数
@log_decorator
def greet(name, prefix="Hello"):
    """向指定名称的人打招呼"""
    return f"{prefix}, {name}!"


greet("Alice", prefix="Hi")
# 输出日志：
# 2023-10-01 12:00:01,456 - INFO - 开始调用函数: greet
# 2023-10-01 12:00:01,456 - INFO - 参数: args=('Alice',), kwargs={'prefix': 'Hi'}
# 2023-10-01 12:00:01,456 - INFO - 函数 greet 执行成功，返回值: Hi, Alice!


# 示例3：可能抛出异常的函数
@log_decorator
def divide(a, b):
    """除法运算（可能抛出除零异常）"""
    return a / b


try:
    divide(10, 0)
except ZeroDivisionError:
    pass  # 捕获异常，避免程序终止
# 输出日志：
# 2023-10-01 12:00:02,789 - INFO - 开始调用函数: divide
# 2023-10-01 12:00:02,789 - INFO - 参数: args=(10, 0), kwargs={}
# 2023-10-01 12:00:02,789 - ERROR - 函数 divide 执行失败，异常: division by zero
# Traceback (most recent call last):
#   File "...", line 18, in wrapper
#     result = func(*args, **kwargs)
#   File "...", line 43, in divide
#     return a / b
# ZeroDivisionError: division by zero
