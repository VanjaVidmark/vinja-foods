from app import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    description = db.Column(db.Text, nullable=True)
    img_url = db.Column(db.String(200), nullable=True)

    def to_json(self):
        return {
            "id":self.id, 
            "name":self.name, 
            "description":self.description, 
            "imgUrl":self.img_url
        }
