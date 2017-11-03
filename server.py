from flask import Flask, render_template, session
app = Flask(__name__)
app.secret_key = "secret"
@app.before_first_request
def cookiez():
    session['count']=0

@app.route('/')
def index():
    session['count'] += 1
    return render_template('index.html')

@app.route('/twice')
def twice():
    session['count'] += 2
    return render_template("index.html")

@app.route('/reset')
def reset():
    session['count']=1
    return render_template('index.html')
app.run(debug=True)
