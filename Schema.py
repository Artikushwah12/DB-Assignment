from sqlalchemy import Column, String, Integer, Boolean, DECIMAL, ForeignKey, VARCHAR, TIMESTAMP
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Product(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(VARCHAR)
    desc = Column(String)
    SKU = Column(VARCHAR)
    price = Column(DECIMAL)
    category_id = Column(Integer, ForeignKey('product_category.id'))  # Foreign key to product_category.id
    inventory_id = Column(Integer, ForeignKey('product_inventory.id'))  # Foreign key to product_inventory.id
    discount_id = Column(Integer, ForeignKey('discount.id'))  # Foreign key to discount.id
    created_at = Column(TIMESTAMP)
    modified_at = Column(TIMESTAMP)
    deleted_at = Column(TIMESTAMP)

    # Relationships
    category = relationship("ProductCategory", foreign_keys=[category_id])
    inventory = relationship("ProductInventory", foreign_keys=[inventory_id])
    discount = relationship("Discount", foreign_keys=[discount_id])


class ProductCategory(Base):
    __tablename__ = 'product_category'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(VARCHAR)
    desc = Column(String)
    created_at = Column(TIMESTAMP)
    modified_at = Column(TIMESTAMP)
    deleted_at = Column(TIMESTAMP)


class ProductInventory(Base):
    __tablename__ = 'product_inventory'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    quantity = Column(Integer)
    created_at = Column(TIMESTAMP)
    modified_at = Column(TIMESTAMP)
    deleted_at = Column(TIMESTAMP)


class Discount(Base):
    __tablename__ = 'discount'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    name = Column(VARCHAR)
    desc = Column(String)
    discount_percentage = Column(DECIMAL)
    active = Column(Boolean)
    created_at = Column(TIMESTAMP)
    modified_at = Column(TIMESTAMP)
    deleted_at = Column(TIMESTAMP)
