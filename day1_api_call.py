# Import library to make HTTP requests (like Java's HttpClient)
import requests

# API endpoint (GitHub public API)
url = "https://api.github.com"

# Send GET request to the server
response = requests.get(url)

# Print HTTP status code (200 = success)
print("Status Code:", response.status_code)

# Print response data in JSON (dictionary-like object)
print("Response JSON:", response.json())
