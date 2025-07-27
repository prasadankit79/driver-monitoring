import os
from pathlib import Path
from dotenv import load_dotenv
from twilio.rest import Client

# Load .env from project root
env_path = Path(__file__).resolve().parents[3] / '.env'
load_dotenv(dotenv_path=env_path)

ACCOUNT_SID = os.getenv("TWILIO_SID")
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
