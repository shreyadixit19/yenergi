from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import usage_load_template
from flask.ext.heroku import Heroku

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
heroku = Heroku(app)
db = SQLAlchemy(app)

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
	site = db.Column(db.String(255))
	building = db.Column(db.Integer, primary_key=True)
	building_abbr = db.Column(db.String(255))
	description = db.Column(db.String(1000))
	usage_description = db.Column(db.String(255))
	address_1 = db.Column(db.String(255))
	address_2 = db.Column(db.String(255))
	address_3 = db.Column(db.String(255))
	status = db.Column(db.String(255))
	historical_alias = db.Column(db.String(255))
	addr1_alias = db.Column(db.String(255))
	msag_alias = db.Column(db.String(255))
	latitude = db.Column(db.String(255))
	longitude = db.Column(db.String(255))
	historical_name = db.Column(db.String(255))
	building_prose = db.Column(db.String(255))

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
			"building_prose": self.building_prose,
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
	#usage_load_template.load(db, Usage)
	#return jsonify(Building.query.all()[0].serialize())
	return jsonify(Usage.query.all()[0].serialize())

#def print_dict(s):
#	print '{'
#	for line in s.split('\n'):
#		v = line.lstrip().split(' ')[0]
#		print '\t"{}": self.{},'.format(v, v)
#	print '}'
