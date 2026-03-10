import json
import time
from google.cloud import monitoring_v3

project_id = "orms-sta-project"

client = monitoring_v3.AlertPolicyServiceClient()
name = f"projects/{project_id}"

while True:

    policies = client.list_alert_policies(request={"name": name})

    for p in policies:

        event = {
            "alert_name": p.display_name,
            "project": project_id
        }

        print(json.dumps(event), flush=True)

    time.sleep(60)
