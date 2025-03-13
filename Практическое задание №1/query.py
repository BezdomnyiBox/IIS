from config import db
from models import Region, SubRegion, Country, Export

def get_regions():
    return db.session.query(Region).all()

def get_subregions():
    return db.session.query(SubRegion).all()

def get_countries():
    return db.session.query(Country).all()

def get_exports():
    return db.session.query(Export).all()

def get_region_names():
    result = db.session.query(
        Region.name.label("Регион"), 
    ).all()
    return result

def get_sub_region_names():
    result = db.session.query(
        SubRegion.name.label("Субрегион"), 
    ).all()
    return result

def get_country_names():
    result = db.session.query(
        Country.name.label("Страна"), 
    ).all()
    return result

def get_export_from_year(year):
    result = db.session.query(Export).filter(Export.year == year).all()
    return result

def get_export_value_in(value_1, value_2):
    result = db.session.query(Export).filter(Export.value > value_1, Export.value < value_2).all()
    return result

def get_export_order_by_year():
    result = db.session.query(Export).order_by(Export.year.desc()).all()
    return result

def get_export_with_country():
    result = db.session.query(
        Export.value.label("Уровень экспорта"),
        Export.year.label("Год"),
        Country.name.label("Страна")
    ).join(Country).all()
    return result


