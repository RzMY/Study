import pymysql

db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'qwertyuiop0!',
    db = 'crawler',
    autocommit = True
)

cursor = db.cursor()

# 获取所有的表名
cursor.execute("SHOW TABLES")
tables = cursor.fetchall()

# 为每个表添加自增主键列
for table in tables:
    cursor.execute(f"ALTER TABLE {table[0]} ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

cursor.close()
db.close()