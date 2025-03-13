from config import db
from models import Country, City, Building, TypeBuilding
from sqlalchemy import func


def get_countries():
    return db.session.query(Country).all()


def get_cities():
    return db.session.query(City).all()


def get_buildings():
    return (
        db.session.query(
            Building.title.label("Здание"),
            Building.year.label("Год"),
            Building.height.label("Высота"),
        )
        .filter(Building.height > 640)
        .all()
    )


def get_buildings_2():
    return (
        db.session.query(
            Building.title.label("Здание"),
            Building.year.label("Год"),
            Building.height.label("Высота"),
        )
        .filter((Building.height < 355) | (Building.height > 800))
        .all()
    )


def get_buildings_3():
    return (
        db.session.query(
            Building.title.label("Здание"),
            Building.year.label("Год"),
            Building.height.label("Высота"),
        )
        .filter(~(Building.height < 640))
        .all()
    )


def get_buildings_4():
    return (
        db.session.query(
            Building.title.label("Здание"),
            Building.year.label("Год"),
            Building.height.label("Высота"),
        )
        .filter(Building.title.contains("башня"))
        .all()
    )


def get_buildings_5():
    return (
        db.session.query(
            Building.title.label("Здание"),
            Building.year.label("Год"),
            Building.height.label("Высота"),
        )
        .filter(Building.title.like("%башня"))
        .all()
    )


def get_buildings_6():
    return (
        db.session.query(
            Building.title.label("Здание"),
            Building.year.label("Год"),
            Building.height.label("Высота"),
        )
        .order_by("Год", Building.height.desc())
        .all()
    )


def get_types_buildings():
    return db.session.query(TypeBuilding).all()


def get_city_name_and_country():
    return db.session.query(
        City.name.label("Город"), City.country_id.label("Страна")
    ).all()


def get_city_join_country():
    return (
        db.session.query(
            Country.name.label("Страна"),
            City.name.label("Город"),
        )
        .join(Country)
        .all()
    )


def get_buildings_join_city_and_country():
    return (
        db.session.query(
            Building.title.label("Здание"),
            Country.name.label("Страна"),
            City.name.label("Город"),
            Building.year.label("Год"),
            Building.height.label("Высота"),
        )
        .select_from(Building)
        .join(City)
        .join(Country)
        .all()
    )


def get_buildings_7():
    return (
        db.session.query(
            TypeBuilding.name.label("Тип"),
            func.count(Building.height).label("Количество"),
            func.max(Building.height).label("Максимальная высота"),
            func.min(Building.height).label("Минимальная высота"),
            func.round(func.avg(Building.height), 1).label("Средняя высота"),
        )
        .join(TypeBuilding)
        .group_by(TypeBuilding.name)
        .all()
    )
# print(get_buildings_7())

# Самостоятельное задание
# 1. Вывести информацию о каждом здании: название, тип, страна, город, год, высота.
# Информацию отсортировать по убыванию высоты.

def get_buildings_info():
    return (
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
        .order_by(Building.height.desc())
        .all()
    )

# 2. Посчитать максимальную, минимальную и среднюю высоту зданий в каждой стране,
# информацию отсортировать по названию страны.

def get_building_heights_by_country():
    return (
        db.session.query(
            Country.name.label("Страна"),
            func.max(Building.height).label("Максимальная высота"),
            func.min(Building.height).label("Минимальная высота"),
            func.round(func.avg(Building.height), 1).label("Средняя высота"),
        )
        .join(Country)
        .group_by(Country.name)
        .order_by(Country.name)
        .all()
    )

# 3. Посчитать максимальную, минимальную и среднюю высоту зданий по каждому
# году, информацию отсортировать по возрастанию года.
def get_building_heights_by_year():
    return (
        db.session.query(
            Building.year.label("Год"),
            func.max(Building.height).label("Максимальная высота"),
            func.min(Building.height).label("Минимальная высота"),
            func.round(func.avg(Building.height), 1).label("Средняя высота"),
        )
        .group_by(Building.year)
        .order_by(Building.year)
        .all()
    )
# 4. Посчитать максимальную, минимальную и среднюю высоту зданий только для тех
# типов зданий, название которых содержит слово «мачта». Информацию отсортировать по
# убыванию средней высоты.
def get_building_heights_for_mast_types():
    return (
        db.session.query(
            TypeBuilding.name.label("Тип"),
            func.max(Building.height).label("Максимальная высота"),
            func.min(Building.height).label("Минимальная высота"),
            func.round(func.avg(Building.height), 1).label("Средняя высота"),
        )
        .join(TypeBuilding)
        .filter(TypeBuilding.name.contains("мачта"))
        .group_by(TypeBuilding.name)
        .order_by(func.round(func.avg(Building.height), 1).desc())
        .all()
    )
# 5. Посчитать максимальную, минимальную и среднюю высоту зданий для тех стран, в
# которых построено больше одного здания (самостоятельно найти соответствующий метод).
def get_building_heights_for_countries_with_multiple_buildings():
    subquery = (
        db.session.query(
            Building.country_id,
            func.count(Building.id).label("building_count")
        )
        .group_by(Building.country_id)
        .having(func.count(Building.id) > 1)
        .subquery()
    )

    return (
        db.session.query(
            Country.name.label("Страна"),
            func.max(Building.height).label("Максимальная высота"),
            func.min(Building.height).label("Минимальная высота"),
            func.round(func.avg(Building.height), 1).label("Средняя высота"),
        )
        .join(Building, Building.country_id == Country.id)
        .join(subquery, subquery.c.country_id == Country.id)
        .group_by(Country.name)
        .order_by(Country.name)
        .all()
    )
