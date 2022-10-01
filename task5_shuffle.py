import os
import datetime

class InitSets:
    def __init__(this):
        clear = lambda: os.system("CLS")
        clear()

class ExecModule:
    def __init__(this):
        this.myList = ["Первый", "Второй", "Третий", "Четвертый", "Пятый", "Шестой", "Седьмой", "Восьмой"]
        this.newOrder = []

    def CreateShuffle(this):
        for i in range(len(this.myList)):
            divider = len(this.myList) - i
            this.newOrder.append(int(datetime.datetime.now().strftime("%f")) % divider)

        # print(this.newOrder)
        

        for i in range(len(this.newOrder)):
            check = this.newOrder[i]
            for j in range(i + 1, len(this.newOrder)):
                if this.newOrder[j] == check:
                    # print("новая цифра для", this.newOrder[j])
                    this.newOrder[i] = this.FindNewDigit()
                    break
        
        lastCheck = int(datetime.datetime.now().strftime("%f")) % len(this.myList)
        cach = this.newOrder[len(this.myList) - 1]
        this.newOrder[len(this.myList) - 1] = this.newOrder[lastCheck]
        this.newOrder[lastCheck] = cach

        # print(this.newOrder)
            
    def FindNewDigit(this):
        for i in range(len(this.newOrder)):
            if i in this.newOrder: continue
            else:
                return i

        return 0

    def MakeShuffle(this):
        this.shuffList = []

        for i in range(len(this.newOrder)):
            x = this.newOrder[i]
            this.shuffList.append(this.myList[x])
            
        print("Лист до шаффла")
        print(this.myList)

        print("\nЛист после шаффла")
        print(this.shuffList)



initClear = InitSets()
work = ExecModule()
work.CreateShuffle()
work.MakeShuffle()