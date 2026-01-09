"""
file_handling.py
Module for reading and writing files with error handling.
"""

def read_file(filename: str) -> str:
    """
    Reads content from a file.
    
    Args:
        filename (str): Path to the file.
    
    Returns:
        str: Content of the file or error message.
    """
    try:
        with open(filename, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Unexpected error: {str(e)}"

def write_file(filename: str, content: str) -> str:
    """
    Writes content to a file.
    
    Args:
        filename (str): Path to the file.
        content (str): Text to write.
    
    Returns:
        str: Success or error message.
    """
    try:
        with open(filename, 'w') as f:
            f.write(content)
        return "File written successfully."
    except Exception as e:
        return f"Error writing file: {str(e)}"
