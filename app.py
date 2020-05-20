from flask import Flask, request, render_template, session, redirect, url_for, g
from validate_email import validate_email
#import db_sqlite3
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
import hashlib
from flask_login import login_manager, UserMixin, login_required
conn = sqlite3.connect('CyberPPW2Database.db')
conn.close()

class User:
    def __init__(self, username):
        self.username = username


users = []


app = Flask(__name__)
app.secret_key = 'asecretkey'


@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user

@app.route('/createaccount')
def createaccount():
    return render_template('createaccount.html')


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/login')
def login():

    return render_template('login.html')



@app.route('/submitcreateform', methods=['POST'])
def submitcreateform():
    """
        Check that a user id is valid (i.e. the user exists)
        :return: A boolean value indicating whether or not the user ID provided is valid
        """
    conn = sqlite3.connect('CyberPPW2Database.db')
    c = conn.cursor()
    user_fullname = request.form['userFullName'].strip()
    user_email = request.form['userEmail'].strip()
    user_pwd = request.form['userPassword'].strip()
    hashed_value = generate_password_hash(user_pwd)

    is_valid = bool(validate_email(user_email, verify=True))

    #c.execute("INSERT INTO user (userID, userEmail, userPassword, userFullname) VALUES ('', "+ user_email +", "+user_pwd+","+ user_fullname")")
    #c.execute("INSERT INTO user (userID, userEmail, userPassword, userFullname) VALUES (2, 'user_email', 'user_pwd', 'user_fullname')")
    c.execute("""INSERT INTO user (id, userEmail, userPassword, userFullname) VALUES (?, ?, ?, ?);""", (None, user_email, hashed_value, user_fullname))
    conn.commit()
    conn.close()
    return user_email +" "+ user_pwd +" "+ user_fullname +" "+ str(is_valid) +" "+ hashed_value

@app.route('/submitloginform', methods=['POST', 'GET'])
def submitloginform():

    if request.method == 'POST':
        session.pop('user_id', None)
        conn = sqlite3.connect('CyberPPW2Database.db')
        c = conn.cursor()

        user_fullname = request.form['userFullName'].strip()
        user_email = request.form['userEmail'].strip()
        user_pwd = request.form['userPassword'].strip()
        hashed_value = generate_password_hash(user_pwd)
        #hashed_test = generate_password_hash('egg')
        # find_user = """SELECT userFullname FROM user WHERE (userEmail) == (?);""",(user_email)
        # c.execute(find_user, user_fullname)
        #find_user = str("""SELECT userPassword FROM user WHERE (userEmail) == (?);""", user_email)
        #c.execute(find_user)
        print(user_email)
        c.execute("""SELECT userPassword FROM user WHERE (userEmail) == (?);""", (user_email,))

        results = c.fetchone()

        print(results)
        print(results[0])
        print(type(results))
        print(user_pwd)
        print(type(user_pwd))
        verify = check_password_hash(str(results[0]), str(user_pwd))

        conn.commit()
        conn.close()
        users.append(User(username=user_fullname))
        print(session)
        #if 'user_id' in session:
         #   user = [x for x in users if x.id == session['user_id']][0]
          #  g.user = user
        print(g.user)
        print(g.user)
        print(results)
        print(user_pwd)
        print(hashed_value)

        print(verify)
        if verify == True:
            session['user_id'] = user_fullname
            g.user = user_fullname
            print(session)
            #print(user)
            print(users)
            print(g.user)
            return redirect(url_for('profile'))
        return 'yo'
    return render_template(login.html)

@app.route('/profile')
def profile():
    print(g.user)
    print(g.user)
    print(type(User))
    print(g.user)
    print(g.user)
    if not g.user:
        return render_template('login.html')
    return render_template('profile.html')
    # if results:
    #     for i in results:
    #         return i
    #c.execute("""SELECT * FROM user WHERE (userEmail) == (?);""",(user_email,))
    #List = [c.execute("""SELECT * FROM user WHERE '1=1'""")],







    #@app.route('/<username>')
    #def profile(username):
    #    return "Hello %s " % username
#yeet
#pbkdf2:sha256:150000$bCGt62I6$574858f2919c59134b10e95fed6487f98dc31e8a83df77946782f89220ef3c03

if __name__ == '__main__':
    app.run(debug=False)
    app.run(host='0.0.0.0', port=5000)
