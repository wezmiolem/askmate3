from flask import Flask, render_template
import data_manager
app = Flask(__name__)


@app.route('/')
def hello_world():
    answers = data_manager.get_answers()
    return render_template('index.html', answers=answers)


if __name__ == '__main__':
    app.run()
