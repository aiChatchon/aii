from .db import SessionLocal
from .models import Order, OrderItem, Product
from .shopee import fetch_orders
from sqlalchemy.orm import Session


def insert_orders(session: Session, orders_data):
    for order_data in orders_data:
        if session.query(Order).filter_by(order_id=order_data['order_id']).first():
            continue
        order = Order(
            order_id=order_data['order_id'],
            platform=order_data['platform'],
            customer_name=order_data['customer_name'],
            status=order_data['status'],
            total_amount=order_data['total_amount'],
        )
        session.add(order)
        session.flush()  # to get order.id

        for item in order_data.get('items', []):
            product = session.query(Product).filter_by(sku=item['sku']).first()
            product_id = product.id if product else None
            order_item = OrderItem(
                order_id=order.id,
                product_id=product_id,
                quantity=item['quantity'],
                price_per_unit=item['price'],
            )
            session.add(order_item)
    session.commit()


def fetch_and_store_orders():
    session = SessionLocal()
    try:
        orders = fetch_orders()
        insert_orders(session, orders)
    finally:
        session.close()
