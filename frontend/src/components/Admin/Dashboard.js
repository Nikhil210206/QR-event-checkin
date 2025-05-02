import React, { useEffect, useState } from "react";
import API from "../../api";

const Dashboard = () => {
  const [attendees, setAttendees] = useState([]);
  const [eventId, setEventId] = useState(1); // Replace with dynamic event ID if needed

  useEffect(() => {
    const fetchAttendees = async () => {
      const response = await API.get(`/admin/attendees/${eventId}`);
      setAttendees(response.data);
    };
    fetchAttendees();
  }, [eventId]);

  const exportData = async (format) => {
    try {
      const response = await API.get(`/admin/export/${eventId}?format=${format}`);
      if (format === "csv") {
        const blob = new Blob([response.data], { type: "text/csv" });
        const url = window.URL.createObjectURL(blob);
        const link = document.createElement("a");
        link.href = url;
        link.setAttribute("download", "attendees.csv");
        document.body.appendChild(link);
        link.click();
      } else {
        const jsonData = JSON.stringify(response.data, null, 2);
        const blob = new Blob([jsonData], { type: "application/json" });
        const url = window.URL.createObjectURL(blob);
        const link = document.createElement("a");
        link.href = url;
        link.setAttribute("download", "attendees.json");
        document.body.appendChild(link);
        link.click();
      }
    } catch (error) {
      alert("Failed to export data");
    }
  };

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
      <button onClick={() => exportData("csv")}>Export as CSV</button>
      <button onClick={() => exportData("json")}>Export as JSON</button>
    </div>
  );
};

export default Dashboard;