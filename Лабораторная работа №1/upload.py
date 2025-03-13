import csv
from config import db
from models import Country, City, Building

def country_upload():
	with open("./data/country.csv") as f:
		reader = csv.reader(f)
		next(reader)
		for item in reader:
			new_entry = Country(item[0])
			db.session.add(new_entry)
	db.session.commit()

def city_upload():
	with open("./data/city.csv") as f:
		reader = csv.reader(f)
		next(reader)
		for item in reader:
			new_entry = City(item[0],item[1])
			db.session.add(new_entry)
	db.session.commit()
 
def building_upload():
	with open("./data/building.csv") as f:
		reader = csv.reader(f)
		next(reader)
		for item in reader:
			new_entry = Building(item[0],item[1],item[2],item[3],item[4])
			db.session.add(new_entry)
	db.session.commit()
 
 
# country_upload()
# city_upload()
# building_upload()