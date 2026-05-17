import os
import requests
from dotenv import load_dotenv

load_dotenv()

def debug_uplink():
    token = os.getenv("TFY_API_KEY")
    url = os.getenv("TFY_GATEWAY_URL")
    
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    payload = {"model": "google/gemini-1.5-pro", "messages": [{"role": "user", "content": "Ping."}]}

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=10)
        if response.status_code == 200:
            print("✅ [SUCCESS] THE KERNEL IS ONLINE IN GOOGLE CLOUD.")
        else:
            print(f"❌ [FAILURE] {response.text}")
    except Exception as e:
        print(f"🔥 [CRITICAL] {str(e)}")

if __name__ == "__main__":
    debug_uplink()
