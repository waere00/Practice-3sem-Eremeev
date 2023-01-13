from tkinter import *

board = [['', '', ''], ['', '', ''], ['', '', '']]
count = 0
player = 'X'


def check_win(board):
    for i in range(3):
        if (''.join(board[i]) == 'XXX') or (''.join(board[i]) == 'OOO'):
            return True
    for i in range(3):
        column = ''
        for j in range(3):
            column = column + board[j][i]
        if column == 'XXX' or column == 'OOO':
            return True
    if board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[2][0] == board[1][1] == board[0][2]:
        return True


def restart():
    global board, count, player
    board = [['', '', ''], ['', '', ''], ['', '', '']]
    count = 0
    but1['text'] = ''
    but2['text'] = ''
    but3['text'] = ''
    but4['text'] = ''
    but5['text'] = ''
    but6['text'] = ''
    but7['text'] = ''
    but8['text'] = ''
    but9['text'] = ''
    player = 'X'
    lab['text'] = 'Текущий игрок: ' + player


def tap(row, column, button):
    global count, board, player
    lab['text'] = 'Текущий игрок: ' + player
    if board[row][column] == '':
        button['text'] = player
        board[row][column] = player
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
        lab['text'] = 'Текущий игрок: ' + player
        count = count + 1
        if count >= 5:
            if check_win(board):
                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'
                lab['text'] = 'Победа игрока ' + player + '!'
                root.after(1000, restart)
        if count == 9:
            lab['text'] = "Ничья"
            root.after(1000, restart)
    else:
        lab['text'] = 'Select another one!'


root = Tk()

but1 = Button(text="", height=5, width=10, font=('arial', 12, 'bold'), fg='black', command=lambda: tap(0, 0, but1))
but2 = Button(text="", height=5, width=10, font=('arial', 12, 'bold'), fg='black', command=lambda: tap(0, 1, but2))
but3 = Button(text="", height=5, width=10, font=('arial', 12, 'bold'), fg='black', command=lambda: tap(0, 2, but3))
but4 = Button(text="", height=5, width=10, font=('arial', 12, 'bold'), fg='black', command=lambda: tap(1, 0, but4))
but5 = Button(text="", height=5, width=10, font=('arial', 12, 'bold'), fg='black', command=lambda: tap(1, 1, but5))
but6 = Button(text="", height=5, width=10, font=('arial', 12, 'bold'), fg='black', command=lambda: tap(1, 2, but6))
but7 = Button(text="", height=5, width=10, font=('arial', 12, 'bold'), fg='black', command=lambda: tap(2, 0, but7))
but8 = Button(text="", height=5, width=10, font=('arial', 12, 'bold'), fg='black', command=lambda: tap(2, 1, but8))
but9 = Button(text="", height=5, width=10, font=('arial', 12, 'bold'), fg='black', command=lambda: tap(2, 2, but9))
lab = Label(width=30, bg='white', fg='black', text='Кликните для начала')

but1.grid(row=0, column=0)
but2.grid(row=0, column=1)
but3.grid(row=0, column=2)
but4.grid(row=1, column=0)
but5.grid(row=1, column=1)
but6.grid(row=1, column=2)
but7.grid(row=2, column=0)
but8.grid(row=2, column=1)
but9.grid(row=2, column=2)
lab.grid(row=3, column=0, columnspan=3, rowspan=3)
root.mainloop()
