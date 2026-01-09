"""
data_validation.py
Module for validating emails and phone numbers.
"""

def validate_email(email: str) -> bool:
    """
    Validates an email address format.
    
    Args:
        email (str): Email to validate.
    
    Returns:
        bool: True if valid, False otherwise.
    """
    if not isinstance(email, str):
        raise TypeError("Email must be a string")
    return "@" in email and "." in email

def validate_phone(phone: str) -> bool:
    """
    Validates an Indian phone number (10 digits).
    
    Args:
        phone (str): Phone number to validate.
    
    Returns:
        bool: True if valid, False otherwise.
    """
    if not isinstance(phone, str):
        raise TypeError("Phone must be a string")
    return phone.isdigit() and len(phone) == 10
