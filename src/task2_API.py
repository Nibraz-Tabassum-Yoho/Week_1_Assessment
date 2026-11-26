import csv
import json
import requests
import os

from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv("API_KEY")

print("API Key loaded:", bool(API_KEY))

employees = []

high_earners = []

with open("employees.csv", "r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["id"] = int(row["id"])
        row["salary"] = int(row["salary"])
        employees.append(row)
        if row["salary"] > 50000:
            high_earners.append(row)

with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)

with open("high_earners.csv", "w", newline="") as file:
    fieldnames = ["id", "name", "department", "salary", "city"]
    writer = csv.DictWriter(
        file,
        fieldnames=fieldnames
    )
    writer.writeheader()
    writer.writerows(high_earners)

print(
    f"Rows read: {len(employees)} | "
    f"High earners: {len(high_earners)}"
)

url = "https://jsonplaceholder.typicode.com/users"
try:

    response = requests.get(url, timeout=5)
    response.raise_for_status()
    users = response.json()
    print("\nFirst 3 users:")
    for user in users[:3]:
        print(
            user.get("id"),
            "-",
            user.get("name"),
            "-",
            user.get("email")
        )

except requests.exceptions.Timeout:
    print("Request timed out!")

except requests.exceptions.ConnectionError:
    print("Connection error!")

except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)

not_found_url = (
    "https://jsonplaceholder.typicode.com/users/9999"
)
try:
    response = requests.get(
        not_found_url,
        timeout=5
    )
    if response.status_code == 404:
        print("/users/9999 -> 404 Not found")
    else:
        response.raise_for_status()

except requests.exceptions.Timeout:
    print("404 request timed out!")

except requests.exceptions.ConnectionError:
    print("Connection error!")

except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)

try:

    response = requests.get(url, timeout=5)
    response.raise_for_status()
    users = response.json()
    parsed_users = []
    for user in users:
        company = user.get("company", {})
        address = user.get("address", {})
        parsed_user = {
            "id": user.get("id"),
            "name": user.get("name"),
            "email": user.get("email"),
            "city": address.get("city"),
            "company_name": company.get("name"),
            "catch_phrase": company.get("catchPhrase")
        }
        parsed_users.append(parsed_user)
    with open("users.json", "w") as file:

        json.dump(
            parsed_users,
            file,
            indent=4
        )

    print("\nNested JSON saved to users.json")
except requests.exceptions.Timeout:
    print("Request timed out!")

except requests.exceptions.ConnectionError:
    print("Connection error!")

except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)
