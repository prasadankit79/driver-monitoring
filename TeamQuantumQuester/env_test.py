import os
from dotenv import load_dotenv

# Load from same folder
load_dotenv()

print("✅ SID:", os.getenv("TWILIO_SID"))
print("✅ Phone:", os.getenv("TWILIO_PHONE"))
