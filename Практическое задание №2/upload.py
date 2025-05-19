import csv
from config import db
from models import Region, SubRegion, Country, Export


def country_upload():
    with open("./data/export_goods_services_countries_dataset.csv") as f:
        reader = csv.reader(f)
        next(reader)
        for item in reader:
            if (
                not db.session.query(Country).filter_by(name=item[1]).first()
                and item[1] != ""
            ):
                if item[3] != "":
                    sub_region = (
                        db.session.query(SubRegion).filter_by(name=item[3]).first()
                    )
                    if sub_region:
                        sub_region_id = sub_region.id
                    else:
                        sub_region_id = None
                else:
                    sub_region_id = None
                new_entry = Country(item[1], sub_region_id)
                db.session.add(new_entry)
    db.session.commit()


def sub_region_upload():
    with open("./data/export_goods_services_countries_dataset.csv") as f:
        reader = csv.reader(f)
        next(reader)
        for item in reader:
            if (
                not db.session.query(SubRegion).filter_by(name=item[3]).first()
                and item[3] != ""
            ):
                if item[2] != "":
                    region = db.session.query(Region).filter_by(name=item[2]).first()
                    if region:
                        region_id = region.id
                    else:
                        region_id = None
                else:
                    region_id = None
                new_entry = SubRegion(item[3], region_id)
                db.session.add(new_entry)
    db.session.commit()


def region_upload():
    with open("./data/export_goods_services_countries_dataset.csv") as f:
        reader = csv.reader(f)
        next(reader)
        for item in reader:
            if (
                not db.session.query(Region).filter_by(name=item[2]).first()
                and item[2] != ""
            ):
                new_entry = Region(item[2])
                db.session.add(new_entry)
    db.session.commit()


def export_upload():
    with open("./data/export_goods_services_countries_dataset.csv") as f:
        reader = csv.reader(f)
        next(reader)
        for item in reader:
            country = db.session.query(Country).filter_by(name=item[1]).first()
            if country:
                country_id = country.id
            else:
                country_id = None
            new_entry = Export(item[7], item[8], country_id)
            db.session.add(new_entry)
    db.session.commit()


def update_raw_data():
    Region.query.filter(Region.id == 1).update({Region.name: "ЮЖНАЯ АЗИЯ"})
    Region.query.filter(Region.id == 2).update({Region.name: "ЕВРОПА И ЦЕНТРАЛЬНАЯ АЗИЯ"})
    Region.query.filter(Region.id == 3).update({Region.name: "АФРИКА К ЮГУ ОТ САХАРЫ"})
    Region.query.filter(Region.id == 4).update({Region.name: "БЛИЖНИЙ ВОСТОК И СЕВЕРНАЯ АФРИКА"})	
    Region.query.filter(Region.id == 5).update({Region.name: "ЛАТИНСКАЯ АМЕРИКА И КАРИБСКИЙ БАССЕЙН"})
    Region.query.filter(Region.id == 6).update({Region.name: "ВОСТОЧНАЯ АЗИЯ И ТИХООКЕАНСКИЙ РЕГИОН"})
    db.session.commit()
    
    query = Region.query.all()
    print(query)


# region_upload()
# sub_region_upload()
# country_upload()
# export_upload()
# update_raw_data()
