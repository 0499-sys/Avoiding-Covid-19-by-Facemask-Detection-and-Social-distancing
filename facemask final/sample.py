from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
import mysql.connector
from flask import redirect
import re
regex= '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

app = Flask(__name__,template_folder='template')

message=''
 
@app.route('/')
def index():
    return render_template('login.html')


@app.route('/save' ,methods = ['GET','POST'])
def save():
    s1 = request.args['email']
    s2 = request.args['psw']
    con=mysql.connector.connect(user="root",password="",host="localhost",database="finalyearprojectdb")
    cur=con.cursor()
    cur.execute("select * from signup where email = %s", (s1,))
    a=cur.fetchall()
    for row in a:
        if(s1==row[1] and s2==row[2]):
            return "Your username is {} and your password is {}".format(s1,s2)
            con.commit()
            con.close()
            cur.close()

    return render_template('login.html',message="Emailid or Password is wrong")

@app.route('/signup' ,methods = ['GET','POST'])
def signup():
    return render_template('signup.html') 

@app.route('/signupdata' ,methods = ['GET','POST'])
def signupdata():
    s1 = request.args['name']
    s2 = request.args['email']
    match = re.search(regex, s2)
    s3 = request.args['psw']
    s4 = request.args['cpsw']
    s5 = request.args['gender']

    if(s1=="" or s2=="" or s3=="" or s4=="" or s5==""):
        message = "please fill all the fields, all fields are required"
        return render_template('signup.html',message=message)

    if match==None:
        message="Enter valid email address"
        return render_template('signup.html',message=message)

    if s3!=s4:
        message="Please enter correct password"
        return render_template('signup.html',message=message)

    else:
        con=mysql.connector.connect(user="root",password="",host="localhost",database="finalyearprojectdb")
        cur=con.cursor()
        cur.execute("insert into signup values(%s,%s,%s,%s,%s)",(s1,s2,s3,s4,s5))

        con.commit()
        con.close()
        cur.close()
        return "Your username is {} , email is {} , password is {} and gender is {}".format(s1,s2,s2,s5)

@app.route('/login' ,methods = ['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/forgotpassword')
def forgotpassword():
 return render_template("forgotpass.html")

@app.route('/forgotpass' ,methods = ['GET','POST'])
def forgotpass():
    s1 = request.args['emailid']
    con = mysql.connector.connect(user="root", password="", host="localhost", database="finalyearprojectdb")
    cur = con.cursor()
    cur.execute("select * from signup where email = %s", (s1,))
    a=cur.fetchall()
    for row in a:
        name=row[0]
        password=row[2]   # message = "Hello Your password is {}".format(pass)
    con.commit()
    con.close()
    cur.close()
    if a:
        import smtplib
        content="""
        Hello! {} 
        Your Password is {}.""".format(name,password)
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login("nnrsproject2019@gmail.com","nnrs@123")
        server.sendmail("nnrsproject2019@gmail.com","{}".format(s1),content)
        server.quit()
    return render_template('/forgotpass.html',message="password is sent to your registered email address. Thank you!")

app.run(debug=True, port=5000)    