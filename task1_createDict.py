import os

class InitSets:
    def __init__(this):
        clear = lambda: os.system("CLS")
        clear()

class ExecModule:
    def __init__(this):
        this.strLegend = "Введите пожалуйста целое число: "
        this.myDict = {}

    def InputFunc(this):
            while True:
                try:
                    inputStr = float(input(this.strLegend))
                    this.N = int(inputStr)
                except:
                    print("Вы ввели не соответсвующую запись! Попробуйте еще раз")
                else: 
                    if this.N > 0: return
                    else: print("Вы ввели отрицательнон число! Попробуйте еще раз")

    def CreateDict(this):
        for i in range(1, this.N + 1):
            this.myDict[i] = 3 * i + 1
        print(this.myDict)

initClear = InitSets()
work = ExecModule()
work.InputFunc()
work.CreateDict()