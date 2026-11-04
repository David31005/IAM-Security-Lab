
# Project 9: IAM MFA Security Lab
# Author: David Jeffries
# Educational MFA policy simulation

users = {
    "admin01": {"role": "Admin", "mfa_enabled": True},
    "analyst01": {"role": "Analyst", "mfa_enabled": True},
    "employee01": {"role": "Employee", "mfa_enabled": False}
}

def check_login(username, mfa_verified):
    user = users.get(username)

    if user is None:
        return "ACCESS DENIED: Unknown user"

    if not user["mfa_enabled"]:
        return "ACCESS DENIED: MFA enrollment required"

    if not mfa_verified:
        return "ACCESS DENIED: MFA verification required"

    return f"ACCESS GRANTED: {username}"

if __name__ == "__main__":
    print("=== IAM MFA Security Lab ===")
    print(check_login("admin01", True))
    print(check_login("analyst01", False))
    print(check_login("employee01", True))
    print(check_login("unknown01", True))
