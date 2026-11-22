import json
import random
from datetime import datetime

def lambda_handler(event, context=None):
    current_load = event.get("request_count", 0)
    threshold = 50
    action = ""

    if current_load > threshold:
        action = "Scale Up"
    elif current_load < 10:
        action = "Scale Down"
    else:
        action = "No Action"

    result = {
        "timestamp": datetime.utcnow().isoformat(),
        "load": current_load,
        "action": action
    }
    print(json.dumps(result, indent=2))
    return result

# Simulate function triggers
if __name__ == "__main__":
    for _ in range(5):
        mock_event = {"request_count": random.randint(0, 100)}
        lambda_handler(mock_event)
