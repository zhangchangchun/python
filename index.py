from flask import Flask,request,render_template
from flask_script import Manager

app = Flask(__name__)
manage = Manager(app)

@app.route('/')
def index():
    return render_template('./tpl/index.html')

if __name__ == "__main__":
    manage.run()