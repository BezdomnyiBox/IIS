from config import db
from models import Country, City, Building, TypeBuilding


def get_all_buildings():
    query = (
        db.session.query(
            Building.title.label("Здание"),
            TypeBuilding.name.label("Тип"),
            Country.name.label("Страна"),
            City.name.label("Город"),
            Building.year.label("Год"),
            Building.height.label("Высота"),
        )
        .select_from(Building)
        .join(TypeBuilding)
        .join(City)
        .join(Country)
    )
    return [query.statement.columns.keys(), query.all()]


def get_building_stats_by_type():
    query = (
        db.session.query(
            TypeBuilding.name.label("Тип"),
            db.func.max(Building.height).label("Максимальная высота"),
            db.func.min(Building.height).label("Минимальная высота"),
            db.func.avg(Building.height).label("Средняя высота"),
        )
        .select_from(Building)
        .join(TypeBuilding)
        .group_by(TypeBuilding.name)
    )
    return [query.statement.columns.keys(), query.all()]


def get_building_stats_by_country():
    query = (
        db.session.query(
            Country.name.label("Страна"),
            db.func.max(Building.height).label("Максимальная высота"),
            db.func.min(Building.height).label("Минимальная высота"),
            db.func.avg(Building.height).label("Средняя высота"),
        )
        .select_from(Building)
        .join(City)
        .join(Country)
        .group_by(Country.name)
    )
    return [query.statement.columns.keys(), query.all()]


def get_building_stats_by_year():
    query = (
        db.session.query(
            Building.year.label("Год"),
            db.func.max(Building.height).label("Максимальная высота"),
            db.func.min(Building.height).label("Минимальная высота"),
            db.func.avg(Building.height).label("Средняя высота"),
        )
        .select_from(Building)
        .group_by(Building.year)
    )
    return [query.statement.columns.keys(), query.all()]


def get_buildings_by_year_range(start_year, end_year):
    query = (
        db.session.query(
            Building.title.label("Здание"),
            TypeBuilding.name.label("Тип"),
            Country.name.label("Страна"),
            City.name.label("Город"),
            Building.year.label("Год"),
            Building.height.label("Высота"),
        )
        .select_from(Building)
        .join(TypeBuilding)
        .join(City)
        .join(Country)
        .filter(Building.year >= start_year, Building.year <= end_year)
    )
    return [query.statement.columns.keys(), query.all()]
