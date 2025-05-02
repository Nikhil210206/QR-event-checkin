import React from "react";
import { Link } from "react-router-dom";

const AdminHome = () => {
  return (
    <div>
      <h1>Admin Dashboard</h1>
      <nav>
        <Link to="/admin">View Dashboard</Link> | <Link to="/admin/export">Export Attendees</Link>
      </nav>
    </div>
  );
};

export default AdminHome;