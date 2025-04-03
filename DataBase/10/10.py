import pymysql as mysql
from prettytable import PrettyTable

def db_show():
    connection = mysql.connect(
        host='localhost',
        user='root',
        password='qwertyuiop0!',
        database='邱宗森实验10'
    )

    try:
        with connection.cursor() as cursor:
            sql = "SELECT 学号, 姓名, 性别, 年龄, 系别 FROM student order by rand() limit 1;"
            cursor.execute(sql)
            result = cursor.fetchall()
            table = PrettyTable()
            table.field_names = ["学号", "姓名", "性别", "年龄", "系别"]
            for row in result:
                table.add_row(list(row))
            print(table)
    finally:
        connection.close()

def db_delete_one():
    connection = mysql.connect(
        host='localhost',
        user='root',
        password='qwertyuiop0!',
        database='邱宗森实验10'
    )
    
    student_id = input("请输入要删除的学生学号: ")
    try:
        with connection.cursor() as cursor:
            sql = f"DELETE FROM student WHERE 学号 = '{student_id}';"
            cursor.execute(sql)
            connection.commit()
            if cursor.rowcount > 0:
                print("删除成功!")
            else:
                print("删除失败!")
    finally:
        connection.close()
        
def db_find_student_by_id():
    connection = mysql.connect(
        host='localhost',
        user='root',
        password='qwertyuiop0!',
        database='邱宗森实验10'
    )
    
    student_id = input("请输入要查找的学生学号: ")
    try:
        with connection.cursor() as cursor:
            sql = f"SELECT 学号, 姓名, 性别, 年龄, 系别 FROM student WHERE 学号 = '{student_id}';"
            cursor.execute(sql)
            result = cursor.fetchall()
            if len(result) == 0:
                print("查无此人!")
                return
            table = PrettyTable()
            table.field_names = ["学号", "姓名", "性别", "年龄", "系别"]
            for row in result:
                table.add_row(list(row))
            print(table)
    finally:
        connection.close()
        
def fetch_all_student():
    connection = mysql.connect(
        host='localhost',
        user='root',
        password='qwertyuiop0!',
        database='邱宗森实验10'
    )
    
    try:
        with connection.cursor() as cursor:
            sql = "SELECT 学号, 姓名, 性别, 年龄, 系别 FROM student;"
            cursor.execute(sql)
            result = cursor.fetchall()
            table = PrettyTable()
            table.field_names = ["学号", "姓名", "性别", "年龄", "系别"]
            for row in result:
                table.add_row(list(row))
            print(table)
    finally:
        connection.close()

def db_insert_student():
    connection = mysql.connect(
        host='localhost',
        user='root',
        password='qwertyuiop0!',
        database='邱宗森实验10'
    )
    
    try:
        with connection.cursor() as cursor:
            student_id = input("请输入学号: ")
            student_name = input("请输入姓名: ")
            student_gender = input("请输入性别: ")
            student_age = input("请输入年龄: ")
            student_major = input("请输入系别: ")
            student_height = input("请输入身高: ")
            sql = f"INSERT INTO student (学号, 姓名, 性别, 年龄, 系别, 身高) VALUES \
                ('{student_id}', '{student_name}', '{student_gender}', {student_age}, '{student_major}', {student_height});"
            cursor.execute(sql)
            connection.commit()
            if cursor.rowcount > 0:
                print("插入成功!")
            else:
                print("插入失败!")
    finally:
        connection.close() 

def main():
    # db_show()
    # db_delete_one()
    db_find_student_by_id()
    # fetch_all_student()
    # db_insert_student()
    
if __name__ == '__main__':
    main()