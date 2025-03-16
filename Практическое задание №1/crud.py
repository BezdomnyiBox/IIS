from models import Region, SubRegion, Country, Export
from config import db

# # Create
# item = Region('Евразия')
# db.session.add(item)
# db.session.commit()

# # Read
# query = Region.query.all()
# print(query)
# query = Region.query.filter(Region.id == 5).all()
# print(query)
# query = Region.query.filter(Region.name.like("%Азия%")).order_by(Region.name.desc()).all()
# print(query)

# # Update
# Region.query.filter(Region.name == 'Мост').update({Region.name: "Мосты"})        
# db.session.commit()
# query = Region.query.all()
# print(query)

# Delete
# Export.query.delete()
# db.session.commit()
# query = Export.query.all()

# Country.query.delete()
# db.session.commit()
# query = Country.query.all()

# SubRegion.query.delete()
# db.session.commit()
# query = SubRegion.query.all()

# Region.query.delete()
# db.session.commit()
# query = Region.query.all()

# print(query)