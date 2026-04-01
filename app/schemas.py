from pydantic import BaseModel
from typing import Optional
class OrderPayload(BaseModel):
    userId: str
    server: str
    promoCode: Optional[str] = None
    gameName: str
    gameId: str
    packageId: int
    amount: float
    timestamp: str