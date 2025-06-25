from config import db
from models import Region, SubRegion, Country, Export


# 1. Выбрать все страны в регионе
def get_countries_in_region(region_name):
    query = (
        db.session.query(
            Country.name.label("Страна"),
            Region.name.label("Регион"),
            SubRegion.name.label("Субрегион"),
        )
        .select_from(Region)
        .join(SubRegion, Region.id == SubRegion.region_id)
        .join(Country, SubRegion.id == Country.sub_region_id)
        .filter(Region.name == region_name)
    )
    return [query.statement.columns.keys(), query.all()]


# 2. Получить экспорт по стране
def get_exports_for_country(country_name):
    query = (
        db.session.query(Export.year.label("Год"), Export.value.label("Значение"))
        .select_from(Country)
        .join(Export, Country.id == Export.country_id)
        .filter(Country.name == country_name)
    )
    return [query.statement.columns.keys(), query.all()]


# 3. Получить страны лидеры по экспорту на каждый год через GROUP BY
def get_top_exporting_countries_per_year():
    subquery = (
        db.session.query(
            Export.year.label("year"),
            db.func.max(Export.value).label("max_value")
        )
        .group_by(Export.year)
        .subquery()
    )

    query = (
        db.session.query(
            Export.year.label("Год"),
            Country.name.label("Страна"),
            Export.value.label("Значение")
        )
        .join(Country, Export.country_id == Country.id)
        .join(subquery, (Export.year == subquery.c.year) & (Export.value == subquery.c.max_value))
        .order_by(Export.year)
    )
    return [query.statement.columns.keys(), query.all()]


# 4. Получить топ 20 стран с самым низким ненулевым уровнем экспорта
def get_bottom_20_exporting_countries():
    query = (
        db.session.query(
            Country.name.label("Страна"),
            db.func.sum(Export.value).label("Общий экспорт"),
        )
        .join(Export, Country.id == Export.country_id)
        .group_by(Country.name)
        .having(db.func.sum(Export.value) > 0)
        .order_by(db.func.sum(Export.value))
        .limit(20)
    )
    return [query.statement.columns.keys(), query.all()]


# 5. Получить топ 20 стран с самым высоким уровнем экспорта
def get_top_20_exporting_countries():
    query = (
        db.session.query(
            Country.name.label("Страна"),
            db.func.sum(Export.value).label("Общий экспорт"),
        )
        .join(Export, Country.id == Export.country_id)
        .group_by(Country.name)
        .order_by(db.func.sum(Export.value).desc())
        .limit(20)
    )
    return [query.statement.columns.keys(), query.all()]
