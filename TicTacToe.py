# -*- coding: utf-8 -*-
class TicTacToe:
    def __init__ (self, tic_player, toc_player):
        self.tic_player = tic_player
        self.toc_player = toc_player
        self.field = list(range(1, 10))
        self.string_field = ''
    
    def print_field(self):
        print("-------------")
        for i in range(3):
            print("|", self.field[0 + i * 3], "|", self.field[1 + i * 3], "|", self.field[2 + i * 3], '|')
        print("-------------")

    def checkWin(self):
        win_cond = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for cond in win_cond:
            if self.field[cond[0]] == self.field[cond[1]] == self.field[cond[2]]:
                return True
        return False

    def take_input(self, current_tocken):
        continue_flag = True
        if current_tocken == 'X':
            current_name = self.tic_player
        else:
            current_name = self.toc_player
        while continue_flag:
            player_answer = input("{name}, введите позицию, куда поставить {tocken}: ".format(name=current_name, tocken=current_tocken))
            try:
                player_answer = int(player_answer)
            except:
                print("Некорректный ввод, введите число")
                continue
            write_answer = self.write_field(player_answer, current_tocken)
            if write_answer == 0:
                continue_flag = False
            elif write_answer == 2:
                    print("Эта клетка уже занята")
            else:
                print("Нужно ввести число от 1 до 9!")

    def write_field (self, player_answer, current_tocken):
        if player_answer >= 1 and player_answer <= 9:
            if(str(self.field[player_answer - 1]) not in "X0"):
                self.field[player_answer - 1] = current_tocken
                self.string_to_field()
                return 0
            else: 
                return 2
        else:
            return 1
    
    def string_to_field (self):
        for elem in self.string_field:
            self.string_field += str(elem)

    def run(self):
        turn = 0
        win = False
        self.print_field()
        while not win:
            if turn % 2 == 0:
                self.take_input("X")
            else:
                self.take_input("0")
            turn += 1
            if (turn > 4):
                if (self.checkWin()):
                    if(turn % 2 == 0):
                        self.print_field()
                        print("{name} победил".format(name=self.toc_player))
                    else:
                        self.print_field()
                        print("{name} победил".format(name=self.tic_player))
                    win = True
                    break
                if turn == 9:
                    print("Ничья")
                    break
            self.print_field()

if __name__ == "__main__":
    while True:
        player_one = input("Игрок за крестики, введите свое имя: ")
        if (not player_one):
            print("У вас нет имени!")
            continue
        break
    while True:
        player_two = input("Игрок за нолики, введите свое имя: ")
        if (not player_two):
            print("У вас нет имени!")
            continue
        break

    game = TicTacToe(player_one, player_two)
    game.run()