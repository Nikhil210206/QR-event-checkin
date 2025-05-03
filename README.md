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
