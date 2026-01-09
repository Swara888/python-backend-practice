"""
api_call.py
Module for fetching data from APIs with error handling.
"""
import requests

def fetch_data(url: str, timeout: int = 5):
    """
    Fetch JSON data from a URL.
    
    Args:
        url (str): API endpoint.
        timeout (int): Timeout in seconds.
    
    Returns:
        dict: JSON data or error message.
    """
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP error occurred: {http_err}"}
    except requests.exceptions.Timeout:
        return {"error": "Request timed out"}
    except requests.exceptions.RequestException as e:
        return {"error": f"Request failed: {str(e)}"}
