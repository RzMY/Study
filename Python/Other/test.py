total_animals = int(input("请输入总数量："))
total_legs = int(input("请输入总腿数："))

chicken_count = (total_legs - total_animals * 4) / 2
rabbit_count = total_animals - chicken_count

print("鸡的数量为：", chicken_count)
print("兔子的数量为：", rabbit_count)