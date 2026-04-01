from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)

    userId = Column(String, index=True)
    server = Column(String)
    promoCode = Column(String, nullable=True)

    gameName = Column(String)
    gameId = Column(String)

    packageId = Column(Integer)
    amount = Column(Float)

    timestamp = Column(String)