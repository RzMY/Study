import threading
import time
import random

# 配置参数
BUFFER_SIZE = 4
PRODUCER_COUNT = 3
CONSUMER_COUNT = 2
ITEMS_PER_PRODUCER = 5

buffer = [None] * BUFFER_SIZE
in_ptr = 0  # 生产者放入位置
out_ptr = 0  # 消费者取出位置
count = 0  # 当前缓冲区中的项目数

# 实现互斥锁
mutex_flag = 0  # 0表示锁可用，1表示被占用

# 实现信号量(empty和full)
empty_count = BUFFER_SIZE  # 空槽位数量
full_count = 0  # 满槽位数量

# 记录计数
produced_count = 0
consumed_count = 0
production_done = False

# 互斥锁的获取和释放
def acquire_mutex():
    global mutex_flag
    while True:
        if mutex_flag == 0:
            mutex_flag = 1
            break
        time.sleep(0.001)

def release_mutex():
    global mutex_flag
    mutex_flag = 0

# 信号量P操作(wait)
def wait_empty():
    global empty_count
    while True:
        acquire_mutex()
        if empty_count > 0:
            empty_count -= 1
            release_mutex()
            break
        release_mutex()
        time.sleep(0.001)

def wait_full():
    global full_count
    while True:
        acquire_mutex()
        if full_count > 0:
            full_count -= 1
            release_mutex()
            break
        release_mutex()
        time.sleep(0.001)

# 信号量V操作(signal)
def signal_empty():
    global empty_count
    acquire_mutex()
    empty_count += 1
    release_mutex()

def signal_full():
    global full_count
    acquire_mutex()
    full_count += 1
    release_mutex()

# 生产者函数
def producer(producer_id):
    global in_ptr, count, produced_count, production_done

    for i in range(ITEMS_PER_PRODUCER):
        # 生成产品
        item = producer_id * 100 + i
        
        wait_empty()
        acquire_mutex()
        
        # 放入产品
        buffer[in_ptr] = item
        print(f"生产者 {producer_id} 生产产品: {item} 放入位置 {in_ptr}")
        in_ptr = (in_ptr + 1) % BUFFER_SIZE
        count += 1
        # 更新已生产计数
        produced_count += 1
        
        release_mutex()
        signal_full()
        
        time.sleep(random.uniform(0.1, 0.3))
    
    print(f"生产者 {producer_id} 完成生产")
    
    acquire_mutex()
    if produced_count >= PRODUCER_COUNT * ITEMS_PER_PRODUCER:
        production_done = True
    release_mutex()

# 消费者函数
def consumer(consumer_id):
    global out_ptr, count, consumed_count
    
    while True:
        # 检查是否已完成所有消费
        acquire_mutex()
        if production_done and consumed_count >= produced_count:
            release_mutex()
            break
        
        if consumed_count >= PRODUCER_COUNT * ITEMS_PER_PRODUCER:
            release_mutex()
            break
        release_mutex()
        

        wait_full()
        acquire_mutex()
        
        # 取出产品
        item = buffer[out_ptr]
        print(f"消费者 {consumer_id} 消费产品: {item} 从位置 {out_ptr}")
        buffer[out_ptr] = None
        out_ptr = (out_ptr + 1) % BUFFER_SIZE
        count -= 1
        # 更新已消费计数
        consumed_count += 1
        
        release_mutex()
        signal_empty()
        
        # 随机休眠
        time.sleep(random.uniform(0.2, 0.5))
    
    print(f"消费者 {consumer_id} 完成消费")

def display():
    print("缓冲区状态:")
    for i in range(BUFFER_SIZE):
        item = buffer[i] if buffer[i] is not None else "空"
        print(f"位置 {i}: {item}")
    print(f"当前缓冲区项目数: {count}, 空槽位: {empty_count}, 满槽位: {full_count}")
    print("-" * 40)

def main():
    random.seed()
    
    producer_threads = []
    consumer_threads = []
    
    display()

    # 创建生产者线程
    for i in range(PRODUCER_COUNT):
        thread = threading.Thread(target=producer, args=(i+1,))
        producer_threads.append(thread)
        thread.start()
    
    # 创建消费者线程
    for i in range(CONSUMER_COUNT):
        thread = threading.Thread(target=consumer, args=(i+1,))
        consumer_threads.append(thread)
        thread.start()
    
    display()  # 显示初始状态

    # 等待所有线程结束
    for thread in producer_threads:
        thread.join()
    for thread in consumer_threads:
        thread.join()
    
    print("所有生产者和消费者已完成工作")
    print(f"总共生产了 {produced_count} 个产品，消费了 {consumed_count} 个产品")
    display()

if __name__ == "__main__":
    main()