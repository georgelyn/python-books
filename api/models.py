from config import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    author = db.Column(db.String(120))
    cover = db.Column(db.String(500))

    def __repr__(self):
        return {f"[{self.id}] - {self.title} by {self.author}"}