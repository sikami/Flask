from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'd4746689083660e86ef9647cf8bacf3d'

posts = [ 
    {   'author': 'Listya W',
        'title': 'Maximorphimus',
        'content': 'Maximus Journal',
        'date_posted': ' 02 April 2019'},
    {
        'author': 'Jane Doe',
        'title': 'Wuthering Heights',
        'content': 'A novel',
        'date_posted': ' 02 April 2018'
    },

    {
        'author': 'Raditya Purnama',
        'title': 'Kenallah Aku Dengan Nama Adrian',
        'content': 'Cerita tentang Adrian',
        'date_posted': ' 08 August 2019'
    }
]

@app.route("/")
def home ():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about ():
    return "<h1>About Page</h1>"

@app.route("/register", methods=['GET', 'POST'])
def register ():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login ():
    form = LoginForm ()
    return render_template('login.html', title='login', form=form)

if __name__ == '__main__':
    app.run(debug=True)