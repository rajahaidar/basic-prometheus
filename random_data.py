#!/usr/bin/env python3

import requests
import random
import time

while True:
    metric = f'''mymetric{{site_id="raja"}} {random.randint(1, 100)}
mymetric{{site_id="raja2"}} {random.randint(1, 100)}
'''
    print(f"Inserting metrics into pushgateway")
    print(metric)
    response = requests.post('http://localhost:9091/metrics/job/my-push-job', data=metric)
    print(response.text)
    print(response.status_code)
    time.sleep(30)
