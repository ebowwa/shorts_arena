from resemble import Resemble
import os

def get_api_key():
    # Retrieve API key from environment variable
    api_key = '6mkg97PzKz3uezBonSIepAtt'
    if not api_key:
        raise ValueError("RESEMBLE_API_KEY not set in environment variables")

    return api_key

def initialize_resemble_client():
    # Initialize the Resemble client with the API key
    api_key = get_api_key()
    Resemble.api_key(api_key)