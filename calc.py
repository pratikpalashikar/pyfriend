from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


class ReusableForm(Form):
    friend = TextField('YourName:', validators=[validators.required()])
    friend1 = TextField('Friend Name:', validators=[validators.required()])



@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
    if request.method == 'POST':
        yourname = request.form['friend']
        friendname = request.form['friend1']
        if form.validate():
            x = len(yourname)
            y = len(friendname)
            if x>y:
                result = (float(y)/float(x))*100.0
                flash(round(result,2))
            elif y>x:
                result = (float(x)/float(y))*100.0
                flash(round(result,2))
            else:
                result = (float(x) / float(y)) * 100.0
                flash(round(result, 2))


        else:
            flash('All the form fields are required. ')

    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run()