from models import Item
from db import SessionLocal


def create_item(cell: int, name: str, price: float):
    with SessionLocal() as session:
        item = Item(cell, name, price)
        
        session.add(item)
        session.commit()
        session.refresh(item)
        

def get_item(session, item_id: int):
    return session.get(Item, item_id)


def get_all_items():
    with SessionLocal() as session:
        items = session.query(Item).all()
        return items


def update_item(item_id: int, name: str = None, price: float = None):
    with SessionLocal() as session:
        item = get_item(session, item_id)
        
        if item is None:
            return None
        
        item.name = name
        item.price = price

        session.commit()
        session.refresh(item)
        
        return item
    

def delete_item(item_id: int):
    with SessionLocal() as session:
        item = get_item(session, item_id)
        
        if item is None:
            return None
        
        session.delete(item)
        session.commit()
        
        return f"Item deleted: {item.name}"