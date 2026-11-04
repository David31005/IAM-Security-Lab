
# Identity & Access Management (IAM) Security Lab

**Author:** David Jeffries

## Project Overview

A Python-based cybersecurity portfolio project demonstrating fundamental Identity and Access Management (IAM) security controls.

The lab uses simulated employee accounts and security events to demonstrate user provisioning, role-based access control, MFA policy checks, least privilege, access reviews, and suspicious login detection.

## Project Objectives

- Simulate user account creation and deactivation
- Enforce role-based access control (RBAC)
- Demonstrate least-privilege principles
- Evaluate MFA enrollment and verification flags
- Identify excessive user permissions
- Generate security audit logs
- Detect repeated failed login attempts

## Technologies Used

- Python 3
- GitHub
- Google Colab
- Python standard library
- Requests library for downloading scripts

## Project Files

| File | Description |
|---|---|
| `iam_security.py` | Role-based access control |
| `user_provisioning.py` | Account creation and deactivation |
| `mfa_security.py` | MFA policy simulation |
| `access_review.py` | Least-privilege access review |
| `security_audit.py` | Login auditing and suspicious activity detection |

## Security Features

### 1. Role-Based Access Control

Defines Admin, Analyst, and Employee roles with different permissions.

### 2. User Provisioning

Creates simulated employee accounts, assigns roles, and deactivates accounts.

Disabled accounts are denied access.

### 3. MFA Policy Simulation

Evaluates MFA enrollment and verification status.

This is a policy simulation, not a real MFA authentication service.

### 4. Access Reviews

Compares assigned permissions with approved role permissions.

The sample review identifies an employee account with excessive delete privileges.

### 5. Security Audit Logging

Records simulated authentication events and identifies accounts with three or more failed login attempts.

## Sample Test Results

### Access Review

- Accounts reviewed: 4
- Accounts with excessive permissions: 1
- Excessive permission identified: delete

### Security Audit

- Login events: 8
- Failed login attempts: 6
- Accounts flagged: 2

## How to Run

1. Open Google Colab.
2. Create a Python notebook.
3. Download a project script from this repository.
4. Run the script and review its output.

Example:

```python
import requests

url = "https://raw.githubusercontent.com/David31005/IAM-Security-Lab/main/security_audit.py"

response = requests.get(url, timeout=15)
response.raise_for_status()

with open("security_audit.py", "w") as file:
    file.write(response.text)

%run security_audit.py
```

## Security Concepts Demonstrated

- Identity and Access Management (IAM)
- Role-Based Access Control (RBAC)
- Principle of Least Privilege
- Account Provisioning and Deprovisioning
- MFA Policy Enforcement
- Access Reviews
- Security Audit Logging
- Suspicious Authentication Detection

## Limitations

This is an educational simulation using fictional users and predefined security events.

It does not connect to production identity providers, verify real MFA codes, or modify live user accounts.

## Career Relevance

This project demonstrates foundational concepts relevant to:

- IAM Analyst I
- Junior Cybersecurity Analyst
- SOC Analyst I
- Security Compliance Analyst
- IT Security Analyst

## Author

David Jeffries

[GitHub Portfolio](https://github.com/David31005)

[LinkedIn](https://www.linkedin.com/in/david-jeffries001)
  
