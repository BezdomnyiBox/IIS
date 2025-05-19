from models import Region, SubRegion, Country, Export
from config import ma, db

class RegionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Region
        load_instance = True
        sqla_session = db.session
        
class SubRegionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = SubRegion
        load_instance = True
        sqla_session = db.session
    region = ma.Nested(RegionSchema())
    region_id = ma.auto_field()

class CountrySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Country
        load_instance = True
        sqla_session = db.session
    sub_region = ma.Nested(SubRegionSchema())
    sub_region_id = ma.auto_field()

class ExportSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Export
        load_instance = True
        sqla_session = db.session
    country = ma.Nested(CountrySchema())
    country_id = ma.auto_field()
    
    

region_cschema = RegionSchema()
regions_cschema = RegionSchema(many=True)

subregion_cschema = SubRegionSchema()
subregions_cschema = SubRegionSchema(many=True)

country_cschema = CountrySchema()
countries_cschema = CountrySchema(many=True)

export_cschema = ExportSchema()
exports_cschema = ExportSchema(many=True)




