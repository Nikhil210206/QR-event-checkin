from fastapi import FastAPI
from auth.routes import router as auth_router
from events.routes import router as events_router
from admin.routes import router as admin_router
from database import Base, engine

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="QR-Based Event Check-In System",
    description="API documentation for the QR-based event check-in system.",
    version="1.0.0",
    contact={
        "name": "Support Team",
        "email": "support@example.com",
    },
)

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

# Register routers
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(events_router, prefix="/events", tags=["Events"])
app.include_router(admin_router, prefix="/admin", tags=["Admin"])