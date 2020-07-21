import sqlite3

con = sqlite3.connect('data_book.db')
c = con.cursor()

c.execute("INSERT INTO admin VALUES (:enrollmentno, :name, :password)",
		{
			'enrollmentno' : '171200107027' ,
			'name' : 'Smit',
			'password' : '12345'
		}
	)
		
con.commit()
con.close()
