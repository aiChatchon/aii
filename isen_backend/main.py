import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from apscheduler.schedulers.background import BackgroundScheduler
from typing import List

from isen.db import SessionLocal, Base, engine
from isen.models import Order, OrderItem
from isen.tasks import fetch_and_store_orders


Base.metadata.create_all(bind=engine)

app = FastAPI(title="ISEN Backend")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/orders")
def list_orders(db: Session = Depends(get_db)):
    orders = db.query(Order).all()
    results = []
    for o in orders:
        results.append({
            'id': o.id,
            'order_id': o.order_id,
            'platform': o.platform,
            'customer_name': o.customer_name,
            'status': o.status,
            'total_amount': o.total_amount,
            'created_at': o.created_at,
            'updated_at': o.updated_at,
        })
    return results


@app.get("/orders/{order_id}")
def get_order(order_id: int, db: Session = Depends(get_db)):
    order = db.query(Order).filter_by(id=order_id).first()
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return {
        'id': order.id,
        'order_id': order.order_id,
        'platform': order.platform,
        'customer_name': order.customer_name,
        'status': order.status,
        'total_amount': order.total_amount,
        'created_at': order.created_at,
        'updated_at': order.updated_at,
        'items': [
            {
                'id': item.id,
                'product_id': item.product_id,
                'quantity': item.quantity,
                'price_per_unit': item.price_per_unit,
            } for item in order.items
        ]
    }


def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(fetch_and_store_orders, 'interval', minutes=30)
    scheduler.start()


start_scheduler()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
