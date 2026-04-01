from sqlalchemy.orm import Session
from app import models, schemas

def create_order(db: Session, order: schemas.OrderPayload):
    db_order = models.Order(
        userId=order.userId,
        server=order.server,
        promoCode=order.promoCode,
        gameName=order.gameName,
        gameId=order.gameId,
        packageId=order.packageId,
        amount=order.amount,
        timestamp=order.timestamp
    )

    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

def get_order(db: Session, skip: int = 0, limit: int = 100):
 return db.query(models.Order).offset(skip).limit(limit).all()