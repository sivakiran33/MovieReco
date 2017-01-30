
#from flask import Flask, render_template, redirect, url_for, request, session
from flask import * #Imports all required modules
app = Flask(__name__) #Flask application is run from here
#from app import app
app.secret_key='6264' #Session secret key
@app.route("/") #Home page as referenced by index.html page, for navigation
def main():
    return render_template('index.html')
@app.route("/welcome") #welcome page
def welcome(): 
    return render_template('welcome.html')
@app.route("/main") #main page, can be naviagated from the UI window
def home(): #home page for movie recommendation engine
    return render_template('index.html')
@app.route('/showSignUp') #sign up page
def showSignUp():
    return render_template('index.html') #shows sign up page and brings up a form to enter data
@app.route('/showSignIn', methods=['GET', 'POST'])
def showSignIn(): #sign in page, brings up a form to sign in.
     return render_template('signin.html')
@app.route("/archean") #my home page
def archean():
     return render_template('index.html')
@app.route('/login',methods=['GET','POST']) #login page with http methods like get and post
def login():
     error = None
     if request.method == 'POST':
	if request.form['username'] != 'admin' or request.form['password'] != 'admin':
		error = 'Invalid Credentials. Try Again.'
	else:
		session['logged_in']= True
		return redirect(url_for('archean'))
     return render_template('login.html', error = error) 
@app.route('/logout')#log out page
def logout():
     session.pop('logged_in', None)
     return redirect(url_for('home'))
@app.route('/mostwatched')
def mostwatched():
     return render_template('mostwatched.html')
@app.route('/highestratings')
def highestratings(): #highest ratings page
     return render_template('/highestratings.html')
@app.route('/recommended') #recommended page
def recommended():
     return render_template('/recommended.html')
@app.route('/superhero') #superhero page which gives the most popular superhero
def superhero():
     return render_template('/superhero.html')
@app.route('/sim1') #similar movies page
def sim1():
     return render_template('sim1.html')
if __name__ == "__main__":
    app.run(debug=True) 
