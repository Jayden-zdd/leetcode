# 处理复杂数据结构
import threading
import copy


def modify_list(shared_list):
    for i in range(len(shared_list)):
        shared_list[i] += 10


original_list = [1, 2, 3]
threads = []
for _ in range(5):
    thread = threading.Thread(target=modify_list, args=(copy.deepcopy(original_list),))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(original_list)


# 配置对象定制
import copy
import threading

global_config = {"server": "localhost", "port": 8080, "timeout": 60}


def thread_task(config):
    config["port"] = 8081
    # 线程内其他操作，使用修改后的配置


threads = []
for _ in range(3):
    copied_config = copy.deepcopy(global_config)
    thread = threading.Thread(target=thread_task, args=(copied_config,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print(global_config)
