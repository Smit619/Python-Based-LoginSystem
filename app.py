from flask import Flask,request,render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def login_page():
	return render_template("login.html")

@app.route('/form_login', methods=['POST','GET'])
def login():

	con = sqlite3.connect('templates/data_book.db')
	c = con.cursor()

	c.execute("SELECT * FROM admin")
	attribute = c.fetchall()

	enrollmentnos = []
	names = []
	passwords = []
	for student_data in attribute:
		enrollmentnos.append(student_data[0])
		names.append(student_data[1])
		passwords.append(student_data[2])

	con.close()

	data1 = dict(zip(enrollmentnos,passwords))
	data2 = dict(zip(enrollmentnos,names))

	if 'login_button' in request.form:
		number = request.form['enrollmentno']
		pwd = request.form['password']
		if number not in enrollmentnos:
			return render_template("login.html", status = "Your enrollment number is not registered")
		else:
			if data1[number] != pwd:
				return render_template("login.html", status = 'Invalid password')
			else:
				return render_template("welcome_page.html",name = data2[number])

	elif 'register_button' in request.form:
		return render_template("register.html")

@app.route('/form_register', methods=['POST','GET'])
def store():

	enrollno = request.form['enrollmentno']
	name = request.form['name']
	pwd = request.form['password']

	con = sqlite3.connect('templates/data_book.db')
	c = con.cursor()

	c.execute("")

	c.execute("INSERT INTO admin VALUES (:enrollmentno, :name, :password)",
			{
				'enrollmentno' : enrollno,
				'name' : name,
				'password' : pwd
			}
		)

	con.commit()
	con.close()

	return render_template("login.html", status = 'Your data is registered')

if __name__ == "__main__":
	app.run()