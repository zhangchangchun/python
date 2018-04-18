from flask import Flask,request
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<h1>Hello World ! </h1><h2>%s</h2>' % user_agent

@app.route('/user/<name>')
def user(name):
        return "<h1>Hello %s" % name

if __name__=="__name__":
    app.run(debug=True,host='0.0.0.0')
