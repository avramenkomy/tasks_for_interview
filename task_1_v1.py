def task(array):
    return array.index("0")

def task_2(array):
    return array.find("0")

print("Первый способ методом .index")
print(task("111111111111111111111111100000000")) # 25

print("Второй способ методом .find")
print(task_2("111111111111111111111111100000000")) # 25
