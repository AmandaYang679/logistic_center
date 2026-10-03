from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String
from db import engine


class Base(DeclarativeBase):
    pass


class Item(Base):
    __tablename__ = "items"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cell: Mapped[int] = mapped_column(unique=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[float] = mapped_column()
    
    def __repr__(self):
        return f"Item(id={self.id}, cell={self.cell}, name='{self.name}',  price={self.price})"
    
    
class Order(Base):
    __tablename__ = "orders"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    item_id: Mapped[int] = mapped_column()
    status: Mapped[int] = mapped_column()
    total_price: Mapped[float] = mapped_column()
    
    def __repr__(self):
        return f"Order(id={self.id}, item_id={self.item_id}, status={self.status}, total_price={self.total_price})"
    

Base.metadata.create_all(engine)