import re

def is_valid_mobile_number(mobile_number):
  pattern = r'^[6-9]\d{9}$'  # Matches numbers starting with 6-9 and then 9 digits
  return bool(re.match(pattern, mobile_number))

# Example usage
mobile_number = "9876543210"
if is_valid_mobile_number(mobile_number):
  print("Valid mobile number")
else:
  print("Invalid mobile number")
