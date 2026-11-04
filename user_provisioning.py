
# Project 9: IAM User Provisioning Lab
# Author: David Jeffries
# Simulated accounts only — no real user data

from datetime import datetime, timezone

users = {}
audit_log = []

VALID_ROLES = {"Admin", "Analyst", "Employee"}

def log_event(action, username):
    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "action": action,
        "username": username
    }
    audit_log.append(event)

def create_user(username, role):
    if not username or username in users:
        return "ERROR: Invalid or existing user"

    if role not in VALID_ROLES:
        return "ERROR: Invalid role"

    users[username] = {
        "role": role,
        "active": True
    }

    log_event("USER_CREATED", username)
    return f"CREATED: {username} ({role})"

def deactivate_user(username):
    if username not in users:
        return "ERROR: User not found"

    users[username]["active"] = False
    log_event("USER_DEACTIVATED", username)

    return f"DEACTIVATED: {username}"

def check_user_access(username):
    user = users.get(username)

    if not user:
        return "ACCESS DENIED: Unknown user"

    if not user["active"]:
        return "ACCESS DENIED: Account disabled"

    return f"ACCESS ACTIVE: {username}"

if __name__ == "__main__":
    print("=== IAM User Provisioning Lab ===")

    print(create_user("employee01", "Employee"))
    print(create_user("analyst01", "Analyst"))

    print(check_user_access("employee01"))

    print(deactivate_user("employee01"))

    print(check_user_access("employee01"))

    print("\n=== Security Audit Log ===")
    for event in audit_log:
        print(event)
