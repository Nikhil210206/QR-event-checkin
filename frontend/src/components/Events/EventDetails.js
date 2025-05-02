import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import API from "../../api";

const EventDetails = () => {
  const { eventId } = useParams();
  const [event, setEvent] = useState(null);

  useEffect(() => {
    const fetchEvent = async () => {
      const response = await API.get(`/events/${eventId}`);
      setEvent(response.data);
    };
    fetchEvent();
  }, [eventId]);

  if (!event) return <p>Loading...</p>;

  return (
    <div>
      <h1>{event.title}</h1>
      <p>{event.description}</p>
      <p>Location: {event.location}</p>
      <p>Date: {event.date}</p>
      <p>Time: {event.time}</p>
    </div>
  );
};

export default EventDetails;