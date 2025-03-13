from config import db
from models import Region

# Create
item = Region('Евразия')
db.session.add(item)
db.session.commit()

# Read
query = Region.query.all()
print(query)
query = Region.query.filter(Region.id == 5).all()
print(query)
query = Region.query.filter(Region.name.like("%Азия%")).order_by(Region.name.desc()).all()
print(query)

# Update
Region.query.filter(Region.name == 'Мост').update({Region.name: "Мосты"})        
db.session.commit()
query = Region.query.all()
print(query)

# Delete
Region.query.filter(Region.id == 9).delete()
db.session.commit()
query = Region.query.all()
print(query)