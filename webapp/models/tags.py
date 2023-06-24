from db import db


class Tag(db.Model):
    __tablename__ = 'tags'  # noqa

    uuid = db.Column(db.UUID(as_uuid=True), primary_key=True, autoincrement=True)
    tag = db.Column(db.String, index=True, nullable=False)

    def __repr__(self):
        return f'{self.tag}'
