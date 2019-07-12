from flask import Flask,render_template,request,redirect,url_for,session

app=Flask(__name__)
app.secret_key="nethra"

@app.route("/")

def home():
	return render_template("home.html")

@app.route("/about")

def about():
	return render_template("about.html")


@app.route("/contact")
def contact():
	return render_template("contact.html")

@app.route("/login",methods=['GET','POST'])
def login():
	if request.method=='POST':
		users={'user1':'123','user2':'345','user3':'658'}
		username=request.form['username']
		password=request.form['password']

		if username not in users :
			return "user dosent exists .go back enter valid name "

		if users[username]!=password:
			return "password doesnt match .go back enter password"
		session['username']=username
		redirect(url_for('home'))
	return redirect(url_for('home'))

@app.route("/logout")
def logout():
	session.clear()
	return redirect(url_for('home'))





app.run(debug=True)