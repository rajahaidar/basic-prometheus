#!/usr/bin/env bash

while true
do
    echo "Inserting random data"
	echo "mymetric{site_id=\"raja\"} $((1 + $RANDOM % 100))\nmymetric{site_id=\"raja2\"} $((1 + $RANDOM % 100))" | curl --data-binary @- http://localhost:9091/metrics/job/my-push-job
    echo "Sleeping for 30 secs"
    sleep 30
done
