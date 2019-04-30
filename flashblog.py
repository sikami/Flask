from flask import Flask, render_template, url_for
app = Flask(__name__)

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

@app.route("/registration")
def registration ():
    return render_template('register.html', title='register', form=form)

@app.route("/login")
def login ():
    return render_template('login.html', title='login', form=form)

if __name__ == '__main__':
    app.run(debug=True)