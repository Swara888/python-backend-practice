"""
demo.py
Demonstrates usage of file_handling, data_validation, and api_call modules.
"""
from file_handling import read_file, write_file
from data_validation import validate_email, validate_phone
from api_call import fetch_data

# File handling
print(write_file("example.txt", "Hello World from Python Backend!"))
print(read_file("example.txt"))

# Data validation
print(validate_email("test@example.com"))  # True
print(validate_email("invalid_email"))     # False
print(validate_phone("1234567890"))        # True
print(validate_phone("12345"))             # False

# API call
api_result = fetch_data("https://jsonplaceholder.typicode.com/todos/1")
print(api_result)
