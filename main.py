# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print("================================")
print("     JOB APPLICATION TRACKER")
print("================================")
applications = []

while True:
    print("\n--- Job Application Tracker ---")
    company = input("Enter company name (or 'stop' to finish): ")

    if company.lower() == "stop":
        break

    role = input("Enter job role: ")
    status = input("Enter application status: ")

    application = {
        "company": company,
        "role": role,
        "status": status
    }

    applications.append(application)

print("\n--- Your Job Applications ---")

for app in applications:
    print("Company:", app["company"])
    print("Role:", app["role"])
    print("Status:", app["status"])
    print("--------------------")

