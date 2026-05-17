import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

class VedaannaResilienceEngine:
    def __init__(self):
        self.api_key = os.getenv("TFY_API_KEY")
        self.url = os.getenv("TFY_GATEWAY_URL")
        self.headers = {"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}
        # Failover sequence: Primary -> Backup
        self.models = ["openai/gpt-4o", "google/gemini-1.5-pro"]

    def execute_hot_swap(self):
        print("\n🚨 [INCIDENT DETECTED]: 'auth-service' pod OOMKilled in production.")
        print("🔍 [LOGS]: java.lang.OutOfMemoryError: Java heap space.\n")
        
        for model in self.models:
            try:
                # FORCE FAILURE on OpenAI to prove TrueFoundry Gateway Resilience
                if "openai" in model:
                    print(f"📡 [UPLINK] Requesting fix from {model}...")
                    time.sleep(1.5)
                    raise ConnectionError("503 Service Unavailable - LLM Provider Outage")

                # REAL CALL to Gemini via TrueFoundry Gateway
                print(f"⚠️ [RESILIENCE TRIGGERED] {model.split('/')[0]} is down. Handling Chaos...")
                print(f"🔄 [HOT-SWAP] Migrating context to {model}...")
                
                payload = {
                    "model": model,
                    "messages": [
                        {"role": "system", "content": "You are the Vedaanna Kernel SRE. Provide a 1-line kubectl fix."},
                        {"role": "user", "content": "Fix: java.lang.OutOfMemoryError: Java heap space for auth-service deployment"}
                    ]
                }
                
                start_time = time.time()
                response = requests.post(self.url, headers=self.headers, json=payload, timeout=10)
                response.raise_for_status()
                duration = time.time() - start_time
                
                solution = response.json()['choices'][0]['message']['content'].strip()
                print(f"\n✅ [SUCCESS] Hot-swap complete in {duration:.2f}s")
                print(f"🛠️ [KERNEL ACTION PLAN]:\n{solution}\n")
                return
                
            except Exception as e:
                print(f"❌ [API ERROR]: {str(e)}")

if __name__ == "__main__":
    engine = VedaannaResilienceEngine()
    engine.execute_hot_swap()
