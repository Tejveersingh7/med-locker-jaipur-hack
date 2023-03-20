from flask import Flask, render_template, request, redirect, session, url_for, flash
import mysql.connector
from flask_mysqldb import MySQL, MySQLdb
import MySQLdb.cursors
from werkzeug.utils import secure_filename
import re
import os
import urllib.request
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import json
from wtforms.validators import ValidationError
import datetime
import base64
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
import cloudinary
import cloudinary.uploader
import cloudinary.api
import os
import asyncio










cloudinary.config(
  cloud_name = "dirxr9ttg",
  api_key = "872352612882821",
  api_secret = "3nbqeEtddaw6DKr_oRIs0-PytOg",
  secure = True
)

# upload("https://media-cldnry.s-nbcnews.com/image/upload/newscms/2021_05/3447991/210205-home-health-certificate-mn-1237.png", public_id="olympic_flag")



local_server = True

with open('config.json', 'r') as c:
    params= json.load(c)["params"]



app = Flask(__name__)
app.secret_key = '12345'











#SQLAlchemy connection 

if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']

db = SQLAlchemy(app)














#mysql.connection- for login

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'user-system'

mysql = MySQL(app)

















class User(db.Model):
    userid = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.VARCHAR(100), nullable=False)
    email = db.Column(db.VARCHAR(100), unique=True, nullable=False)
    password = db.Column(db.VARCHAR(255), nullable=False)


class Doc_credentials(db.Model):
    doc_aadhar = db.Column(db.Integer, primary_key=True, nullable=False)
    doc_name = db.Column(db.VARCHAR(100), nullable=False)
    doc_password = db.Column(db.VARCHAR(255), nullable=False)
    doc_email = db.Column(db.VARCHAR(100), unique=True, nullable=False)


class Records(db.Model):
    s_no = db.Column(db.Integer, primary_key=True, nullable=False)
    userid = db.Column(db.Integer, primary_key=False, nullable=False)
    name_of_report = db.Column(db.Text(100), nullable=False)
    name_of_clinic = db.Column(db.VARCHAR(100), nullable=False)
    report_img = db.Column(db.LargeBinary(), unique=True, nullable=False)
    date = db.Column(db.DateTime(255), nullable=False)
   



ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'fgif'])

def allowed_file(filename):
 return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS







@app.route("/")
def home():
    return render_template('index.html', params = params)








@app.route('/login', methods =['GET', 'POST'])
def login():
    
    

    return render_template('loginpage.html', params = params)


















@app.route('/patientloginform', methods =['GET', 'POST'])
def patientloginform():
      mesage = ''
      if request.method == 'POST' and 'userid' in request.form and 'password' in request.form:
        userid = request.form['userid']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user WHERE userid = % s AND password = % s', (userid, password, ))
        user = cursor.fetchone()
        # cursor.execute('SELECT name_of_doctor FROM records WHERE userid = % s ', (userid, ))
        # record_info = cursor.fetchone()
        
        
        if user:
            username = user["name"]
            session['loggedin'] = True
            session['userid'] = user['userid']
            session['name'] = user['name']
            session['email'] = user['email']
            mesage = 'Logged in successfully !'
            return render_template('dashboard.html', username=username)
        else:
            mesage = 'Please enter correct User ID / password !'


      return render_template('patientloginform.html', params = params, mesage = mesage)












@app.route('/medicine_query', methods =['GET', 'POST'])
def medicine_query():
      
    if request.method == 'POST' and 'medicine_query' in request.form:
        medicine_query=request.form['medicine_query']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT  medicine_quantity FROM hospital_1 WHERE medicine_name = % s UNION SELECT medicine_quantity FROM hospital_2 WHERE medicine_name = % s', (medicine_query, medicine_query))
        query = cursor.fetchone()


        if(query):
            
            return render_template('medicinepage.html', query=query)




    return render_template('medicinepage.html')





@app.route('/doc_login', methods =['GET', 'POST'])
def doctor_login():
      mesage = ''
      if request.method == 'POST' and 'doc_aadhar' in request.form and 'doc_password' in request.form:
        userid = request.form['doc_aadhar']
        password = request.form['doc_password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM doc_credentials WHERE doc_aadhar = % s AND doc_password = % s', (userid, password, ))
        user = cursor.fetchone()
        
    
        if user:
            username = user["doc_name"]
            # session['loggedin'] = True
            # session['userid'] = user['userid']
            # session['name'] = user['name']
            # session['email'] = user['email']
            # mesage = 'Logged in successfully !'
            return render_template('doctor_dashboard.html')
        else:
            mesage = 'Please enter correct User ID / password !'


      return render_template('doctor_login.html', params = params, mesage = mesage)























@app.route("/temp_doctor_login",methods=["GET","POST"])
async def upload():


    # if(request.method=="POST"):
    #   file_to_upload = await request.files['filename']

    # if file_to_upload:
    #     upload_result = cloudinary.uploader.upload(file_to_upload)
    #     app.logger.info(upload_result)    

    
    
     

    return render_template('doctor_login.html')

# @app.route("/temp_doctor_login",methods=["GET","POST"])
# def upload():
#     if(request.method=='POST'):
#        a_no = request.form.get('userid')
#        name_of_report = request.form.get('name_of_report')
#        name_of_clinic = request.form.get('name_of_clinic')
#        report_img = request.form.get('filename')
#        file = base64.b64encode(report_img)
#        date=datetime.date.today()
       


#        args = (a_no, name_of_report, name_of_clinic, file, date)
#        query = 'INSERT INTO records VALUES(3, %s, %s, %s, %s, %s)'
       
#        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#        cursor.execute(query,args)
#        mysql.connection.commit()

#     return render_template('doctor_login.html')
















@app.route('/register', methods =['GET', 'POST'])
def register():
    if(request.method=='POST'):
       name = request.form.get('name')
       a_no = request.form.get('userid')
       email = request.form.get('email')
       password = request.form.get('pswd')
       entry = User( userid=a_no, name=name, email=email, password=password )   
       db.session.add(entry)
       db.session.commit()



    


   
    return render_template('registerr.html', params = params)




if __name__ == "__main__":
    app.debug = True
    app.run() 
   
