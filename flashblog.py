from flask import Flask, render_template, url_for
app = Flask(__name__)

app.config['SECRET_KEY'] = '82c4a7a2db2483bbfc842389e16c7d0d'

posts = [
    {
        'author': 'Listya Widyasari',
        'title': 'Maximorphimus',
        'content': 'Maximus Journal',
        'date_posted': '24th February 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'The King',
        'content': 'Documentary about a king in the early period of human kind',
        'date_posted': '22th February 2019'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

if __name__ == '__main__':
    app.run(debug=True)