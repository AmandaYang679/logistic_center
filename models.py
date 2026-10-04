from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import CheckConstraint, String
from db import engine


class Base(DeclarativeBase):
    pass


class Item(Base):
    __tablename__ = "items"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    cell: Mapped[int] = mapped_column(unique=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[float] = mapped_column()
    
    __table_args__ = (
        CheckConstraint("price > 0", name="check_price_positive"),
        CheckConstraint("cell > 0", name="check_cell_positive"),
    )
    
    def __repr__(self):
        return f"Item(id={self.id}, cell={self.cell}, name='{self.name}',  price={self.price})"
    
    
class Order(Base):
    __tablename__ = "orders"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    items: Mapped[list] = mapped_column(nullable=False)
    status: Mapped[bool] = mapped_column()
    total_price: Mapped[float] = mapped_column()
    
    __table_args__ = (
        CheckConstraint("total_price > 0", name="check_total_price_positive"),
    )
    
    def __repr__(self):
        return f"Order(id={self.id}, items={self.items}, status={self.status}, total_price={self.total_price})"
    

Base.metadata.create_all(engine)