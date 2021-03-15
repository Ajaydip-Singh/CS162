from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Text, Numeric, DateTime
from sqlalchemy.orm import relationship 
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///:memory:', echo=True)

engine.connect()

base = declarative_base()

class Product(base):

    __tablename__ = "product"

    product_id = Column(Integer, primary_key=True)
    title = Column(Text)
    description = Column(Text)
    price = Column(Numeric(11,2))
    cost = Column(Numeric(11,2))

class Orders(base):

    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True),
    customer_id = Column(Integer, ForeignKey('customer.customer_id'))
    date_ordered = Column(DateTime)
    month_ordered = Column(Integer)

    customer = relationship(Customer)

class OrderItems(base): 

    __tablename__ = "orderitems"

    order_id = Column(Integer, ForeignKey('orders.order_id'))
    product_id = Column(Integer, ForeignKey('product.product_id'))
    quantity = Column(Integer)

    orders = relationship(Orders)
    product = relationship(Product)


class Warehouse(base): 

     __tablename__ = "warehouse"

    warehouse_id = Column(Integer, primary_key=True)

    name = Column(Text)
    address_line_1 = Column(Text)
    address_line_2 = Column(Text)
    address_line_2 = Column(Text)

class Inventory(base):

    __tablename__ = "inventory"

    warehouse_id = Column(Integer, ForeignKey('warehouse.warehouse_id'))
    product_id = Column(Integer, ForeignKey('product.product_id'))
    quantity = Column(Integer)

    warehouse = relationship(Warehouse)
    product = relationship(Product)


class Supplier(base): 

    __tablename__ = "supplier"

    supplier_id = Column(Integer, primary_key=True)
    name = Column(Text)
    address_line_1 = Column(Text)
    address_line_2 = Column(Text)
    address_line_3 = Column(Text)
    phone_numer = Column(Text)
    email = Column(Text)

class SupplierProduct(base):

    __tablename__ = "supplierproduct"

    supplier_id = Column(Integer, ForeignKey('supplier_supplier_id'))
    product_id = Column(Integer, ForeignKey('product.product_id'))
    days_lead_time = Column(Integer)
    cost = Column(Numeric(11,2))

    supplier = relationship(Supplier)
    product = relationship(Product)


class SupplierOrders(base):

    __tablename__ = "supplierorders"

    supplier_order_id = Column(Integer, primary_key=True)
    supplier_id = Column(Integer, ForeignKey('supplier.supplier_id'))
    product_id = Column(Integer, ForeignKey('product.product_id'))
    warehouse_id = Column(Integer, ForeignKey('warehouse.warehouse_id'))
    quantity = Column(Integer)
    status = Column(Text)
    date_ordered = Column(DateTime)
    date_dure = Column(DateTime)

    supplier = relationship(Supplier)
    product = relationship(Product)
    warehouse = relationship(Warehouse)

class Customer(base):

    __tablename__ = "customer"

    customer_id = Column(Integer, primary_key=True)
    first_name = Column(Text)
    surname = Column(Text)
    address_line_1 = Column(Text)
    address_line_2 = Column(Text)
    address_line_3 = Column(Text)
    phone_numer = Column(Text)
    email = Column(Text)
