from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
# import usage_load_template
from flask_heroku import Heroku

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
heroku = Heroku(app)
db = SQLAlchemy(app)
CORS(app)


class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.String(10))
    college = db.Column(db.String(80))
    major = db.Column(db.String(120))

    # returns dictionary form of data
    def serialize(self):
    	return {
			"student_id": self.student_id,
			"year": self.year,
			"college": self.college,
			"major": self.major,
		}

class Building(db.Model):
	building = db.Column(db.String(255), primary_key=True)
	status = db.Column(db.String(255))
	description = db.Column(db.String(255))
	historical_alias = db.Column(db.String(255))
	address_3 = db.Column(db.String(255))
	site = db.Column(db.String(255))
	longitude = db.Column(db.String(255))
	msag_alias = db.Column(db.String(255))
	historical_name = db.Column(db.String(255))
	address_1 = db.Column(db.String(255))
	address_2 = db.Column(db.String(255))
	building_abbr = db.Column(db.String(255))
	latitude = db.Column(db.String(255))
	addr1_alias = db.Column(db.String(255))
	usage_description = db.Column(db.String(255))

	def serialize(self):
		return {
			"site": self.site,
			"building": self.building,
			"building_abbr": self.building_abbr,
			"description": self.description,
			"usage_description": self.usage_description,
			"address_1": self.address_1,
			"address_2": self.address_2,
			"address_3": self.address_3,
			"status": self.status,
			"historical_alias": self.historical_alias,
			"addr1_alias": self.addr1_alias,
			"msag_alias": self.msag_alias,
			"latitude": self.latitude,
			"longitude": self.longitude,
			"historical_name": self.historical_name,
		}

class Usage(db.Model):
	usage_id = db.Column(db.Integer, primary_key=True)
	campus = db.Column(db.String(255))
	utilityarea = db.Column(db.String(255))
	facid = db.Column(db.String(255))
	buildingname = db.Column(db.String(255))
	sqr_feet = db.Column(db.String(255))
	commodityinfo = db.Column(db.String(255))
	usagemonth = db.Column(db.String(255))
	nativeuse = db.Column(db.String(255))
	nativeuseunit = db.Column(db.String(255))
	commonuse = db.Column(db.String(255))
	commonuseunit = db.Column(db.String(255))
	globaluse = db.Column(db.String(255))
	globaluseunit = db.Column(db.String(255))
	globalsqftuse = db.Column(db.String(255))
	globalsqftuseunit = db.Column(db.String(255))

	def serialize(self):
		return {
			"usage_id": self.usage_id,
			"campus": self.campus,
			"utilityarea": self.utilityarea,
			"facid": self.facid,
			"buildingname": self.buildingname,
			"sqr_feet": self.sqr_feet,
			"commodityinfo": self.commodityinfo,
			"usagemonth": self.usagemonth,
			"nativeuse": self.nativeuse,
			"nativeuseunit": self.nativeuseunit,
			"commonuse": self.commonuse,
			"commonuseunit": self.commonuseunit,
			"globaluse": self.globaluse,
			"globaluseunit": self.globaluseunit,
			"globalsqftuse": self.globalsqftuse,
			"globalsqftuseunit": self.globalsqftuseunit,
		}

class Aggregateusage(db.Model):
	usage_id = db.Column(db.String(255), primary_key=True)
	buildingname = db.Column(db.String(255))
	facid = db.Column(db.String(255))
	usagemonth = db.Column(db.String(255))
	globaluse = db.Column(db.String(255))
	globalsqftuse = db.Column(db.String(255))

	def serialize(self):
		return {
			"usage_id": self.usage_id,
			"facid": self.facid,
			"buildingname": self.buildingname,
			"usagemonth": self.usagemonth,
			"globaluse": self.globaluse,
			"globalsqftuse": self.globalsqftuse,
		}

class Weather(db.Model):
	date = db.Column('date', db.String(255), primary_key=True)
	station = db.Column(db.String(255))
	name = db.Column(db.String(255))
	awnd = db.Column(db.String(255))
	snow = db.Column(db.String(255))
	tavg = db.Column(db.String(255))
	tmax = db.Column(db.String(255))
	tmin = db.Column(db.String(255))




	def serialize(self):
		return {
			"date": self.date, 
			"station": self.station,
			"name": self.name,
			"awnd": self.awnd,
			"snow": self.snow,
			"tavg": self.tavg,
			"tmax": self.tmax,
			"tmin": self.tmin
		}

@app.route("/")
def index():
	return "hi!"

@app.route("/energyovertime")
def energyovertime():
	result = db.engine.execute("SELECT Aggregateusage.facid, Building.latitude, Building.longitude, Aggregateusage.globaluse, Aggregateusage.globalsqftuse, Building.description, Aggregateusage.usagemonth FROM Aggregateusage JOIN Building ON Aggregateusage.facid=Building.building")
	all_buildings = {}
	for thing in result:
		if thing[1] == '[]':
			continue

		thing = {
			'lat':float(thing[1]),
			'lng':float(thing[2]),
			'id':float(thing[0]),
			'usage':[(thing[6], float(thing[3]))],
			'sqftusage':[(thing[6], float(thing[4]))],
			'description':thing[5]
		}

		if thing['id'] in all_buildings:
			minidict = all_buildings[thing['id']]
			minidict['usage'].append(thing['usage'][0])
			minidict['sqftusage'].append(thing['sqftusage'][0])
		else:
			all_buildings[thing['id']] = thing

	all_buildings = list(all_buildings.values())

	counter = 1
	for building in all_buildings:
		building['usage'] = sorted(building['usage'], key=lambda student: student[0])
		building['sqftusage'] = sorted(building['sqftusage'], key=lambda student: student[0])
		building['usage'] = [bleh[1] for bleh in building['usage']]
		building['sqftusage'] = [bleh[1] for bleh in building['sqftusage']]

	for building in all_buildings:
		if len(building['usage']) < 182:
			building['usage'] = [0]*(182-len(building['usage'])) + building['usage']
			building['sqftusage'] = [0]*(182-len(building['sqftusage'])) + building['sqftusage']


	return jsonify(all_buildings)

@app.route("/rcenergy")
def recenergy():
	result = db.engine.execute("SELECT Aggregateusage.facid, Building.latitude, Building.longitude, Aggregateusage.globaluse, Aggregateusage.globalsqftuse, Building.description, Aggregateusage.usagemonth FROM Aggregateusage JOIN Building ON Aggregateusage.facid=Building.building WHERE Aggregateusage.facid IN ('2420', '2510', '1820', '2035', '2500', '2505', '2050', '2100', '2145', '2040', '2425', '1350', '1354', '1800')")
	all_buildings = {}
	for thing in result:
		if thing[1] == '[]':
			continue

		thing = {
			'lat':float(thing[1]),
			'lng':float(thing[2]),
			'id':float(thing[0]),
			'usage':[(thing[6], float(thing[3]))],
			'sqftusage':[(thing[6], float(thing[4]))],
			'description':thing[5]
		}

		if thing['id'] in all_buildings:
			minidict = all_buildings[thing['id']]
			minidict['usage'].append(thing['usage'][0])
			minidict['sqftusage'].append(thing['sqftusage'][0])
		else:
			all_buildings[thing['id']] = thing

	all_buildings = list(all_buildings.values())

	counter = 1
	for building in all_buildings:
		building['usage'] = sorted(building['usage'], key=lambda student: student[0])
		building['sqftusage'] = sorted(building['sqftusage'], key=lambda student: student[0])
		building['usage'] = [bleh[1] for bleh in building['usage']]
		building['sqftusage'] = [bleh[1] for bleh in building['sqftusage']]

	for building in all_buildings:
		if len(building['usage']) < 182:
			building['usage'] = [0]*(182-len(building['usage'])) + building['usage']
			building['sqftusage'] = [0]*(182-len(building['sqftusage'])) + building['sqftusage']


	return jsonify(all_buildings)

@app.route("/students")
def students():
	result = db.engine.execute('SELECT Building.building AS id, Building.latitude AS lat, Building.longitude AS lng, COUNT(Student.student_id) AS count, Building.description FROM Student Join Building ON Student.college=Building.description GROUP BY Building.building')

	results = []
	for thing in result:
		results.append(dict(thing))

	return jsonify(results)

@app.route("/weather")
def weather():
	result = db.engine.execute("SELECT Weather.date, Weather.tavg FROM Weather JOIN Aggregateusage ON weather.date=Aggregateusage.usagemonth WHERE Aggregateusage.facid='2050'")

	results = []
	for thing in result:
		minidict = dict(thing)
		try:
			minidict['tavg'] = float(minidict['tavg'])
		except:
			minidict['tavg'] = 0.0
		results.append(minidict)

	results = sorted(results, key=lambda student: student['date'])

	actual_results = []
	for thing in results:
		actual_results.append(thing['tavg'])

	return jsonify(actual_results)

# def print_dict(s):
# 	print('{')
# 	for line in s.split('\n'):
# 		v = line.lstrip().split(' ')[0]
# 		print('\t"{}": self.{},'.format(v, v))
# 	print('}')

