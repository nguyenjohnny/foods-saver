from flask import Flask, render_template, url_for 
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

app.config['SECRET_KEY'] = ''


posts = [
		{
		'author': 'Johnny Nguyen',
		'title': 'Blog post 1',
		'content': 'First post content',
		'date_posted': 'Oct 3, 2018',
	},
	{
		'author': 'Jane Nguyen',
		'title': 'Blog post 2',
		'content': 'second post content',
		'date_posted': 'Oct 4, 2018',
	},
]

@app.route("/")    
@app.route("/home")  
def home():
    return render_template('home.html', posts=posts)  


@app.route("/about")  
def about():
    return render_template('about.html', title='About')


@app.route('/register')
def register():
	form = RegistrationForm()
	return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
	form = LoginForm()
	return render_template('login.html', title='login', form=form)
 
if __name__ == '__main__':
	app.run(debug=True)
