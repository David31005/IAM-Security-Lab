
# Project 9: IAM Security Audit Lab
# Author: David Jeffries
# Simulated security events only

from collections import Counter
from datetime import datetime, timezone

events = [
    ("admin01", "SUCCESS"),
    ("employee01", "FAILED"),
    ("employee01", "FAILED"),
    ("employee01", "FAILED"),
    ("analyst01", "SUCCESS"),
    ("unknown01", "FAILED"),
    ("unknown01", "FAILED"),
    ("unknown01", "FAILED")
]

audit_log = []

for username, status in events:
    audit_log.append({
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "username": username,
        "status": status
    })

print("=== IAM SECURITY AUDIT LOG ===")

for event in audit_log:
    print(event)

failed = Counter(
    event["username"]
    for event in audit_log
    if event["status"] == "FAILED"
)

print("\n=== SUSPICIOUS ACCESS REPORT ===")

alerts = 0

for username, count in failed.items():
    if count >= 3:
        alerts += 1
        print(
            f"ALERT: {username} has "
            f"{count} failed login attempts"
        )

print("\n=== SECURITY SUMMARY ===")
print("Total login events:", len(audit_log))
print("Failed login attempts:", sum(failed.values()))
print("Suspicious accounts:", alerts)
