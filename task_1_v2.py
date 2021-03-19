import sys

def task(array):
    return array.find("0") # Здесь можно было бы использовать метод .index(str), но тогда придется вводить обработку исключений 

if __name__ == "__main__":

    # при запуске программы считываем, переданные аргументы, если массив единиц и нулей не введен,
    # то приглашаем пользователя на ввод
    if len(sys.argv) < 2:
        array = input("Please enter ones and zeros: ")
        if array:
            print(task(array))
        else:
            print("Second argument is not found. Calculation failed.")

    # В этом блоке считываются аргументы и если их 2, то выполняется поиск "0"
    # 
    if len(sys.argv) == 2:
        result = task(sys.argv[1])
        if result == -1:
            result = "Zero is not found" # если "0" не найден в переданном массиве(на самом деле это строка) данных
            
        print(result)

    # Этот блок выполняется, если передано больше аргументов чем нужно
    if len(sys.argv) > 2:
        print("Sorry, calculations failed. Too many arguments. Only one argument is expected.")