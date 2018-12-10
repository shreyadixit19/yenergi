"""
Template for creating a loading a table. Assuming you have a TAB-SEPARATED file structured
with the first row as the header (the column names), and subsequent rows are the entries
in the table with tab-separated values, set DATA_FILE_PATH to the path of that file

Change the import statement to import db as well as the table you are loading.
Also change the name on line 25. In Terminal, navigate to the directory where your
application.py file is, start the Python shell, and then copy/paste this code.

You can check whether it was successfully by quering for the entire table:
[TABLE NAME].query.all() should give you back a list of all of the entries.
e.g. Student.query.all() => [<Student 0>, <Student 1>,..., <Student 6216>]
"""

from application import db, Building

DATA_FILE_PATH = "./data/buildings.tsv"

db.create_all()

with open(DATA_FILE_PATH) as file:
	header = next(file).rstrip().split()
	header = [x.lower() for x in header]
	print header
	for line in file:
		attrs = {att: val.decode('utf-8') for att, val in zip(header, line.rstrip().split('\t')) if att in header}
		if len(attrs) >= 16: 
			#attrs = {att: val for att, val in zip(header, line.rstrip().split('\t'))}
			row = Building(**attrs)
			db.session.add(row)
		else: 
			print Building.serialize(row)
db.session.commit()
result = db.engine.execute('SELECT * FROM "Building"')
for _r in result:
   print(_r)
#print result.first()

exit()
