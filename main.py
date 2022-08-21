
from markupsafe import escape
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def show_main():
    return render_template('index.html')


@app.route('/user/<username>')
def show_user_profile(username):

    return "Hello World {}!".format(escape(username))


@app.route('/results/<int:input_val>')
def show_grade(input_val):
    grade = ""
    if input_val >= 90:
        grade += "A+"
    elif 90 > input_val >= 85:
        grade += "A"
    elif 85 > input_val >= 80:
        grade += "A-"
    elif 80 > input_val >= 75:
        grade += "B+"
    elif 75 > input_val >= 70:
        grade += "B"
    elif 70 > input_val >= 65:
        grade += "B-"
    elif 65 > input_val >= 60:
        grade += "C+"
    elif 60 > input_val >= 55:
        grade += "C"
    elif 55 > input_val >= 50:
        grade += "C-"
    elif 50 > input_val >= 45:
        grade += "D+"
    elif 45 > input_val >= 40:
        grade += "D"
    elif 40 > input_val >= 0:
        grade += "D-"
    else:
        grade += "N/A"

    return render_template('results.html',
                           result=grade
                          )


if __name__ == '__main__':
    app.run(debug=True, port=8000)
