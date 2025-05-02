import React from "react";
import API from "../../api";

const ExportAttendees = ({ eventId }) => {
  const exportData = async (format) => {
    try {
      const response = await API.get(`/admin/export/${eventId}?format=${format}`);
      const blob = new Blob([response.data], { type: format === "csv" ? "text/csv" : "application/json" });
      const url = window.URL.createObjectURL(blob);
      const link = document.createElement("a");
      link.href = url;
      link.setAttribute("download", `attendees.${format}`);
      document.body.appendChild(link);
      link.click();
    } catch (error) {
      alert("Failed to export data");
    }
  };

  return (
    <div>
      <button onClick={() => exportData("csv")}>Export as CSV</button>
      <button onClick={() => exportData("json")}>Export as JSON</button>
    </div>
  );
};

export default ExportAttendees;