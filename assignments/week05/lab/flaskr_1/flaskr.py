import sqlite3
from contextlib import closing

from flask import Flask
from flask import g
from flask import render_template
from flask import session
from flask import request
from flask import redirect
from flask import flash
from flask import url_for
from flask import abort


# configuration goes here
DATABASE = 'C:\\tmp\\flaskr.db'
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'

app = Flask(__name__) # this is already in the file
app.config.from_object(__name__)


# add the rest of this below the app.config statement
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()
# add these function after init_db
@app.before_request
def before_request():
    g.db = connect_db()
    
def write_entry(title, text):
    g.db.execute('insert into entries (title, text) values (?, ?)', [title, text])
    g.db.commit()

def get_all_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return entries


# and after our last functions:
@app.route('/')
def show_entries():
    entries = get_all_entries()
    return render_template('show_entries.html', entries=entries)


# and a function
def do_login(usr, pwd):
    if usr != app.config['USERNAME']:
        raise ValueError
    elif pwd != app.config['PASSWORD']:
        raise ValueError
    else:
        session['logged_in'] = True
        
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        try:
            do_login(request.form['username'],
                     request.form['password'])
        except ValueError:
            error = "Invalid Login"
        else:
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    try:
        write_entry(request.form['title'], request.form['text'])
        flash('New entry was successfully posted')
    except sqlite3.Error as e:
        flash('There was an error: %s' % e.args[0])
    return redirect(url_for('show_entries'))        
        
@app.teardown_request
def teardown_request(exception):
    g.db.close()


        



if __name__ == '__main__':
    app.run(debug=True)
