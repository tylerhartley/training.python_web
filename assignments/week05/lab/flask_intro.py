from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

    
@app.route('/profile/<username>/')
def show_profile(username):
    return "My username is %s" % username
    
@app.route('/div/<float:val>/')
def divide(val):
    return "%0.2f divided by 2 is %0.2f" % (val, val / 2)
    
@app.route('/blog/entry/<int:id>/', methods=['GET',])
def read_entry(id):
    return "reading entry %d" % id

@app.route('/blog/entry/<int:id>/', methods=['POST', ])
def write_entry(id):
    return 'writing entry %d' % id

from flask import render_template

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)
    
    
if __name__ == '__main__':
    app.run(debug=True)