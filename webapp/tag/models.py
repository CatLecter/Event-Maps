from db import db


class Tag(db.Model):
    __tablename__ = 'tag'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag = db.Column(db.String, index=True, nullable=False)

    def __repr__(self):
        return f'{self.tag}'
