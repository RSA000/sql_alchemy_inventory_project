from sqlalchemy import (create_engine, Column, Integer, String, Date)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///inventory.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

class Inventory(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True)
    product_name = Column(String)
    product_quantity = Column(Integer)
    product_price = Column(Integer)
    date_updated = Column(Date)

    def __repr__(self):
        return f"""\rProduct ID: {self.product_id}\n \rProduct Name: {self.product_name},
                 \rProduct Quantity: {self.product_quantity},\n \rPrice: {'$'+str(self.product_price/100)},
                  \rDate_updated: {self.date_updated}"""

    def return_list(self):
        return [self.product_id, self.product_name,
                 '$' + str(float(self.product_price/100)), self.product_quantity, str(self.date_updated).replace('-', '/')]

    def __gt__(self, other):
        if self.date_updated > other.date_updated:
            return True
        else:
            return False 