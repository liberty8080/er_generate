from flask import Flask
from flask import request
from process import transfer_table
from eralchemy.main import render_er, get_table_relationship

app = Flask(__name__)


@app.route('/', methods=['POST'])
def hello_world():
    a = request.get_json()
    print(type(transfer_table(a)))
    render_er(transfer_table(a), 'home/jacob/sss.png')
    return


@app.route('/dot', methods=['POST'])
def pr_dot():
    a = request.get_json()
    dot = get_table_relationship(transfer_table(a))
    print(dot)
    return dot


if __name__ == '__main__':
    app.debug = True
    app.run()
