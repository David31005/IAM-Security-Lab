
# Project 9: Identity and Access Management Security Lab
# Author: David Jeffries
# Purpose: Demonstrate role-based access control (RBAC)

users = {
    "admin_user": "Admin",
    "security_analyst": "Analyst",
    "regular_employee": "Employee"
}

permissions = {
    "Admin": ["read", "write", "delete"],
    "Analyst": ["read", "write"],
    "Employee": ["read"]
}

def check_access(username, action):
    if username not in users:
        return "ACCESS DENIED: Unknown user"

    role = users[username]

    if action in permissions[role]:
        return f"ACCESS GRANTED: {username} can {action}"

    return f"ACCESS DENIED: {username} cannot {action}"


if __name__ == "__main__":
    print("=== IAM Security Lab ===")
    print(check_access("admin_user", "delete"))
    print(check_access("security_analyst", "write"))
    print(check_access("regular_employee", "delete"))
    print(check_access("unknown_user", "read"))
  
