import os

class InitSets:
    def __init__(this):
        clear = lambda: os.system("CLS")
        clear()

class ExecModule:
    def __init__(this):
        this.strLegend = "Введите пожалуйста целое число: "
        this.myList = []

    def InputFunc(this):
            while True:
                try:
                    inputStr = float(input(this.strLegend))
                    this.N = int(inputStr)
                except:
                    print("Вы ввели не соответсвующую запись! Попробуйте еще раз")
                else: 
                    if this.N > 0: return
                    else: print("Вы ввели отрицательное число или 0! Попробуйте еще раз")

    def CreateList(this):
        sum = 0
        for i in range(1, this.N + 1):
            res = (1 + (1 / i)) ** i
            this.myList.append(round(res, 2))
            sum = sum + round(res, 2)
        print(this.myList)
        print(f"Сумма списка равна {sum}")

initClear = InitSets()
work = ExecModule()
work.InputFunc()
work.CreateList()