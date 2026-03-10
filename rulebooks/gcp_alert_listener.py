import json
import time

while True:
    event = {"alert": "test"}
    print(json.dumps(event), flush=True)
    time.sleep(30)
