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
    """
    Create a new user account in Reftab for the employee
    userinfo    dict    user object

    Returns
    userinfo    dict    user object
    """
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
    """
    Seach Reftab for user account by username
    username    str     any query, but username or email is best

    Return
    response    list    an array of user objects that match the search
    """
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
    """ 
    Get individual (loan_id) or all loans (userid)
    userid      int/str     loanee ID in Reftab
    loan_id     int/str     loan ID in Reftab

    Returns
    loan(s)     if using userid, you may receive multiple results
    """
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
    """
    Get the asset object from the Reftab API
    asset_id    int/str     Asset ID in Reftab

    Return
    response    dict        Asset object from Reftab
    """
    response = client.get('assets', id=str(asset_id))

    return response

def update_asset_status(asset, status):
    """
    Updates the status label of a given asset
    asset       dict    asset object from Reftab
    status      str     this should be one of the available labels (more to be added)

    Return
    response    dict    asset object (or error)
    """
    if status == "term":
        asset['status'] = {
                            'color': '#ddec09',
                            'defaultVisibility': 0,
                            'loanability': 0,
                            'name': 'Needs shipped home'
                        }
        asset['statid'] = 65952 # ID for status label in Reftab
    response = client.put('assets', asset['aid'], body=asset)
    return response

def terminate_user(userinfo):
    """
    Used when terminating an employee, updates computer due date to today
    and changes the status label for the computer.
    username    str     username of the employee (ex: jsmith)

    Return (None)
    response    dict    this is the response from the API when updating the asset
                        (not the loan due date, but the due date will be shown on success)
    """
    user = search_users(userinfo['username'])

    if len(user) > 1:
        sys.exit("Multiple users match that search, please provide the unique username")
    elif len(user) == 0:
        sys.exit("No users matched the search, please correct the username")
    else:
        user = user[0]

    if user['name'].lower() != userinfo['fname'] + " " + userinfo['lname']:
        os.system("clear")
        print("The user account returned does not match, try searching by email? (y/n)")
        answer = input().strip().lower()

        if answer == "n":
            sys.exit("User account returned did not match given name")
        elif answer == "y":
            user = search_users(userinfo['email_address'])[0]

    try:
        userid = user['lnid']
    except KeyError:
        sys.exit("No matching username, check the spelling")

    
    loans = get_loans(userid=userid)

    for loan in loans:
        category = loan['categoryName']
        if "MacBook" in category or "iMac" in category:
            loan_id = loan['lid']

        if "MacBook" in category:
            asset_id = loan['aid']

        if "iMac" in category:
            status = "in"
        else:
            status = "out"

    # Update device due date to TODAY at 5PM
    due_date = datetime.today().strftime('%Y-%m-%d') + "T22:00:00Z"
    # Update device status to "Needs shipped home"
    
    body = {
            'status': status,
            'notes': 'Employee terminated',
            'due': str(due_date)
            }

    # update the loan status
    if userinfo['test_mode'] == False:
        client.put('loans', id=str(loan_id), body=body)

    # update the asset status label
    asset = get_asset(asset_id)
    
    if userinfo['test_mode'] == False:
        response = update_asset_status(asset, "term")

    print("User's device has been updated in Reftab")

    # Uncomment for debugging purposes or to see the asset response
    # return response

