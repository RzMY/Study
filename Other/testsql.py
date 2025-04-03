import subprocess
import time

while True:
    try:
        result = subprocess.run(
            "mysql -h 10.2.132.34 -u root mysql --password=blah",
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        print(result.stdout)
        break  # 成功连接后退出循环
    except subprocess.CalledProcessError as e:
        print(f"Connection failed: {e.stderr}")
        time.sleep(5)  # 等待5秒后重试