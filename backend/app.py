from flask import Flask, jsonify, request, redirect
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_KEY = "7Pp29u2juEqh5NItBiA7Dchz4crIUsOv"
CITY = "Sydney"

# In-memory store
LEADS = []

@app.route("/api/events")
def get_events():
    url = "https://app.ticketmaster.com/discovery/v2/events.json"
    params = {
        "apikey": API_KEY,
        "city": CITY,
        "countryCode": "AU",
        "size": 20,
        "sort": "date,asc",
    }

    r = requests.get(url, params=params, timeout=10)
    data = r.json()

    events = []
    for ev in data.get("_embedded", {}).get("events", []):
        events.append({
            "id": ev["id"],
            "title": ev["name"],
            "start": ev["dates"]["start"].get("dateTime", "N/A"),
            "venue": ev["_embedded"]["venues"][0]["name"],
            "url": ev.get("url"),
            "image": ev["images"][0]["url"] if ev.get("images") else "",
        })

    return jsonify(events)

@app.route("/api/ticket/<event_id>", methods=["POST"])
def get_ticket(event_id):
    email = request.json.get("email")
    if not email:
        return {"error": "Email required"}, 400

    # Fetch event URL to redirect
    url = f"https://app.ticketmaster.com/discovery/v2/events/{event_id}.json"
    params = {"apikey": API_KEY}
    r = requests.get(url, params=params)
    event = r.json()
    redirect_url = event.get("url")

    if redirect_url:
        LEADS.append({"email": email, "event_id": event_id})
        return jsonify({"url": redirect_url})
    else:
        return {"error": "Event not found"}, 404


import os

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)


