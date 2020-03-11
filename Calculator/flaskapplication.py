from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import Required

class NameForm(Form):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('Submit')

class CalcForm(Form):
    name1 = FloatField('What is your first value?', validators=[Required()], default=0)
    name2 = StringField('Operation? (+, -, *, /)', validators=[Required()])
    name3 = FloatField('What is your last value?', validators=[Required()], default=0)
    submit = SubmitField('Submit')

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = '7cwtzhl0tkg9obj9'



@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name)

""" Load personal"""
@app.route('/calculator', methods=['GET', 'POST'])
def calc():
    name = None
    form = CalcForm()
    if form.validate_on_submit():
        a = form.name1.data
        op = form.name2.data
        b = form.name3.data

        flag = r =  0
        if op == "+":
            r = a + b
        elif op == "-":
            r = a - b
        elif op == "*":
            r = a * b
        elif op == "/":
            try:
                r = a / b
            except:
                r = 0
        else:
            name = "Wrong Operation"
            flag = 1

        if flag == 0:
            name = ("Result of the Operation : %.4f" % r)

    return render_template('calc.html', form=form, name=name)
""" Load personal"""

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
