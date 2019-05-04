#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

# SQLite
# 練習 インメモリ
# engine = sqlalchemy.create_engine('sqlite:///:memory:')
# engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)
# 実体での実行
# engine = sqlalchemy.create_engine('sqlite:///test_sqlite', echo=True)

# MySQL (先にDBが必要)
engine = sqlalchemy.create_engine(
    'mysql+pymysql://root:OWN_PASSWORD@localhost/test_mysql_database2',
    echo=True)


Base = sqlalchemy.ext.declarative.declarative_base()


class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(14))


Base.metadata.create_all(engine)
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

# Insert
p1 = Person(name='Mike')
session.add(p1)
p2 = Person(name='Nancy')
session.add(p2)
p3 = Person(name='Jun')
session.add(p3)
session.commit()

# Update
p4 = session.query(Person).filter_by(name='Mike').first()
p4.name = 'Michel'
session.add(p4)
session.commit()

# Delete
p5 = session.query(Person).filter_by(name='Michel').first()
session.delete(p5)
session.commit()

# Standard View
persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)

