import re
text = "Contact us at info@example.com or support@company.com"
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
email_addresses = re.findall(email_pattern, text)
print("Email Addresses Found:")
print(email_addresses)
