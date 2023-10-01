import random
# Реализация без проверок на 'дурачка'
# Процедуры - Данные представлены в виде переменных и операции над ними разделены на процедуры, что позволяет
#   простить себе жизнь, иначе можно запутаться, а так каждый метод отвечает за конкретное действие
# Программа построена на последовательном выполнении действий, это у нас Императивный стиль
# Структурное программирование - в программе представлены данные и функции,
#   организованные в структурированный код, в данном случае в класс "Game"


class Game:
    print("Правила:\n Нужно выбрать чем будешь играть: буква X или O, ввод на английском\n "
          "Во время твоего хода нужно ввести координаты точки, куда хочешь поставить символ\n "
          "Сначала спросит номер строки потом номер столбца\n "
          "Отсчет координат начитается с 1, игровое поле 3х3\n"
          "Цель игры: три буквы в ряд сделают тебя победителем, вертикально, горизонтально или по дигонали, неважно\n")

    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.player_choice = None

    def print_board(self):
        for row in self.board:
            print('|'.join(row))

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print('Неверный ввод, повторите(X, O).')

    def check_winner(self):
        # Проверка победителя, должно быть 3 в ряд, вертикально, горизонтально, диагонально
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
            if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
                return self.board[0][0]
            if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
                return self.board[0][2]

        # Проверка на ничью
        if all(self.board[i][j] != ' ' for i in range(3) for j in range(3)):
            return 'Draw'
        # продолжение игры
        return None

    def choose_player(self):
        choice = input("Выбери букву, которой будешь играть 'X' или 'O': ")
        while choice not in ['X', 'O']:
            print("Неверный ввод. Введи букву 'X' или 'O'.")
            choice = input("Введи букву 'X' или 'O': ")
        self.player_choice = choice

    def main(self):
        self.choose_player()
        opponent = 'O' if self.player_choice == 'X' else 'X'

        while True:
            if self.current_player == self.player_choice:
                self.print_board()
                row = int(input('Введи номер строки: '))
                row -= 1
                col = int(input('Введи номер столбца: '))
                col -= 1
                self.make_move(row, col)
            else:
                # ход компьютера, заполнение рандомной пустой клетки
                empty_cells = [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']
                if empty_cells:
                    row, col = random.choice(empty_cells)
                    self.make_move(row, col)

            winner = self.check_winner()
            if winner:
                self.print_board()
                if winner == 'Draw':
                    print('Ничья')
                elif winner == self.player_choice:
                    print('Ты победил!')
                else:
                    print('Потрачено!')

                play_again = input('Сыграем снова? (Y/N): ')
                if play_again.lower() == 'y':
                    self.__init__()
                    self.choose_player()
                else:
                    break


# запуск игры

game = Game()
game.main()
