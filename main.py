from flask import Flask, render_template,request

app=Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')


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


@app.errorhandler(404)
def page_not_found(err):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)