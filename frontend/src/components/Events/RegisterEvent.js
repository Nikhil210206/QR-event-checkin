import React from "react";
import API from "../../api";

const RegisterEvent = ({ eventId }) => {
  const handleRegister = async () => {
    try {
      const response = await API.post(`/events/register/${eventId}`);
      alert(response.data.message);
    } catch (error) {
      alert(error.response.data.detail);
    }
  };

  return <button onClick={handleRegister}>Register for Event</button>;
};

export default RegisterEvent;