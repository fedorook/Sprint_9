"""
Random string generation utilities for test data.
"""
import random
import string


def generate_random_string(length):
    """Generate a random string of lowercase letters."""
    return ''.join(random.choices(string.ascii_lowercase, k=length))