import time
import requests

replicas = [
    {"name": "replica1", "url": "http://localhost:5001"},
    {"name": "replica2", "url": "http://localhost:5002"}
]

def check_health(url):
    try:
        response = requests.get(url + "/health", timeout=2)
        return response.status_code == 200 and response.json().get("status") == "healthy"
    except:
        return False

def route_request():
    for replica in replicas:
        if check_health(replica["url"]):
            print(f"[ACTIVE] Routing to {replica['name']}")
            try:
                response = requests.get(replica["url"] + "/predict")
                print("Response:", response.json())
            except Exception as e:
                print("Error during request:", str(e))
            return
    print("[ERROR] All replicas are unavailable!")

if __name__ == "__main__":
    while True:
        route_request()
        time.sleep(5)
