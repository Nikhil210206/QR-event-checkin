from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Event, EventRegistration
from typing import List
import csv
import json

router = APIRouter()

@router.get("/attendees/{event_id}")
def get_attendees(event_id: int, db: Session = Depends(get_db)):
    attendees = db.query(EventRegistration).filter(EventRegistration.event_id == event_id).all()
    return attendees

@router.get("/export/{event_id}")
def export_attendees(event_id: int, format: str, db: Session = Depends(get_db)):
    attendees = db.query(EventRegistration).filter(EventRegistration.event_id == event_id).all()
    if format == "csv":
        with open("attendees.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(["User ID", "Event ID", "Checked In"])
            for attendee in attendees:
                writer.writerow([attendee.user_id, attendee.event_id, attendee.checked_in])
        return {"message": "CSV exported successfully"}
    elif format == "json":
        return json.dumps([{"user_id": a.user_id, "event_id": a.event_id, "checked_in": a.checked_in} for a in attendees])
    else:
        raise HTTPException(status_code=400, detail="Invalid format")