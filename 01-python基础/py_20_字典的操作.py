person = {
    'name': '小明',
    'age': 20,
    'gender': 'male',
    'height': 170
}

# 获取字典长度
length = len(person)

# 合并字典，并对重复属性更新
person2 = {
    'weight': 120,
    'name': '张三'
}
person.update(person2)

# 清空字典
person.clear()

print(length, person)