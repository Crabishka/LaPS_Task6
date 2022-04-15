from flask import Flask, render_template, request, redirect, url_for
import json
from types import SimpleNamespace

from services.jsonParser import get_sudoku_array
from services.sudokuService import solve_sudoku

app = Flask(__name__)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/solve', methods=['POST'])
def solve():
    data = request.form
    sudoku_table = get_sudoku_array(data)
    solve_sudoku(sudoku_table)
    for i in range(0, 9):
        for j in range(0, 9):
            key = str(i) + '-' + str(j)
            render_template('index.html', key=sudoku_table[i][j])
    print(sudoku_table)
    return render_template('index.html')
    # name = data.get('search')
    # password = data.get('password')
    #
    # x = json.loads(request.data, object_hook=lambda d: SimpleNamespace(**d))
    # print(x.name, x.password)
    #
    # return {
    #            "username": name,
    #            "hash": hash(password),
    #            "message": 'Success'
    #        }, 200


if __name__ == '__main__':
    app.run()
