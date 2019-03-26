from flask import Flask, request, redirect, url_for
from sudoku_solver import solveSudoku

app = Flask(__name__)

@app.route('/')
def main():
    html = '<form action="solving" method="POST">'
    for lis in ['abc','def','ghi']:
        for i in range(3):
            for c in lis:
                for j in [3*i+1,3*i+2,3*i+3]:
                    html+='<select name="'+c+str(j)+'">'
                    html+='<option value="0"> </option>'
                    html+='<option value="1">1</option>'
                    html+='<option value="2">2</option>'
                    html+='<option value="3">3</option>'
                    html+='<option value="4">4</option>'
                    html+='<option value="5">5</option>'
                    html+='<option value="6">6</option>'
                    html+='<option value="7">7</option>'
                    html+='<option value="8">8</option>'
                    html+='<option value="9">9</option>'
                    html+='</select>'
                html+=' '
            html+='<br>'
        html+='<br>'
    html+= '<input type="submit" value="Submit">'
    html+= '</form>'
    return html

@app.route('/solving', methods=['POST'])
def process():
    toSolve = ''
    for c in 'abcdefghi':
        for i in range(1,10):
            toSolve+=str(request.form.get(c+str(i)))
    # return toSolve
    return redirect(url_for('solve', sudoku=toSolve))

@app.route('/test')
def formTest():
    return 'Nothing being tested!'

@app.route('/<string:sudoku>')
def solve(sudoku):
    solved = solveSudoku(sudoku)
    response = ''
    if solved == 'Solver Timed out':
        response+= solved
    else:
        response+= '<form action="/dummy">'
        for i in [0,27,54]:
            for j in [0,3,6]:
                for k in [0,9,18]:
                    for l in range(3):
                        response+='<input type="text" value="'+solved[i+j+k+l]+'" size="1" readonly>'
                    response+=' '
                response+='<br>'
            response+='<br>'
        response+='</form>'
    response+='<form action="/"><button name="backbtn" type="submit">Back</button></form>'
    # if solved == 'Solver Timed out':
    #     response+= solved
    # else:
    #     solution = solved.split('\n')
    #     response+= '<p>'+solution[0]+'</p>'+'\n'
    #     response+= '<p>'+solution[1]+'</p>'+'\n'
    #     response+= '<p>'+solution[2]+'</p>'+'\n'
    #     response+= '<p>'+solution[3]+'</p>'+'\n'
    #     response+= '<p>'+solution[4]+'</p>'+'\n'
    #     response+= '<p>'+solution[5]+'</p>'+'\n'
    #     response+= '<p>'+solution[6]+'</p>'+'\n'
    #     response+= '<p>'+solution[7]+'</p>'+'\n'
    #     response+= '<p>'+solution[8]+'</p>'+'\n'
    #     response+= '<p>'+solution[9]+'</p>'+'\n'
    #     response+= '<p>'+solution[10]+'</p>'
    # response+='\n'
    # response+='<form action="/"><button name="backbtn" type="submit">Back</button></form>'
    # return response
    return response
