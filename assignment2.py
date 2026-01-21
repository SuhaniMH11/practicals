name = input("Enter vendor name: ")
year = int(input("Enter year of association: "))
contact = input("Enter contact number: ")
email = input("Enter email ID: ")

monthly_purchases = []
for i in range(12):
    amount = float(input("Enter purchase amount for month " + str(i + 1) + ": "))
    monthly_purchases.append(amount)

annual_total = sum(monthly_purchases)

print("\n--- Annual Purchase / Billing Report ---")
print("Vendor Name:", name)
print("Year of Association:", year)
print("Contact Number:", contact)
print("Email ID:", email)
print("Monthly Purchases:")
for i in range(12):
    print("Month", i + 1, ":", monthly_purchases[i])
print("Annual Purchase/Billing Amount:", annual_total)
