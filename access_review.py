
# Project 9: IAM Access Review & Least Privilege
# Author: David Jeffries
# Educational access review simulation

approved_permissions = {
    "Admin": {"read", "write", "delete"},
    "Analyst": {"read", "write"},
    "Employee": {"read"}
}

users = {
    "admin01": {
        "role": "Admin",
        "permissions": {"read", "write", "delete"}
    },
    "analyst01": {
        "role": "Analyst",
        "permissions": {"read", "write"}
    },
    "employee01": {
        "role": "Employee",
        "permissions": {"read", "delete"}
    },
    "employee02": {
        "role": "Employee",
        "permissions": {"read"}
    }
}

def review_access():
    print("=== IAM ACCESS REVIEW REPORT ===")

    findings = 0

    for username, account in users.items():
        role = account["role"]
        current = account["permissions"]
        approved = approved_permissions[role]

        excessive = current - approved
        missing = approved - current

        print(f"\nUser: {username}")
        print(f"Role: {role}")

        if excessive:
            findings += 1
            print("WARNING: Excessive permissions detected")
            print("Remove:", ", ".join(sorted(excessive)))
        else:
            print("PASS: No excessive permissions")

        if missing:
            print("REVIEW: Missing approved permissions:",
                  ", ".join(sorted(missing)))

    print("\n=== REVIEW SUMMARY ===")
    print("Accounts reviewed:", len(users))
    print("Accounts with excessive access:", findings)

if __name__ == "__main__":
    review_access()
