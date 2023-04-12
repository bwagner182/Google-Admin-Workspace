"""
This file will hold my work with the Reftab API to allow for
better testing and code readability
"""

from reftab import ReftabClient

from pprint import pprint
from datetime import datetime
import os
import sys

import keys

# Set up API authorization
client = ReftabClient(  
    publicKey=keys.REFTAB_PUBLIC_KEY,
    secretKey=keys.REFTAB_SECRET_KEY
    )

def create_user_reftab(userinfo):
    """Create a new user account in Reftab for the employee"""
    print("Creating user account in Reftab")
    # Initialize the request body
    body = {
                "name" :  userinfo['fname'] + " " + userinfo['lname'], 
                "email" : userinfo['email_address'],
                "title" : userinfo['title'],
                "employeeId" : userinfo['email_address'],
                "details" : {}
            }

    if userinfo['test_mode'] == False:
        # Create the user account
        try:
            response = client.post('loanees', body)
        except:
            sys.exit("Error when creating the user in Reftab")

        if response['lnid'] and response['lnid'] != '':
            print("Reftab user creation SUCCESS")
            userinfo['reftab_resp'] = "success"
            return userinfo
        else:
            print("Reftab Error")
            # pprint(result, width=75)
            userinfo['reftab_resp'] = response
            return userinfo
    else:
        # Test mode enabled, store request in userinfo for display and debugging
        userinfo['reftab_request'] = body
        return userinfo

def search_users(username):
    try:
        response = client.get('loanees', query=username, limit=1)
    except:
        print("Error retrieving user search")
        sys.exit()

    if len(response) < 1:
        print("No users by that username")
    else:
        return response

def get_loans(userid=None, loan_id=None):
    if (userid):
        try:
            response = client.get('loans', loan_uid=str(userid))
        except HttpError as e:
            print("Error getting loans for user, suggest checking uid: " + str(userid))
            sys.exit()
    elif (loan_id):
        try:
            response = client.get('loans', loan_id=str(loan_id))
        except HttpError as e:
            pprint(e, width=80)
            sys.exit()


    try:
        response

        if len(response) < 1:
            print("No registered devices for that user")
        else:
            return response
    except TypeError:
        sys.exit("Unable to retrieve loans")

def get_asset(asset_id):
    response = client.get('assets', id=str(asset_id))

    return response

def update_asset(asset, status):
    if status == "term":
        asset['status'] = {
                            'color': '#ddec09',
                            'defaultVisibility': 0,
                            'loanability': 0,
                            'name': 'Needs shipped home'
                        }
        asset['statid'] = 65952
    response = client.put('assets', asset['aid'], body=asset)
    return response

def terminate_user(username):
    # print("searching users")
    user = search_users(username)[0]
    userid = user['lnid']
    # print("getting loans for user")
    loans = get_loans(userid=userid)

    for loan in loans:
        # os.system("clear")
        # pprint(loan)
        category = loan['categoryName']
        if "MacBook" in category or "iMac" in category:
            loan_id = loan['lid']

        if "MacBook" in category:
            asset_id = loan['aid']

    # Update device due date to TODAY at 5PM
    due_date = datetime.today().strftime('%Y-%m-%d') + "T22:00:00Z"
    # Update device status to "Needs shipped home"
    
    body = {
            'status': 'out',
            'notes': 'Employee terminated',
            'due': str(due_date)
            }

    # pprint(body)
    # update the loan status
    client.put('loans', id=str(loan_id), body=body)

    # update the asset status label
    asset = get_asset(asset_id)
    response = update_asset(asset, "term")

    print("User's device has been updated in Reftab")

    return response

