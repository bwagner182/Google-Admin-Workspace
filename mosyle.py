"""
This file will hold my work with the Mosyle API to allow for
better testing and code readability
"""

from pprint import pprint
import keys

import requests
import json
import base64

import ssl
ssl._create_default_https_context = ssl._create_unverified_context


MOSYLE_API_BASE_URL = "https://businessapi.mosyle.com/v1"

def create_user_mosyle(userinfo):
	auth = keys.MOSYLE_USERNAME + ":" + keys.MOSYLE_PASSWORD
	auth = auth.encode("ascii")
	auth = base64.b64encode(auth)
	auth = auth.decode("ascii")
	headers = {
	'Authorization':'Basic ' + auth,
	'Content-Type':'application/json',
	'accesstoken': keys.MOSYLE_API_TOKEN
	}

	# Create the body of the request (refer to mosyle docs for body composition)
	# More commands available for other needs later
	body = {
	    "operation": "create_user",
	    "user_id": userinfo['email_address'],
    	"name": userinfo['fname'] + " " + userinfo['lname'],
    	"type": "ENDUSER"
	}

	response = requests.post(MOSYLE_API_BASE_URL + "/users", json=body, headers=headers)
	# resp_json = response.json()
	if response['status'] != 'OK' :
	 	# print("Error from Mosyle API:")
	 	# print(result['error'])
	 	return result['error']
	else:
	 	print("Mosyle user creation SUCCESS")
	 	return True