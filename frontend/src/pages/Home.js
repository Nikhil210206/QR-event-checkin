import React from "react";
import { Link } from "react-router-dom";

const Home = () => {
  return (
    <div>
      <h1>Welcome to the QR-Based Event Check-In System</h1>
      <nav>
        <Link to="/register">Register</Link> | <Link to="/login">Login</Link> | <Link to="/events">Events</Link>
      </nav>
    </div>
  );
};

export default Home;