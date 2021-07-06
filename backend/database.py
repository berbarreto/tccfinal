import sqlalchemy

from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

import json

from helper import to_json

Base = declarative_base()


def engine():
    # if os.environ['DB'] == "PGS":
    return sqlalchemy.create_engine('postgresql://postgres:postgres@localhost:5432/tcc')
    # else:
    # return sqlalchemy.create_engine("mariadb+mariadbconnector://root@127.0.0.1:3306/tcc")


def new_session():
    session = sqlalchemy.orm.sessionmaker()
    session.configure(bind=engine())
    return session()


def migrate():
    Base.metadata.create_all(engine())


class User(Base):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=100))
    cpf = sqlalchemy.Column(sqlalchemy.String(length=30))
    email = sqlalchemy.Column(sqlalchemy.String(length=50))
    phone = sqlalchemy.Column(sqlalchemy.String(length=30))
    birth_date = sqlalchemy.Column(sqlalchemy.String(length=20))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'cpf': self.cpf,
            'email': self.email,
            'phone': self.phone,
            'birth_date': self.birth_date,
        }
    #
    # def __repr__(self):
    #     return json.dumps(self.serialize)


class Doctor(Base):
    __tablename__ = 'doctors'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=100))
    crm = sqlalchemy.Column(sqlalchemy.String(length=30))
    phone = sqlalchemy.Column(sqlalchemy.String(length=30))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'crm': self.crm,
            'phone': self.phone,
        }


class Analyze(Base):
    __tablename__ = 'analysis'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    result_id = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey('results.id'))
    type = sqlalchemy.Column(sqlalchemy.String(length=500))
    image = sqlalchemy.Column(sqlalchemy.String())

    # result = relationship(Result, back_populates='results')

    # analysis_id = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey('analysis.id'))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'type': self.type,
            'image': self.image
            # 'result_id': self.result_id,
        }

    # def __repr__(self):
    #     return json.dumps(self.serialize)


class Result(Base):
    __tablename__ = 'results'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey('users.id'))
    doctor_id = sqlalchemy.Column(sqlalchemy.Integer, ForeignKey('doctors.id'))

    image = sqlalchemy.Column(sqlalchemy.String)
    diameter = sqlalchemy.Column(sqlalchemy.String)
    symmetry = sqlalchemy.Column(sqlalchemy.String)
    ai_detection = sqlalchemy.Column(sqlalchemy.String)

    feedback = sqlalchemy.Column(sqlalchemy.String(length=500))
    tag = sqlalchemy.Column(sqlalchemy.String(length=500))

    user = relationship(User, backref='user')
    analysis = relationship(Analyze, backref='analysis', lazy='joined')

    @property
    def serialize(self):
        return {
            'id': self.id,
            'created_at': self.created_at.strftime("%b %d %Y %H:%M:%S"),
            'image': self.image,
            'diameter': self.diameter,
            'symmetry': self.symmetry,
            'ai_detection': self.ai_detection,
            'analysis': to_json(self.analysis),
            'feedback': self.feedback,
            'tag': self.tag,
            'user': self.user.serialize,
        }
