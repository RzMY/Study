# matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]

# # 对称
# for i in range(len(matrix)):
#     for j in range(len(matrix)//2):
#         matrix[i][j],matrix[i][-j-1] = matrix[i][-j-1],matrix[i][j]
# # 对角线翻转
# x = len(matrix)//2 + 1
# for i in range(len(matrix)//2 + 1):
#     for j in range(x):
#         matrix[i][j],matrix[len(matrix)-1-j][len(matrix)-1-i] = matrix[len(matrix)-1-j][len(matrix)-1-i],matrix[i][j]
#     x -= 1

# print(matrix)

matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

# 对称
for i in range(len(matrix)):
    for j in range(len(matrix)//2):
        matrix[i][j],matrix[i][-j-1] = matrix[i][-j-1],matrix[i][j]
# 对角线翻转
x = len(matrix) - 1
for i in range(len(matrix)-1):
    for j in range(x):
        matrix[i][j],matrix[len(matrix)-1-j][len(matrix)-1-i] = matrix[len(matrix)-1-j][len(matrix)-1-i],matrix[i][j]
    x -= 1

print(matrix)