from flask import Flask, render_template, url_for

app = Flask(__name__)


posts = [
    {
        'author': 'Bulgakov M.A.',
        'title': 'Blog post 1',
        'content': 'First post contetn',
        'date_posted': 'April 20, 2023'
    },
    {
        'author': 'Dostoevskiy M.A.',
        'title': 'Blog post 2',
        'content': 'Second post contetn',
        'date_posted': 'April 21, 2023'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
