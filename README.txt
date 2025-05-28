Project: Event Finder – Full Stack Web Application
Candidate: Sneha Gupta

This project displays live Sydney events using the Ticketmaster Discovery API.
Users can:
- View upcoming event details
- Enter their email
- Get redirected to the official ticket page

Tech Stack:
- Backend: Python Flask (REST API using Ticketmaster)
- Frontend: React + Vite
- Styling: CSS (responsive card layout)

How to Run:
1. Navigate to backend/ and install requirements:
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python app.py

2. In another terminal, navigate to frontend/:
   npm install
   npm run dev

3. Visit http://localhost:5173

Note:
- Ticketmaster API key used: 7Pp29u2juEqh5NItBiA7Dchz4crIUsOv (public access)
- All events are fetched in real-time.

