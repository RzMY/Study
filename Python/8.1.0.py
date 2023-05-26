def greet_user():
    """Display a simple greeting."""#文档字符串，描述了函数是做什么的，被称为文档字符串，用三引号括起来
    #"#"后面的内容不是文档字符串的一部分，只是注释
    print("Hello!")
    
greet_user()
print(greet_user.__doc__)
help(greet_user)