from keys import *

import requests
from requests.auth import HTTPBasicAuth

# API endpoint
url = "https://api.planningcenteronline.com/people/v2/people"

# Make the request with Basic Auth
response = requests.get(url, auth=HTTPBasicAuth(CLIENT_ID, SECRET))

# Print response
print(response.status_code)
print(response.json())  # Assuming the response is JSON