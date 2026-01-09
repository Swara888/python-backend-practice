import pytest
from file_handling import write_file, read_file

def test_write_and_read():
    write_file("test.txt", "Hello")
    content = read_file("test.txt")
    assert content == "Hello"

def test_read_nonexistent_file():
    result = read_file("nonexistent.txt")
    assert "Error: File not found" in result
