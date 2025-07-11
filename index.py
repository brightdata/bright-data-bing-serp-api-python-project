#!/usr/bin/env python3
"""
Example of using Bright Data's SERP API
This simple script demonstrates how to make a search engine request through Bright Data SERP API
"""

import os
import requests
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration - Update these values
CONFIG = {
    # Step 1: Get your API Key here: https://brightdata.com/cp/setting/users
    'api_key': os.getenv('BRIGHT_DATA_API_KEY', 'YOUR_API_KEY'),
    # Step 2: Get your SERP zone here: https://brightdata.com/cp/zones
    'zone': 'serp_api1',
    # Step 3: Set your Bing search engine query with URL
    'search_engine_query_url': 'https://www.bing.com/search?q=pizza'
    # Step 4: Run `python index.py` command on terminal
}

def fetch_with_bright_data():
    """
    Makes a request to the Bright Data SERP API
    Returns the API response data
    """
    try:
        # Input validation
        if CONFIG['api_key'] == 'YOUR_API_KEY':
            print('⚠️ Please set your actual API key before making requests')
        
        print(f"🔄 Fetching {CONFIG['search_engine_query_url']} through Bright Data SERP API...")
        
        response = requests.post(
            'https://api.brightdata.com/request',
            headers={
                'Authorization': f"Bearer {CONFIG['api_key']}",
                'Content-Type': 'application/json'
            },
            json={
                'zone': CONFIG['zone'],
                'url': CONFIG['search_engine_query_url'],
                'format': 'json'
            }
        )
        
        # Handle HTTP errors
        if not response.ok:
            raise Exception(f"HTTP error! Status: {response.status_code}")
        
        data = response.json()
        print('✅ Request successful!')
        return data
        
    except Exception as error:
        print(f'❌ Error: {error}')
        raise error  # Re-raise to allow further handling if needed

# Execute the function and handle the response
if __name__ == "__main__":
    try:
        data = fetch_with_bright_data()
        print('📊 Response data:', json.dumps(data, indent=2))
    except Exception:
        # Error already logged in the function
        exit(1)  # Exit with error code for scripts/automation