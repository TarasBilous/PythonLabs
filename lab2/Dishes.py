from app import db


class Dishes(db.Model):
    __tablename__ = "dishes"
    dishes_id = db.Column('id', db.Integer, primary_key=True)
    dishes_price = db.Column('price', db.Integer)
    dishes_material = db.Column('material', db.String(20))
    dishes_color = db.Column('color', db.String(20))

    def __str__(self):
        return str("dishes id: " + str(self.dishes_id) + "\ndishes price: " + str(self.dishes_price) + "\ndishes material: " + str(self.dishes_material)
                   + "\ndishes color: " + str(self.dishes_color))
