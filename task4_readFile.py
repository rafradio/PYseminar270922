import os

class InitSets:
    def __init__(this):
        clear = lambda: os.system("CLS")
        clear()

class ExecModule:
    def __init__(this):
        this.strLegend = "Введите пожалуйста целое число: "
        this.myArr = []

    def InputFunc(this):
            while True:
                try:
                    inputStr = float(input(this.strLegend))
                    this.N = int(inputStr)
                    return
                except:
                    print("Вы ввели не соответсвующую запись! Попробуйте еще раз")

    def FindSum(this):
        if this.N < 0: this.N = abs(this.N)
        for i in range(-this.N, this.N + 1):
            this.myArr.append(i)

        f = open("position.txt")
        this.positions = f.read()
        #x = this.positions.rsplit(" ")
        #x = "".join(this.positions.split())
        this.positions = this.positions.split()
        mult = 1
        for i in this.positions:
            j = float(i)
            j = int(j)
            mult = mult * this.myArr[j]
        print(this.myArr)
        print(mult)



initClear = InitSets()
work = ExecModule()
work.InputFunc()
work.FindSum()