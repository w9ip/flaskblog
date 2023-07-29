from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '37c0537c817855d926550fcc07bb84b6'

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


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
