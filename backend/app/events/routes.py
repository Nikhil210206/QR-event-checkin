from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models import Event, EventRegistration, User
from schemas import EventCreate
from utils.qr_generator import generate_qr_code
from utils.email_sender import send_email
from datetime import datetime
from typing import List

router = APIRouter()

@router.post("/create", status_code=201)
def create_event(event: EventCreate, db: Session = Depends(get_db), current_user: User = Depends()):
    if not current_user.is_admin:
        raise HTTPException(status_code=403, detail="Only admins can create events")
    
    new_event = Event(
        title=event.title,
        description=event.description,
        location=event.location,
        date=event.date,
        time=event.time,
        created_by=current_user.id
    )
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return {"message": "Event created successfully", "event_id": new_event.id}

@router.post("/register/{event_id}")
def register_for_event(event_id: int, db: Session = Depends(get_db), current_user: User = Depends()):
    # Check if event exists
    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    
    # Check if user has already registered
    existing_registration = db.query(EventRegistration).filter(
        EventRegistration.user_id == current_user.id,
        EventRegistration.event_id == event_id
    ).first()
    if existing_registration:
        raise HTTPException(status_code=400, detail="User already registered for this event")
    
    # Generate QR code
    qr_data = f"User: {current_user.id}, Event: {event.id}, Timestamp: {datetime.now()}"
    qr_code = generate_qr_code(qr_data)

    # Save registration
    registration = EventRegistration(
        user_id=current_user.id,
        event_id=event.id,
        qr_code=qr_code
    )
    db.add(registration)
    db.commit()
    db.refresh(registration)

    # Send email with QR code
    email_body = f"""
    Hi {current_user.name},

    You have successfully registered for the event: {event.title}.
    Event Details:
    - Location: {event.location}
    - Date: {event.date}
    - Time: {event.time}

    Your QR Code is attached for check-in.

    Regards,
    Event Team
    """
    send_email(current_user.email, "Event Registration Confirmation", email_body, qr_code)

    return {"message": "Registration successful, QR code sent to your email"}