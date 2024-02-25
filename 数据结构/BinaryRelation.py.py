import numpy as np
import re

# 自反闭包函数
def reflexive_closure(matrix):
    n = len(matrix)  # 获取矩阵的大小
    reflexive_matrix = matrix.copy()  # 复制原矩阵
    np.fill_diagonal(reflexive_matrix, 1)  # 将对角线元素设置为1
    relations = [(i, j) for i in range(n) for j in range(n) if reflexive_matrix[i][j] == 1]  # 获取所有关系对
    return reflexive_matrix, relations  # 返回自反闭包矩阵和关系对

# 对称闭包函数
def symmetric_closure(matrix):
    n = len(matrix)  # 获取矩阵的大小
    symmetric_matrix = matrix.copy()  # 复制原矩阵
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 1:  # 如果元素为1
                symmetric_matrix[j][i] = 1  # 将对应的对称元素设置为1
    relations = [(i, j) for i in range(n) for j in range(n) if symmetric_matrix[i][j] == 1]  # 获取所有关系对
    return symmetric_matrix, relations  # 返回对称闭包矩阵和关系对

# 传递闭包函数
def transitive_closure(matrix):
    n = len(matr  ix)  # 获取矩阵的大小
    transitive_matrix = matrix.copy()  # 复制原矩阵
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # 如果元素[i][j]为0，并且元素[i][k]和元素[k][j]都为1，则将元素[i][j]设置为1
                transitive_matrix[i][j] = transitive_matrix[i][j] or (transitive_matrix[i][k] and transitive_matrix[k][j])
    relations = [(i, j) for i in range(n) for j in range(n) if transitive_matrix[i][j] == 1]  # 获取所有关系对
    return transitive_matrix, relations  # 返回传递闭包矩阵和关系对

# 打印矩阵和关系对的函数
def print_matrix_and_relations(name, matrix, relations, elements):
    print(f"\n{name}")  # 打印矩阵的名称
    print(' ', ' '.join(elements))  # 打印元素列表
    for i, row in enumerate(matrix):  # 遍历矩阵的每一行
        print(elements[i], ' '.join(map(str, row)))  # 打印行元素和行数据
    print(' '.join(f"<{elements[i]},{elements[j]}>" for i, j in relations))  # 打印关系对

# 主函数
def main():
    s = input("请输入关系，格式为 <x,y>,<a,b>,<m,n>：\n")  # 获取用户输入的关系对
    relations = [tuple(re.findall(r'\w+', relation)) for relation in re.findall(r'<\w+,\w+>', s)]  # 解析关系对
    elements = sorted(set(x for relation in relations for x in relation))  # 获取所有的元素并排序
    element_to_index = {element: index for index, element in enumerate(elements)}  # 创建元素到索引的映射
    n = len(elements)  # 获取元素的数量
    matrix = np.zeros((n, n), dtype=int)  # 创建一个全0的矩阵
    for x, y in relations:  # 遍历所有的关系对
        matrix[element_to_index[x]][element_to_index[y]] = 1  # 将对应的矩阵元素设置为1

    indexed_relations = [(element_to_index[x], element_to_index[y]) for x, y in relations]  # 获取索引化的关系对
    print_matrix_and_relations("原关系矩阵", matrix, indexed_relations, elements)  # 打印原关系矩阵和关系对

    reflexive_matrix, reflexive_relations = reflexive_closure(matrix)  # 计算自反闭包
    print_matrix_and_relations("自反闭包", reflexive_matrix, reflexive_relations, elements)  # 打印自反闭包矩阵和关系对

    symmetric_matrix, symmetric_relations = symmetric_closure(matrix)  # 计算对称闭包
    print_matrix_and_relations("对称闭包", symmetric_matrix, symmetric_relations, elements)  # 打印对称闭包矩阵和关系对

    transitive_matrix, transitive_relations = transitive_closure(matrix)  # 计算传递闭包
    print_matrix_and_relations("传递闭包", transitive_matrix, transitive_relations, elements)  # 打印传递闭包矩阵和关系对

if __name__ == "__main__":
    main()