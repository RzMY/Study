from collections import deque, defaultdict

# 中缀表达式
infix_expression = ''  
# 后缀表达式
postfix_expression = deque()  
# 存放所有字母变量
variables = ''  
# 映射，将字母变量与0或1一一对应
variable_mapping = defaultdict(int)  
# 存放主析取范式对应字母变量的01情况，也就是表达式真值为T
true_cases = []  
# 存放主合取范式对应字母变量的01情况，也就是表达式真值是F
false_cases = []  

# 计算操作符的优先级，用于中缀转后缀
def incoming_priority(a):
    return {'#': 0, '(': 12, '&': 2, '|': 1, ')': 1}.get(a, 0)

# 计算栈内操作符的优先级，用于中缀转后缀
def in_stack_priority(a):
    return {'#': 0, '(': 1, '&': 2, '|': 1, ')': 12}.get(a, 0)

# 将中缀表达式转换为后缀表达式
def convert_to_postfix():
    global infix_expression, postfix_expression, variables
    stack = deque(['#'])
    for char in infix_expression:
        if char.isalpha():  # 如果是字母，直接添加到后缀表达式中
            postfix_expression.append(char)
            if char not in variables:  # 如果是新的变量，添加到变量列表中
                variables += char
        elif char == ')':  # 如果是右括号，弹出栈中的操作符直到遇到左括号
            while stack and (y := stack.pop()) != '(':
                postfix_expression.append(y)
        else:  # 如果是操作符，弹出栈中优先级高于或等于它的操作符，然后将它压入栈中
            while stack and incoming_priority(char) <= in_stack_priority(y := stack.pop()):
                postfix_expression.append(y)
            stack.append(y)
            stack.append(char)
    while stack:  # 弹出栈中剩余的操作符
        y = stack.pop()
        if y != '#':
            postfix_expression.append(y)

# 计算后缀表达式的值
def calculate():
    stack = deque()
    for char in postfix_expression:
        if char.isalpha():  # 如果是字母，将其对应的值压入栈中
            stack.append(variable_mapping[char])
        else:  # 如果是操作符，弹出栈顶的两个元素进行运算，然后将结果压入栈中
            if char == '&':
                stack.append(stack.pop() and stack.pop())
            elif char == '|':
                stack.append(stack.pop() or stack.pop())
    return stack.pop()  # 返回栈顶元素，即表达式的值

# 深度优先搜索所有可能的变量值组合，并计算表达式的真值
def depth_first_search(cur):
    global variables, variable_mapping, true_cases, false_cases
    if cur == len(variables):  # 如果所有变量都已赋值，计算表达式的值
        result = calculate()
        if result:  # 如果表达式的值为真，添加到真值情况列表中
            true_cases.append([variable_mapping[char] for char in variables])
        else:  # 如果表达式的值为假，添加到假值情况列表中
            false_cases.append([variable_mapping[char] for char in variables])
        return
    variable_mapping[variables[cur]] = 1  # 尝试将当前变量赋值为1
    depth_first_search(cur + 1)
    variable_mapping[variables[cur]] = 0  # 尝试将当前变量赋值为0
    depth_first_search(cur + 1)

# 打印主析取范式
def print_disjunctive_normal_form():
    global variables, true_cases
    for i, case in enumerate(true_cases):
        if i != 0:
            print("∨", end="")
        print("(", end="")
        print("∧".join(f"{variables[j]}" if case[j] == 1 else f"￢{variables[j]}" for j in range(len(variables))), end="")
        print(")", end="")
    print()

# 打印主合取范式
def print_conjunctive_normal_form():
    global variables, false_cases
    for i, case in enumerate(false_cases):
        if i != 0:
            print("∧", end="")
        print("(", end="")
        print("∨".join(f"{variables[j]}" if case[j] == 0 else f"￢{variables[j]}" for j in range(len(variables))), end="")
        print(")", end="")
    print()

# 打印真值表
def print_truth_table():
    global variables
    print(' '.join(variables), "表达式真值")
    for i in range(2**len(variables)):
        values = [bool(int(x)) for x in format(i, f'0{len(variables)}b')]
        value_dict = {variables[j]: values[j] for j in range(len(variables))}
        for value in values:
            print('1' if value else '0', end=' ')
        print('1' if eval(infix_expression, value_dict) else '0')

# 主函数
def main():
    global infix_expression, postfix_expression, variables, variable_mapping, true_cases, false_cases
    infix_expression = input("请输入表达式：\n")
    convert_to_postfix()  # 将中缀表达式转换为后缀表达式
    depth_first_search(0)  # 深度优先搜索所有可能的变量值组合，并计算表达式的真值
    print("真值表为：")
    print_truth_table()  # 打印真值表
    print("主析取范式为：")
    print_disjunctive_normal_form()  # 打印主析取范式
    print("主合取范式为：")
    print_conjunctive_normal_form()  # 打印主合取范式

if __name__ == "__main__":
    main()