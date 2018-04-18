from flask import Flask,request,render_template
from flask_script import Manager

app = Flask(__name__)
manage = Manager(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

if __name__ == "__main__":
    #manage.run()
    app.run(debug=True,host='0.0.0.0')