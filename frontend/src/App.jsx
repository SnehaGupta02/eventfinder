import './App.css';

import { useEffect, useState } from "react";

function App() {
  const [events, setEvents] = useState([]);
  const [emails, setEmails] = useState({});

  useEffect(() => {
    fetch("http://localhost:5000/api/events")
      .then((res) => res.json())
      .then(setEvents)
      .catch(console.error);
  }, []);

  const handleInput = (e, id) => {
    setEmails({ ...emails, [id]: e.target.value });
  };

  const handleSubmit = async (id) => {
    const email = emails[id];
    if (!email) return alert("Please enter your email");

    const res = await fetch(`http://localhost:5000/api/ticket/${id}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email }),
    });

    const data = await res.json();
    if (data.url) {
      window.open(data.url, "_blank");
    } else {
      alert("Event not found");
    }
  };

 return (
  <>
    <h1>Live Events in Sydney</h1>
    <div className="container">
      {events.map((ev) => (
        <div key={ev.id} className="card">
          <img src={ev.image} alt={ev.title} />
          <h3>{ev.title}</h3>
          <p><strong>When:</strong> {new Date(ev.start).toLocaleString()}</p>
          <p><strong>Where:</strong> {ev.venue}</p>
          <input
            type="email"
            placeholder="Enter email"
            value={emails[ev.id] || ""}
            onChange={(e) => handleInput(e, ev.id)}
          />
          <button onClick={() => handleSubmit(ev.id)}>Get Tickets</button>
        </div>
      ))}
    </div>
  </>
);

}

export default App;

