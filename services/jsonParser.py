def get_sudoku_array(d):
    sudoku = [[0 for i in range(0, 9)] for j in range(0, 9)]
    for i in range(0, 9):
        for j in range(0, 9):
            key = str(i) + '-' + str(j)
            if d[key] == '':
                sudoku[i][j] = 0
            else:
                sudoku[i][j] = int(d[key])
    return sudoku
