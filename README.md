# AWS IAM Audit + Budget Control

## Why this project

When I was experimenting in AWS, I noticed two recurring problems:

* Old IAM users and keys that nobody touches anymore.
* Test resources that keep running and quietly add to the bill.

This project is my attempt to solve both issues in a simple way.

## What it does

* A **Python script** that lists IAM users, their last login, and flags unused keys.
* A **Terraform module** that sets up AWS Budgets with email alerts (so I get a warning before costs run away).

## Tech I used

* **AWS IAM** – user and key data.
* **AWS Budgets** – to send cost alerts.
* **boto3 + AWS CLI** – for scripting.
* **Terraform** – to manage the budget setup as code.

## Key features

* Exports a CSV report of IAM users + last login.
* Identifies inactive access keys.
* Sends budget alerts (default: \$5).
* Terraform code is modular so it can be reused.

## Project layout

```
aws-iam-audit-budget-control/
│── scripts/    # Python IAM audit script
│── reports/    # Generated CSV reports
│── infra/      # Terraform configs for budgets
│── docs/       # Diagrams and screenshots
│── README.md   # This file
```
