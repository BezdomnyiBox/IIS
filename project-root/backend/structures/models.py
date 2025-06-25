from config import db
from flask import abort
from models import Region, SubRegion, Country, Export
from structures.serializers import region_cschema, subregion_cschema, country_cschema, export_cschema
from sqlalchemy import func

def get_all_regions ():
    query = Region.query.all()
    return query

def get_all_subregions():
    query = SubRegion.query.all()
    return query

def get_all_countries():
    query = Country.query.all()
    return query

def get_all_exports():
    query = Export.query.all()
    return query

def get_one_region(region_id):
    query = Region.query.filter(Region.id == region_id).one_or_none()
    return query

def get_one_subregion(subregion_id):
    query = SubRegion.query.filter(SubRegion.id == subregion_id).one_or_none()
    return query

def get_one_country(country_id):
    query = Country.query.filter(Country.id == country_id).one_or_none()
    return query

def get_one_export(export_id):
    query = Export.query.filter(Export.id == export_id).one_or_none()
    return query

def insert_region(region):
    item = region_cschema.load(region, session=db.session)
    db.session.add(item)
    db.session.commit()
    return Region.query.\
        filter(Region.id == db.session.query(func.max(Region.id))).\
        one_or_none()
    
def insert_subregion(subregion):
    query = Region.query.filter(Region.id == subregion['region_id']).one_or_none()
    if query is None:
        abort(404)
    item = subregion_cschema.load(subregion, session=db.session)
    db.session.add(item)
    db.session.commit()
    return SubRegion.query.\
        filter(SubRegion.id == db.session.query(func.max(SubRegion.id))).\
        one_or_none()
        
def insert_country(country):    
    query = SubRegion.query.filter(SubRegion.id == country['sub_region_id']).one_or_none()
    if query is None:
        abort(404)
    item = country_cschema.load(country, session=db.session)
    db.session.add(item)
    db.session.commit()
    return Country.query.\
        filter(Country.id == db.session.query(func.max(Country.id))).\
        one_or_none()
        
def insert_export(export):
    query = Country.query.filter(Country.id == export['country_id']).one_or_none()
    if query is None:
        abort(404)
    item = export_cschema.load(export, session=db.session)
    db.session.add(item)
    db.session.commit()
    return Export.query.\
        filter(Export.id == db.session.query(func.max(Export.id))).\
        one_or_none()

def update_region(region_id, update_params):
    existing_region = get_one_region(region_id)
    if existing_region is None or not update_params:
        abort(404)
    if 'name' in update_params:
            existing_region.name = update_params['name']
    db.session.commit()
    return existing_region  

def update_subregion(subregion_id, update_params):
    existing_subregion = get_one_subregion(subregion_id)
    if existing_subregion is None or not update_params:
        abort(404)
    if 'name' in update_params:
        existing_subregion.name = update_params['name']
    if 'region_id' in update_params:
        existing_subregion.region_id = update_params['region_id']
    db.session.commit()
    return existing_subregion

def update_country(country_id, update_params):
    existing_country = get_one_country(country_id)
    if existing_country is None or not update_params:
        abort(404)
    if 'name' in update_params:
        existing_country.name = update_params['name']
    if 'sub_region_id' in update_params:
        existing_country.sub_region_id = update_params['sub_region_id']
    db.session.commit()
    return existing_country 

def update_export(export_id, update_params):
    existing_export = get_one_export(export_id)
    if existing_export is None or not update_params:
        abort(404)
    if 'country_id' in update_params:
        existing_export.country_id = update_params['country_id'] 
    if 'year' in update_params:
        existing_export.year = update_params['year']
    if 'value' in update_params:
        existing_export.value = update_params['value']
    db.session.commit()
    return existing_export  

def delete_region(region_id):
    region = get_one_region(region_id)
    if region is None:
        return False
    db.session.delete(region)
    db.session.commit()
    return True   

def delete_subregion(subregion_id): 
    subregion = get_one_subregion(subregion_id)
    if subregion is None:
        return False
    db.session.delete(subregion)
    db.session.commit()
    return True    

def delete_country(country_id):
    country = get_one_country(country_id)
    if country is None:
        return False
    db.session.delete(country)
    db.session.commit()
    return True  

def delete_export(export_id):
    export = get_one_export(export_id)
    if export is None:
        return False
    db.session.delete(export)
    db.session.commit()
    return True   

def get_region_by_subregion(subregion_id):
    query = Region.query.filter(Region.sub_region_id == subregion_id).all()
    return query

def get_subregion_by_region(region_id):
    query = SubRegion.query.filter(SubRegion.region_id == region_id).all()
    return query

def get_country_by_subregion(subregion_id):
    query = Country.query.filter(Country.sub_region_id == subregion_id).all()
    return query    

def get_export_by_country(country_id):
    query = Export.query.filter(Export.country_id == country_id).all()
    return query

def get_export_by_year(year):
    query = Export.query.filter(Export.year == year).all()
    return query

def get_max_export_by_country(country_id):
    country = Country.query.filter(Country.id == country_id).one_or_none()
    if country is None:
        abort(404)
    query = Export.query.filter(Export.country_id == country_id)\
     .order_by(Export.value.desc())\
     .first()
    return query

def get_min_export_by_country(country_id):
    country = Country.query.filter(Country.id == country_id).one_or_none()
    if country is None:
        abort(404)
    query = Export.query.filter(Export.country_id == country_id)\
     .order_by(Export.value.asc())\
     .first()
    return query

def get_avg_export_by_country(country_id):
    country = Country.query.filter(Country.id == country_id).one_or_none()
    if country is None:
        abort(404)
    query = db.session.query(
        func.avg(Export.value).label('avg_value')
    ).filter(Export.country_id == country_id).scalar()
    return query

def get_max_export_by_year(year):
    query = Export.query.filter(Export.year == year)\
     .order_by(Export.value.desc())\
     .first()
    return query

def get_min_export_by_year(year):
    query = Export.query.filter(Export.year == year)\
     .order_by(Export.value.asc())\
     .first()
    return query

def get_avg_export_by_year(year):
    query = db.session.query(
        func.avg(Export.value).label('avg_value')
    ).filter(Export.year == year).scalar()
    return query

def get_max_export_by_region(region_id):
    region = Region.query.filter(Region.id == region_id).one_or_none()
    if region is None:
        abort(404)
    query = Export.query.join(Country, Export.country_id == Country.id)\
     .join(SubRegion, Country.sub_region_id == SubRegion.id)\
     .join(Region, SubRegion.region_id == Region.id)\
     .filter(Region.id == region_id)\
     .order_by(Export.value.desc())\
     .first()
    return query

def get_min_export_by_region(region_id):
    region = Region.query.filter(Region.id == region_id).one_or_none()
    if region is None:
        abort(404)
    query = Export.query.join(Country, Export.country_id == Country.id)\
     .join(SubRegion, Country.sub_region_id == SubRegion.id)\
     .join(Region, SubRegion.region_id == Region.id)\
     .filter(Region.id == region_id)\
     .order_by(Export.value.asc())\
     .first()
    return query

def get_avg_export_by_region(region_id):
    region = Region.query.filter(Region.id == region_id).one_or_none()
    if region is None:
        abort(404)
    query = db.session.query(
        func.avg(Export.value).label('avg_value')
    ).join(Country, Export.country_id == Country.id)\
     .join(SubRegion, Country.sub_region_id == SubRegion.id)\
     .join(Region, SubRegion.region_id == Region.id)\
     .filter(Region.id == region_id).scalar()
    return query

def get_exports_grouped_by_country():
    results = db.session.query(
        Country.id,
        Country.name,
        func.min(Export.value).label('min_export'),
        func.max(Export.value).label('max_export'),
        func.avg(Export.value).label('avg_export')
    ).join(Export, Country.id == Export.country_id)\
     .group_by(Country.id, Country.name)\
     .all()
    
    return [
        {
            "id": r[0],
            "Группа": r[1],
            "Минимальный экспорт": r[2],
            "Максимальный экспорт": r[3],
            "Средний экспорт": float(r[4]) if r[4] is not None else 0
        } for r in results
    ]

def get_exports_grouped_by_year():
    results = db.session.query(
        Export.year,
        func.min(Export.value).label('min_export'),
        func.max(Export.value).label('max_export'),
        func.avg(Export.value).label('avg_export')
    ).group_by(Export.year)\
     .all()

    return [
        {
            "id": i + 1,
            "Группа": r[0],
            "Минимальный экспорт": r[1],
            "Максимальный экспорт": r[2],
            "Средний экспорт": float(r[3]) if r[3] is not None else 0
        } for i, r in enumerate(results)
    ]

def get_exports_grouped_by_region():
    results = db.session.query(
        Region.id,
        Region.name,
        func.min(Export.value).label('min_export'),
        func.max(Export.value).label('max_export'),
        func.avg(Export.value).label('avg_export')
    ).join(SubRegion, Region.id == SubRegion.region_id)\
     .join(Country, SubRegion.id == Country.sub_region_id)\
     .join(Export, Country.id == Export.country_id)\
     .group_by(Region.id, Region.name)\
     .all()

    return [
        {
            "id": r[0],
            "Группа": r[1],
            "Минимальный экспорт": r[2],
            "Максимальный экспорт": r[3],
            "Средний экспорт": float(r[4]) if r[4] is not None else 0
        } for r in results
    ]









