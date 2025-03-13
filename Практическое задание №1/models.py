from config import db 

class Region(db.Model):
    __tablename__ = 'region' # задавать необязательно
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('Регион', db.String(255), nullable=False)
    sub_regions = db.relationship("SubRegion")
    
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f'\nid: {self.id}, Регион: {self.name}'    
    
        
class SubRegion(db.Model):
    __tablename__ = 'sub_region' # задавать необязательно
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('Субрегион', db.String(255), nullable=False)
    region_id = db.Column(db.Integer, db.ForeignKey('region.id'))
    region = db.relationship("Region", back_populates="sub_regions")
    countries = db.relationship("Country")
    
    def __init__(self, name, region_id):
        self.name = name
        self.region_id = region_id

class Country(db.Model):
    __tablename__ = 'country' # задавать необязательно
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('Страна', db.String(255), nullable=False)
    sub_region_id = db.Column(db.Integer, db.ForeignKey('sub_region.id'))
    sub_region = db.relationship("SubRegion", back_populates="countries")
    exports = db.relationship("Export")
    
    def __init__(self, name, sub_region_id):
        self.name = name
        self.sub_region_id = sub_region_id

class Export(db.Model):
    __tablename__ = 'export' # задавать необязательно
    id = db.Column(db.Integer, primary_key=True) 
    year = db.Column('Год', db.Date(), nullable=False)
    value = db.Column('Значение', db.Float(), nullable=False)    
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    country = db.relationship("Country", back_populates="exports")
    
    def __init__(self, year, value, country_id):
        self.year = year
        self.value = value
        self.country_id = country_id  
            
app.app_context().push()

with app.app_context():
    db.create_all()