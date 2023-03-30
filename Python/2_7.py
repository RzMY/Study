#pytohn会将空格视为字符，因此需要使用strip()方法去除空格，lstrip()方法去除左边空格，rstrip()方法去除右边空格
name0 = " RateMY "
information_1 = f"name:\t{name0}"
print (information_1)
name1 = name0.lstrip()
information_2 = f"name:\t{name1}"
print (information_2)
name2 = name0.rstrip()
information_3 = f"name:\t{name2}"
print (information_3)
name3 = name0.strip()
information_4 = f"name:\t{name3}"
print(information_4)