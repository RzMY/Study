from math import prod
import prettytable
import time

lock = [False, False, False, False]

buffer = [0, 0, 0, 0]

def display():
    table = prettytable.PrettyTable()
    table.field_names = ["缓冲区", "0", "1", "2", "3"]
    table.add_row(["资源数量"] + buffer)
    print(table)

def Producer():
    global lock, buffer
    while True:
        for i in range(4):
            if not buffer[i]:
                if not lock[i]:
                    lock[i] = True
                    buffer[i] += 1
                    print(f"生产者生产了资源, 放入了缓冲区{i}")
                    lock[i] = False
                    break
                if i == 3:
                    print("找不到空缓冲区，等待中...")
                    time.sleep(1)

def Consumer():
    global lock, buffer
    while True:
        for i in range(4):
            if buffer[i]:
                if not lock[i]:
                    lock[i] = True
                    buffer[i] -= 1
                    print(f"消费者消费了资源, 从缓冲区{i}取出")
                    lock[i] = False
                    break
                if i == 3:
                    print("找不到资源，等待中...")
                    time.sleep(1)

def main():
    import threading

    producer_count = 3
    consumer_count = 2

    producer_threads = []
    consumer_threads = []

    display()

    for _ in range(producer_count):
        t = threading.Thread(target=Producer)
        t.daemon = True
        t.start()
        producer_threads.append(t)

    for _ in range(consumer_count):
        t = threading.Thread(target=Consumer)
        t.daemon = True
        t.start()
        consumer_threads.append(t)

if __name__ == "__main__":
    main()