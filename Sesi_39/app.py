from markupsafe import escape
from flask import Flask, render_template, url_for, request
import webbrowser
from author_book import author_book

app = Flask(__name__)

#
# @app.route('/')# will hit url/ || 127.0.0.1/ 
# def helloW():
#     sum = 9
#     pageContent = f'Hello World! {sum}'

#     pageContent += "<i> italic Hello </i>"

#     return pageContent

#     # return f'Hello World! {sum}'
#     # return '<h1>Hello World!</h1> {}'.format(sum)

# @app.route('/<name>') #url/name / url/variabel parameter
# def hello(name):
#     # return 'Hello, {name}'
#     return f"Hello, { escape(name) } "

# @app.route('/Hello/<name>')
# def helloTemplate(name=None):    
#     return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'


@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

@app.route('/books')
def books():
    return 'Ini Books'

@app.route('/author', methods=['GET', 'POST'])
def author():

    if 'authorId' in request.form:
        author_book[request.form['authorId']] = []#empty list
    
    return render_template('author.html', author_book=author_book)

@app.route('/books/authorId')
def book(authorId):
    return render_template('book.html', authorId=authorId, book_list=author_book[authorId])


# apakah dijalankan sebagai stand alone
if __name__ == '__main__':
    app.run(debug=True)
    webbrowser.open_new('http://127.0.0.1:5000/')



