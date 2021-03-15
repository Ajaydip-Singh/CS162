from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Numeric 
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:', echo=True)

engine.connect()

base = declarative_base()

class Clients(base):

    __tablename__ = "clients"

    client_number = Column(Integer, primary_key=True)
    first_name = Column(String)
    surname = Column(String)
    email = Column(String)
    phone = Column(String)

    def __repr__(self):
        return f"Clients(client_number={self.client_number}, \
                         first_name={self.first_name}, \
                         surname={self.surname}, \
                         email={self.email}, \
                         phone={self.phone})"   

class Loans(base):

    __tablename__ = "loans"
    
    id = Column(Integer, primary_key=True)
    account_number = Column(Integer)
    client_number = Column(Integer, ForeignKey('clients.client_number'))
    start_date = Column(DateTime)
    start_month = Column(Integer)
    term = Column(Integer)
    remaining_term = Column(Integer)
    principal_debt = Column(Numeric(11, 2))
    account_limit = Column(Numeric(11, 2))
    balance = Column(Numeric(11, 2))
    status = Column(String)

    user = relationship(Clients)

base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

user1 = Clients(client_number=1, 
                first_name='Robert',
                surname='Warren',
                email='RobertDWarren@teleworm.us',
                phone='(251) 546-9442')
            
session.add(user1)

our_user = session.query(Clients).filter_by(first_name='Robert').first()


user2 = Clients(client_number=2,
                first_name='Adam',
                surname='Justin',
                email='justin@teleworm.us',
                phone='(251) 546-9442')

session.add(user2)
user2.first_name = 'Ajay'
session.commit()

our_user = session.query(Clients).filter_by(first_name='Ajay').first()
print(our_user)
