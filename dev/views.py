from flask import Flask, render_template
import logging

app = Flask(__name__)



@app.route("/")
def index():
    return render_template('components/base.html')

@app.route("/register/")
def register():
    return render_template('auth/register.html')
 
@app.route("/dashboard/")
def dashboard():
    return render_template('dashboard.html')

if __name__ == "__main__":
    app.run()

app.config.from_object('config')