from flask import Flask, render_template
import logging

app = Flask(__name__)



@app.route("/")
def index():
    return render_template('components/base.html')

@app.route("/register/", methods=['GET', 'POST'])
def register():
    if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'email' in request.form:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        print(name)
        print(email)
        print(password) 
    return render_template('auth/register.html')
 
@app.route("/dashboard/")
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run()

app.config.from_object('config')