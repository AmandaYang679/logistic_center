from models import Order
from db import SessionLocal

def create_order(items, status=True):
    with SessionLocal() as session:
        total_price = 0
        for item in items:
            total_price += item.price
        order = Order(items, status, total_price)
        
        session.add(order)
        session.commit()
        session.refresh(order)
        

def get_order(session, order_id: int):
    return session.get(Order, order_id)


def get_all_orders():
    with SessionLocal() as session:
        orders = session.query(Order).all()
        return orders