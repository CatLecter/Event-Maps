from webapp.db import db


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag = db.Column(db.String)

    def __repr__(self):
        return f"<Tag: {self.tag} id={self.id}>"
