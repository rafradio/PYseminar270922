import os

class InitSets:
    def __init__(this):
        clear = lambda: os.system("CLS")
        clear()

class ExecModule:
    def __init__(this):
        this.strLegend = "Введите пожалуйста целое число: "
        this.mapArray = {}
        this.array = []
        this.counter = 0
        this.InputFunc()
        this.FindArray()

    def InputFunc(this):
            while True:
                try:
                    inputStr = float(input(this.strLegend))
                    this.N = int(inputStr)
                    return
                except:
                    print("Вы ввели не соответсвующую запись! Попробуйте еще раз")

    def FindArray(this):
        if this.N < 0:
            for i in range(this.N, 0):
                this.array.append(this.ExecArray(i, -1, 1))
            this.array += [0, 1]

        else:
            for i in range(1, this.N + 1):
                this.array.append(this.ExecArray(i, 1, -1))
                
        print(this.array)
        print(this.counter)

    def ExecArray(this, a, x, step):
        this.counter += 1

        if a in this.mapArray.keys():
            return this.mapArray[a]
        
        if a == x:
            this.mapArray[a] = x 
            return x
        
        res = a * this.ExecArray(a + step, x, step)
        this.mapArray[a] = res
        return res


initClear = InitSets()
work = ExecModule()