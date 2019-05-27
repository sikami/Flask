from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app = Flask(__name__)

app.config['SECRET_KEY'] = 'd4746689083660e86ef9647cf8bacf3d'
# URI database - next time change to heroku URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#put class for database
class User(db.model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = true, nullable = False)
    email = db.Column(db.String(120), unique = true, nullable = False)
    image_file = db.Column(db.String(20), nullable = False, default = 'default.jpg')
    password = db.Column(db.String(60), nullable = False)

    def __repr__(self):
        return "User('{}', '{}', '{}'" .format(self.username, self.email, self.image_file)

class Post(db.model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date_post = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    content = db.Column(db.Text, nullable = False)

    def __repr__(self):
        return "Post({}, {})".format(self.title, self.date_post)
#corey vid part 4, 14:59-ish

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

@app.route("/login", methods=['GET', 'POST'])
def login ():
    form = LoginForm() 
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return(url_for('home'))
        else:
            flash('Sorry, you are not logged in. Please check your username and password', 'danger')
    return render_template('login.html', title='login', form=form)

if __name__ == '__main__':
    app.run(debug=True)