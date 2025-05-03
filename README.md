QR-Based Event Check-In System

Description
The QR-Based Event Check-In System is a backend and frontend application designed to manage college event check-ins using QR codes. Users can register for events, receive a unique QR code, and check in on the event day. Admins can manage events, view attendees, and export attendee data.

Features

User Features
Register using name, email, student ID, and password.
Login with JWT-based authentication.
Register for events and receive a unique QR code via email.
View event details.

Admin Features
Create events with title, description, location, date, and time.
View registered attendees and their check-in status.
Export attendee lists in CSV or JSON format.

Technologies Used

Backend
Framework: FastAPI (Python)
Database: PostgreSQL
Authentication: JWT-based login/signup
QR Code Generation: qrcode package
Email Integration: SMTP (can be replaced with SendGrid)

Frontend
Framework: React.js
Routing: React Router
HTTP Client: Axios

Project Structure
Backend:
backend/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── auth/
│   │   ├── routes.py
│   │   ├── utils.py
│   ├── events/
│   │   ├── routes.py
│   │   ├── utils.py
│   ├── admin/
│   │   ├── routes.py
│   ├── utils/
│       ├── qr_generator.py
│       ├── email_sender.py
├── .env
├── requirements.txt

Frontend: 
frontend/
├── public/
├── src/
│   ├── components/
│   │   ├── Auth/
│   │   │   ├── Login.js
│   │   │   ├── Register.js
│   │   ├── Events/
│   │   │   ├── EventList.js
│   │   │   ├── EventDetails.js
│   │   │   ├── RegisterEvent.js
│   │   ├── Admin/
│   │   │   ├── Dashboard.js
│   │   │   ├── ExportAttendees.js
│   ├── pages/
│   │   ├── Home.js
│   │   ├── AdminHome.js
│   ├── App.js
│   ├── api.js
│   ├── index.js

Setup Instructions

Backend:
1. Clone the repository: git clone [https://github.com/your-username/your-repo.git](https://github.com/Nikhil210206/QR-event-checkin)
cd backend

2. Create a virtual environment and activate it: python3 -m venv venv
source venv/bin/activate

3. pip install -r requirements.txt

4. Set up .env file:
DATABASE_URL=postgresql://username:password@localhost:5432/event_db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

5. Run database migrations: alembic upgrade head

6. Start Backend Server: uvicorn app.main:app --host 0.0.0.0 --port 8000

7. Access Swagger UI: http://localhost:8000/docs

Frontend: 
1. cd frontend
2. npm install
3. npm start
4. Access Frontend: http://localhost:3000
   
User Flow:
Register and log in as a user.
View available events and register for an event.
Receive a QR code via email for check-in.

Admin Flow:
Log in as an admin.
Create events and manage attendees.
Export attendee data in CSV or JSON format.
Environment Variables
The following environment variables are required for the backend:

DATABASE_URL: PostgreSQL connection string.
SECRET_KEY: Secret key for JWT authentication.
ALGORITHM: Algorithm for JWT (e.g., HS256).
ACCESS_TOKEN_EXPIRE_MINUTES: Token expiration time in minutes.

