from flask import Flask, render_template,request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

@app.route('/', methods=['GET','POST'])
def index():
    title_book = False

    form = InfoForm()

    if form.validate_on_submit():
        title_book = form.title_book.data
        form.title_book.data = " "
    return render_template('home.html', form=form, title_book=title_book)



@app.route('/books')
def book_name():
    return render_template('booksadd.html')

@app.route('/signup')
def sign_up():
    return render_template('signup.html')

@app.route('/thankyou')
def thankYou():

    first = request.args.get ('first_name')
    last  = request.args.get ('last_name')

    return render_template('thankyou.html', first=first, last=last)










######################################

class InfoForm(FlaskForm):

    title_book = StringField("What is name of the book?")
    author_book = StringField("What is the name of the author?")
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(err):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)