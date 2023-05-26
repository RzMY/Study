#username是形参，形参是函数完成其工作所需的一项信息，放在函数定义的括号内
#jack是实参,实参是调用函数时传递给函数的信息，放在圆括号内

def greet_user(username):
    """Display a simple greeting."""
    print(f"Hello,{username.title()}!")
    
greet_user('jack')