import React, { useEffect, useState } from "react";
import API from "../../api";

const Dashboard = () => {
  const [attendees, setAttendees] = useState([]);

  useEffect(() => {
    const fetchAttendees = async () => {
      const response = await API.get("/admin/attendees/1"); // Replace 1 with event ID
      setAttendees(response.data);
    };
    fetchAttendees();
  }, []);

  return (
    <div>
      <h1>Admin Dashboard</h1>
      <ul>
        {attendees.map((attendee) => (
          <li key={attendee.id}>
            User ID: {attendee.user_id}, Checked In: {attendee.checked_in ? "Yes" : "No"}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Dashboard;