# s = input()
# a = ['python','computer','book','program']

n = 0
for k in a:
    n += k.count(s)
print(n)

# s = input()

s = s.upper()
t = s[0]
c = 1
for i in range(1,len(s)):
    if s[i] == t:
        c += 1
    else:
        print(f'({t},{c})',end='')
        t = s[i]
        c = 1
print(f'({t},{c})',end='')

# s = input()

s = s.split()
word_max = max(s,key=len)
print(f"输入句子中最长的单词是{word_max},长度是{len(word_max)}")

# import string
# s = input()


for i in s:
    if i in string.ascii_lowercase:
        if ord(i)+3 > ord('z'):
            print(chr(ord(i)+3-26),end='')
        else:
            print(chr(ord(i)+3),end='')
    else:
        print(i,end='')


# students = [
#     {'name':'张三','age':18,'score':98,'tel':'13888889988','gender':'female'},
#     {'name':'李四','age':28,'score':95,'tel':'13886666666','gender':'male'},
#     {'name':'王五','age':17,'score':47,'tel':'13888889999','gender':'unknown'},
#     {'name':'刘六','age':16,'score':16,'tel':'13886666668','gender':'unknown'},
# ]
# n = int(input())


if n == 1:
    x = 0
    for student in students:
        if student['score'] < 60:
            x += 1
        else:
            continue
    print(f"不及格的学生有{x}个")
elif n == 2:
    bad_student = []
    for student in students:
        if student['score'] < 60:
            bad_student.append(student['name'])
        else:
            continue
    print(bad_student)
elif n == 3:
    child_number = 0
    for student in students:
        if student['age'] < 18:
            child_number += 1
        else:
            continue
    print(f"未成年的学生有{child_number}个")
elif n == 4:
    child_tel = []
    for student in students:
        if student['age'] < 18:
            child_tel.append(student['tel'])
        else:
            continue
    print(child_tel)
elif n == 5:
    student_tel_last_number_8 = []
    for student in students:
        if student['tel'][-1] == '8':
            student_tel_last_number_8.append(student['name'])
        else:
            continue
    print(student_tel_last_number_8)
elif n == 6:
    students = [student for student in students if student['gender'] != 'unknown']
    print(students)

# students = [
#     {'name':'张三','age':18,'score':98,'tel':'13888889988','gender':'female'},
#     {'name':'李四','age':28,'score':95,'tel':'13886666666','gender':'male'},
#     {'name':'王五','age':17,'score':47,'tel':'13888889999','gender':'unknown'},
#     {'name':'刘六','age':16,'score':16,'tel':'13886666668','gender':'unknown'},
# ]
# a = input()

if a == 'score':
    students = sorted(students,key=lambda x:x['score'],reverse=True)
    print(students)
elif a == 'age':
    students = sorted(students,key=lambda x:x['age'],reverse=True)
    print(students)