#! /usr/bin/env python
"""Sample of Get Interface
Using Basic Authentication
"""

# Import libraries
import requests
import sys

# Use self signed certs
requests.packages.urllib3.disable_warnings()

# Credentials
USER = 'developer'
PASS = 'C1sco12345'

# URL for GET request
url= "https://ios-xe-mgmt.cisco.com:9443/restconf/data/interfaces/interface=GigabitEthernet1"

# Set yang+jsonas the data formats
headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}
           
# Run GET
response = requests.get(url, auth=(USER, PASS),headers=headers, verify=False)

# Print results
print('Status Code:' + str(response.status_code))
print('Response Text:' + response.text)
