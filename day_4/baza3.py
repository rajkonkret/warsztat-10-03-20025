# sqlalchemy - system orm do pracy z bazą danych w sposób obiektowy
# pip install sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# engine = create_engine('sqlite:///:memory:')
engine = create_engine('sqlite:///moja_baza.db', echo=True)
Base = declarative_base()


# encje - klasy odwzorowujące tabele w bazie danch
class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(String)


Base.metadata.create_all(engine)  # tworzenie struktury bazy danych
Session = sessionmaker(bind=engine)
session = Session()

person = Person(name="Radek", age="23")
session.add(person)  # INSERT INTO person (name, age) VALUES (?, ?)
session.commit()

persons = session.query(Person).all()
print(persons)  # SELECT person.id AS person_id, person.name AS person_name, person.age AS person_age
# FROM person

for p in persons:
    print(p.name)
