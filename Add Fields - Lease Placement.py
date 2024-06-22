import csv
import pandas as pd

csv_file_path = 'population_06-06-2024_2.csv'

column_names = [
    "Account Number", "Product Type", "Store, Affiliate or Brand Name", "First name", "Last name", "City", "State",
    "Zip Code", "SSN", "Date of Birth", "Home Phone Number", "Cell Phone Number", "Email Address", "Account Status",
    "Account Open Date", "Current Balance", "Lease Balance", "Fees Balance", "Last Payment Date", "Last Payment Amount",
    "Total lifetime payments", "Total Number of Lifetime Leases", "Lease Source", "Multiple / Markup", "Name of Servicer",
    "Creditor's Name at Charge-Off", "Account Owner's Name at Charge-Off", "Creditor's Address at Charge-Off",
    "Collateral Type", "Items Rented", "Collateral value", "Chapter", "Filing Date", "Case Number", "Bankruptcy Court",
    "weekly_payment_amount", "Maturity Date (contractual maturity)", "sign_date", "agreement_id", "reference_id",
    "Customer First Default - CFP", "Is Mature", "Is Mature - Customer level", "Customer Level Balance",
    ">= 60 Days Since last cleared payment - Customer level", "Status Exclusion", "Exclusion Statuses", "Text Consent (Y/N)",
    "Not previously sold", "Never Pay", "Address"
]
with open(csv_file_path, 'r', encoding='utf-8', errors='ignore') as file:
    reader = csv.reader(file)
    rows = list(reader)

rows.insert(0, column_names)
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)

df = pd.read_csv(csv_file_path)
df.to_csv("population_06-06-2024_2.csv", index=False)