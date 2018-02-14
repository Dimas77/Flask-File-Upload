from app import app, db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(500))
    name = db.Column(db.String(64))
    
    def __repr__(self):
        return self.username

