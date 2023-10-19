"""
This file will hold my work with the Reftab API to allow for
better testing and code readability
"""

from reftab import ReftabClient

from pprint import pprint
import datetime
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
        "name":  userinfo['fname'] + " " + userinfo['lname'],
        "email": userinfo['email_address'],
        "title": userinfo['title'],
        "employeeId": userinfo['email_address'],
        "details": {}
    }

    if userinfo['test_mode'] is False:
        # Create the user account
        try:
            response = client.post('loanees', body)
        except:
            userinfo['reftab_resp'] = "Error creating user"
            return userinfo

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


def search_users(userinfo):
    """
    Seach Reftab for user account by username
    username    str     any query, but username or email is best

    Return
    response    list    an array of user objects that match the search
    """
    try:
        response = client.get('loanees', query=userinfo['username'], limit=0)
    except:
        response = client.get('loanees', query=userinfo['email_address'], limit=0)

    if len(response) < 1:
        print("No users by that username")
    else:
        for user in response:
            if user['email'] != userinfo['email_address']:
                continue
            elif user['email'] == userinfo['email_address']:
                response = user
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
        except HTTPError as e:
            print("Error getting loans for user, suggest checking uid: " + str(userid))
            sys.exit()
    elif (loan_id):
        try:
            response = client.get('loans', loan_id=str(loan_id))
        except:
            pprint("Error getting loans", width=80)
            sys.exit()

    try:
        response

        if len(response) < 1:
            print("No registered devices for that user")
        else:
            return response
    except TypeError:
        sys.exit("Unable to retrieve loans")


def loan_device_list(loans):
    devices = []
    for loan in loans:
        devices.append(loan['title'])

    return devices


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
        asset['statid'] = 65952  # ID for status label in Reftab
        response = client.put('assets', asset['aid'], body=asset)
    else:
        response = "error"
    return response


def terminate_user(userinfo):
    """
    Used when terminating an employee, updates computer due date to today
    and changes the status label for the computer.
    username    str     username of the employee (ex: jsmith)

    Return (None)
    response    list    return the names of the devices on loan to the user
    """
    user = search_users(userinfo)

    # if len(users) > 1:
    #     for user in users:
    #         if user['email'] != userinfo['email_address']:
    #             continue
    #         elif user['email'] == userinfo['email_address']:
    #             users = user
    # elif len(user) == 0:
    #     sys.exit("No users matched the search, please correct the username")
    # else:
    #     user = user[0]

    # if user['name'].lower() != userinfo['fname'].lower() + " " + userinfo['lname'].lower():
    #     os.system("clear")
    #     print("The user account returned does not match, try searching by email? (y/n)")
    #     answer = input().strip().lower()

    #     if answer == "n":
    #         sys.exit("User account returned did not match given name")
    #     elif answer == "y":
    #         user = search_users(userinfo)[0]

    try:
        loans = get_loans(loan_id=user['lnid'])
    except KeyError:
        loans = get_loans(userid=user['uid'])

    try:
        devices = []
        for loan in loans:
            devices.append(loan['title'])
            category = loan['categoryName']
            if "MacBook" in category or "iMac" in category:
                loan_id = loan['lid']

            if "MacBook" in category:
                asset_id = loan['aid']

            if "iMac" in category:
                status = "in"
                asset_id = loan['aid']
            else:
                status = "out"

    except TypeError:
        print("Sorry, no registered devices for this user")
        devices = ""
        # exit the function and move on
        return devices

    # Update device due date to TOMORROW at 5PM
    due_date = datetime.datetime.today() + datetime.timedelta(days=1)
    due_date = due_date.strftime('%Y-%m-%d')
    due_date = due_date + "T22:00:00Z"
    # Update device status to "Needs shipped home"

    body = {
        'status': status,
        'notes': 'Employee terminated',
        'due': str(due_date)
    }

    # update the loan status
    if userinfo['test_mode'] is False:
        client.put('loans', id=str(loan_id), body=body)

    # update the asset status label
    asset = get_asset(asset_id)

    if userinfo['test_mode'] is False:
        response = update_asset_status(asset, "term")
    else:
        response = ""

    if response != "error":
        print("User's device has been updated in Reftab")
    else:
        print("There was an issue, I'm sorry. Please check the user and")
        print("assigned devices in reftab")

    return devices

def get_manager(userinfo):
    user = search_users(userinfo)
    try:
        if user['details']['Manager'] is not None:
            manager = user['details']['Manager']
    except KeyError:
        manager = None

    return manager

def update_manager(userinfo):
    user = search_users(userinfo)
    try:
        manager_old = user['details']['Manager']
    except KeyError:
        manager_old = None

    if userinfo['manager'] is not None and userinfo['manager'] != '':
        manager_new = userinfo['manager']
    else:
        manager_new = None

    if manager_new is not None and manager_old != manager_new:
        user['details']['Manager'] = manager_new

        try:
            response = client.put('subusers', str(user['uid']), user)
            return response
        except:
            userinfo['reftab_resp'] = "Error updating user"
            return userinfo

def all_loans():
    loans = []
    offset = 0
    more = True
    while more:
        results = client.get("loans", offset=offset)
        if results:
            for loan in results:
                loans.append(loan)
            if len(results) == 20:
                offset += len(client.get("loans", offset=offset))
            elif len(results) < 20:
                more = None
        else:
            more = None
    return loans

