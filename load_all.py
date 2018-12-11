"""
Template for creating and loading a table. Assuming you have a TAB-SEPARATED file structured
with the first row as the header (the column names), and subsequent rows are the entries
in the table with tab-separated values, set DATA_FILE_PATH to the path of that file

Change the import statement to import db as well as the table you are loading.
Also change the name on line 25. In Terminal, navigate to the directory where your
application.py file is, start the Python shell, and then copy/paste this code.

You can check whether it was successfully by quering for the entire table:
[TABLE NAME].query.all() should give you back a list of all of the entries.
e.g. Student.query.all() => [<Student 0>, <Student 1>,..., <Student 6216>]
"""

from application import db, Usage, Aggregateusage, Building, Student
DATA_FILE_PATH = "./data/usage.tsv"

db.drop_all()
db.create_all()

# print(result.first())
# exec(open("./load_all.py").read())

# Load Usage
print("loading Usage...")

with open(DATA_FILE_PATH) as file:
	header = next(file).rstrip().split()
	header = [x.lower() for x in header]
	#print header
	for line in file:
		attrs = {(att if att != "rowid" else "usage_id"): val for att, val in zip(header, line.rstrip().split('\t'))}
		#attrs = {att: val for att, val in zip(header, line.rstrip().split('\t'))}
		# print(attrs)
		# break
		row = Usage(**attrs)
		db.session.add(row)
		#print Usage.serialize(row)

db.session.commit()

# Load Aggregateusage
print("loading Aggregateusage...")

results = db.engine.execute('SELECT usage_id, facid, buildingname, usagemonth, SUM(globaluse), SUM(globalsqftuse) FROM "USAGE" GROUP BY buildingname, usagemonth')

for item_list in results:
	item_list = {
		"usage_id": item_list[0],
		"facid": item_list[1],
		"buildingname": item_list[2],
		"usagemonth": item_list[3],
		"globaluse": item_list[4],
		"globalsqftuse": item_list[5]
	}
	row = Aggregateusage(**item_list)
	db.session.add(row)

db.session.commit()

# Load Building
print("loading Building...")

DATA_FILE_PATH = "./data/buildings.tsv"

with open(DATA_FILE_PATH) as file:
	header = next(file).rstrip().split()
	header = [x.lower() for x in header]
	#print header
	for line in file:
		attrs = {att: val for att, val in zip(header, line.rstrip().split('\t'))}
		#attrs = {att: val for att, val in zip(header, line.rstrip().split('\t'))}
		# print(attrs)
		# break
		row = Building(**attrs)
		db.session.add(row)
		#print Building.serialize(row)

db.session.commit()

# Load Student
print("loading Student...")

DATA_FILE_PATH = "./data/students.tsv"

with open(DATA_FILE_PATH) as file:
	header = next(file).rstrip().split()
	header = [x.lower() for x in header]
	#print header
	for line in file:
		attrs = {att: val for att, val in zip(header, line.rstrip().split('\t'))}
		#attrs = {att: val for att, val in zip(header, line.rstrip().split('\t'))}
		# print(attrs)
		# break
		row = Student(**attrs)
		db.session.add(row)

db.session.commit()

