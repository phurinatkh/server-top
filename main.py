from fastapi import FastAPI, Depends
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import OrderPayload
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
 CORSMiddleware,
 allow_origins=["http://localhost:3000"],
 allow_credentials=True,
 allow_methods=["*"],
 allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
async def read_root():
 return """
    <html>
        <head><title>HELLOOO</title></head>
        <body>
            <h1>DAI YON NI</h1>
            <p>PLZZZ</p>
        </body>
    </html>
    """

@app.post("/")
async def create_data():
    return {"message": "Test swagger", "status": "success"}

@app.post("/OrderPayload")
async def create_order(form_data: schemas.OrderPayload,
db: Session = Depends(get_db)):
 print(f"Received data from Next.js: {form_data}")
 saved_data = crud.create_order(db=db, order=form_data)
 return {"status": "success", "message": "Appointment saved successfully",
 "data": saved_data}
 
@app.get("/OrderPayload")
async def read_order(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    order = crud.get_order(db, skip=skip, limit=limit)
    return {"status": "success", "data": order}