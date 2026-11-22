import json
import os

# Use /tmp/ in AWS Lambda (or LocalStack) because the code directory is read-only
COUNT_FILE = "/tmp/instance_count.txt"
MIN_INSTANCES = 1
MAX_INSTANCES = 10

def get_instance_count():
    if not os.path.exists(COUNT_FILE):
        return MIN_INSTANCES
    try:
        with open(COUNT_FILE, "r") as f:
            return int(f.read().strip())
    except ValueError:
        return MIN_INSTANCES

def save_instance_count(count):
    with open(COUNT_FILE, "w") as f:
        f.write(str(count))

def lambda_handler(event, context):
    # 1. Read the current instance count
    current_instances = get_instance_count()

    # 2. Extract metric or scaling decision from the incoming event
    # (Adjust key names to match your existing event payload, e.g., cpu_usage or decision)
    cpu_usage = event.get("cpu_usage", 50)
    
    if cpu_usage > 75:
        decision = "SCALE_OUT"
        new_instances = min(current_instances + 1, MAX_INSTANCES)
    elif cpu_usage < 30:
        decision = "SCALE_IN"
        new_instances = max(current_instances - 1, MIN_INSTANCES)
    else:
        decision = "NO_CHANGE"
        new_instances = current_instances

    # 3. Save the updated count back to instance_count.txt
    save_instance_count(new_instances)

    # 4. Return the result
    response_body = {
        "decision": decision,
        "previous_instances": current_instances,
        "current_instances": new_instances
    }
    print(json.dumps(response_body))

    return {
        "statusCode": 200,
        "body": json.dumps(response_body)
    }
