from config import db
from flask import abort
from models import Country, City, Building, TypeBuilding
from structures.serializers import building_cschema
from sqlalchemy import func

def get_all_buildings():
    query = Building.query.all()
    return query


def get_building(building_id):
    query = Building.query.filter(Building.id == building_id).one_or_none()
    return query

def insert_building(building):
    item = building_cschema.load(building, session=db.session)
    db.session.add(item)
    db.session.commit()
    # возвращаем вставленную запись, то есть запись с максимальным id
    return Building.query.\
        filter(Building.id == db.session.query(func.max(Building.id))).\
        one_or_none()

def update_building(building_id, update_params):
    building = get_building(building_id)
    if building is None or not update_params:
        abort(404)
    if 'title' in update_params:
        building.title = update_params['title'] 
    if 'type_building_id' in update_params:
        building.type_building_id = update_params['type_building_id']
    if 'city_id' in update_params:
        building.city_id = update_params['city_id']
    if 'year' in update_params:
        building.year = update_params['year']
    if 'height' in update_params:
        building.height = update_params['height']
    db.session.commit()
    return building

def delete_building(building_id):
    building = get_building(building_id)
    if building is None:
        return False
    db.session.delete(building)
    db.session.commit()
    return True

