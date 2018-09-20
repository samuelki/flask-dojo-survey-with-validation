from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
app.secret_key = 'ThisIsSecret!'

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def result():
    session['name'] = request.form['name']
    session['dojo'] = request.form['dojo']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']

    if len(session['name']) < 1:
        flash("Name cannot be empty!")
    if len(session['comment']) < 1:
        flash("A comment must be provided!")
    if len(session['comment']) > 120:
        flash("Comment must not be longer than 120 characters!")

    if '_flashes' in session.keys():
        return redirect('/')
    else:
        return render_template('success.html')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)