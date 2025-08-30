import boto3
import csv
from datetime import datetime


iam = boto3.client("iam")
response = iam.list_users()
filename = f"../reports/iam_audit_{datetime.now().strftime('%Y%m%d')}.csv"

with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["UserName", "CreateDate", "PasswordLastUsed"])

    for user in response["Users"]:
        writer.writerow([
            user["UserName"],
            user["CreateDate"],
            user.get("PasswordLastUsed", "N/A")
        ])

print(f"[+] Report saved as {filename}")
