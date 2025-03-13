from config import db
from models import TypeBuilding, Country, City, Building

# Create

# item = TypeBuilding('Небоскрёб')
# db.session.add(item)

# items = ['Антенная мачта', 'Бетонная башня', 'Радиомачта', 'Гиперболоидная башня',
# 'Дымовая труба', 'Решётчатая мачта', 'Башня', 'Мост']

# for item in items:
#     item = TypeBuilding(item)
#     db.session.add(item)

# db.session.commit()


# Read

# query = TypeBuilding.query.all()
# query = TypeBuilding.query.filter(TypeBuilding.id == 5).all()
# query = TypeBuilding.query.filter(TypeBuilding.name.like("%мачта%")).all()
# query = (TypeBuilding.query.filter(TypeBuilding.name.like("%мачта%"))
#          .order_by(TypeBuilding.name.desc()).all())
# query = TypeBuilding.query.filter(TypeBuilding.name.like("%е%"), TypeBuilding.id > 3).all()

# query = Country.query.all()
# query = City.query.all()
# query = Building.query.all()
# print(query)


# Update

# (
#     TypeBuilding.query.filter(TypeBuilding.name == "Мост").update(
#         {TypeBuilding.name: "Мосты"}
#     )
# )
# db.session.commit()
# query = TypeBuilding.query.all()
# print(query)


# Delete

# TypeBuilding.query.filter(TypeBuilding.id == 9).delete()

# db.session.commit()
# query = TypeBuilding.query.all()
# print(query)
