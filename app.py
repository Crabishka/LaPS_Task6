from flask import Flask, render_template, request, redirect, url_for
import json
from types import SimpleNamespace

from services.jsonParser import get_sudoku_array
from services.sudokuService import solve_sudoku

app = Flask(__name__)


@app.route('/')
def root():
    d = {}
    return render_template('index.html', sudoku=d)


@app.route('/solve', methods=['POST'])
def solve():
    data = request.form
    sudoku_table = get_sudoku_array(data)
    solve_sudoku(sudoku_table)
    sudoku_render_table = {}
    for i in range(0, 9):
        for j in range(0, 9):
            key = str(i) + '-' + str(j)
            sudoku_render_table[key] = sudoku_table[i][j]
    return render_template('index.html', sudoku=sudoku_render_table)


if __name__ == '__main__':
    app.run()
