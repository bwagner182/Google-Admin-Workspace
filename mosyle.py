"""
This file will hold my work with the Mosyle API to allow for
better testing and code readability
"""

from pprint import pprint
import keys

import requests
import json
import base64


MOSYLE_API_BASE_URL = "https://businessapi.mosyle.com/v1"

def create_user_mosyle(userinfo):
    """
    Create a new user account in Mosyle
    userinfo    dict    user object

    Returns
    response    dict    user object from Mosyle
    userinfo    dict    user object (on test or fail)
    """
    print("Creating user account in Mosyle")

    # Set up authorization for the API
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

    if userinfo['test_mode'] == False:
        try:
            response = requests.post(MOSYLE_API_BASE_URL + "/users", json=body, headers=headers).json()
        except:
            sys.exit("There was an issue with the Mosyle request")
    
        # Make sure there are no other errors with the submission
        if response['status'] != 'OK' :
            userinfo['mosyle_resp'] = "fail"
            return userinfo
        else:
            # User successfully created
            print("Mosyle user creation SUCCESS")
            userinfo['mosyle_resp'] = "success"
            return userinfo

    elif userinfo['test_mode'] == True:
        # Test mode enabled, store mosyle request for display and debugging
        userinfo['mosyle_request'] = body
        return userinfo
