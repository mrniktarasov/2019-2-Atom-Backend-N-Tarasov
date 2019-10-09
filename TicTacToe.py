# -*- coding: utf-8 -*-
class TicTacToe:
    def introduction(self):
        self.ticPlayer = input("Игрок за крестики, введите свое имя: ")
        self.tocPlayer = input("Игрок за нолики, введите свое имя: ")
        self.field = list(range(1, 10))
    
    def printField(self):
        print("-------------")
        for i in range(3):
            print("|", self.field[0 + i * 3], "|", self.field[1 + i * 3], "|", self.field[2 + i * 3])
        print("-------------")

    def checkWin(self):
        winCond = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for cond in winCond:
            if self.field[cond[0]] == self.field[cond[1]] == self.field[cond[2]]:
                return self.field[cond[0]]
        return False

    def takeInput(self, currentTocken):
        continueFlag = True
        while(continueFlag):
            playerAnswer = input("{name}, введите позицию, куда поставить {tocken}: ".format(name=self.ticPlayer, tocken=currentTocken))
            try:
                playerAnswer = int(playerAnswer)
            except:
                print("Некорректный ввод, введите число")
                continue
            if (playerAnswer >= 1 and playerAnswer <= 9):
                if(str(self.field[playerAnswer - 1]) not in "X0"):
                    self.field[playerAnswer - 1] = currentTocken
                    continueFlag = False
                else:
                    print("Эта клетка уже занята")
            else:
                print("Нужно ввести число от 1 до 9!")
    
    def run(self):
        turn = 0
        win = False
        self.introduction()
        self.printField()
        while not win:
            if (turn % 2 == 0):
                self.takeInput("X")
            else:
                self.takeInput("0")
            turn += 1
            if (turn > 4):
                checkedWin = self.checkWin()
                if (checkedWin):
                    if(checkedWin == "X"):
                        self.printField()
                        print("{name} победил".format(name=self.ticPlayer))
                    else:
                        self.printField()
                        print("{name} победил".format(name=self.tocPlayer))
                    win = True
                    break
                if (turn == 9):
                    print("Ничья")
                    break
            self.printField()