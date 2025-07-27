from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Twilio API Credentials from environment
ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE = os.getenv("TWILIO_PHONE")
POLICE_PHONE = os.getenv("POLICE_PHONE")

def send_alert(anomalies_detected):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    alert_message = "⚠ Vehicle Anomaly Detected: \n"
    for vehicle, anomaly in anomalies_detected:
        alert_message += f"{vehicle}: {anomaly}\n"

    message = client.messages.create(
        body=alert_message,
        from_=TWILIO_PHONE,
        to=POLICE_PHONE
    )

    print(f"🚨 Alert sent to police: {alert_message}")
