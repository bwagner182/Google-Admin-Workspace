"""Used to interface with the Facebook Business Manager API

This is the Drive Social Media softweare written to interact
with the Facebook Business Manager API in order to automate
admin activities - specifically removing users' access at the
time of employee termination.
"""

import json
import keys
import os
import requests
import sys

from pprint import pprint

FB_API_VERSION = "v16.0"
FB_API_ADDRESS = "https://graph.facebook.com/"

def get_access_token(businessManager):
    """Authorize the app

    Retrieve an access token from the Meta API to authorize future method calls

    Args:
        businessManager (str): this is a key name from keys.BUSINESS_IDS

    Returns:
        access_token (str): access token to be used for future api method calls
    """
    uri = "https://graph.facebook.com/oauth/access_token"
    uri = uri + "?client_id=" + keys.BUSINESS_IDS[businessManager]['app_id']
    uri = uri + "&client_secret=" + keys.BUSINESS_IDS[businessManager]['app_secret']
    uri = uri + "&grant_type=client_credentials"

    response = requests.get(uri).json()

    try:
        access_token = response['access_token']
    except KeyError:
        print("response did not have an access token for you")
    return access_token

def get_business_manager_admins(city):
    """Pull list of admins for a specified business manager

    This will take the input from the function and grab the associated
    data from the keys file to hit the API

    Args:
        city (str): string matching a key from keys.BUSINESS_IDS

    Returns:
        response (dict): list of users for the business manager account
    """
    access_token = get_access_token(city)

    uri =  FB_API_ADDRESS + FB_API_VERSION + "/"
    uri = uri + keys.BUSINESS_IDS[city]['business_id'] + "/business_users"
    uri = uri + "?access_token=" + access_token

    response = requests.get(uri).json()

    try:
        if response['error'] is not None:
            print(response['error']['message'])
            sys.exit()
    except KeyError:
        pass

    try:
        if response['data'] is not None:
            return response['data']
    except KeyError:
        print("Error getting users")
        print(response)
        return response

def find_fb_admin(users, name):
    """Search user list for specified user name

    Takes the list of users from a business manager and returns the
    user object

    Args:
        users (dict): list of users from the Meta API
        name (str): name of the user to look for

    Returns:
        emp (dict): user object from the Meta API
    """
    users = users['data']
    emp = dict()
    for user in users:
        if user['name'] == name:
            emp = user
            break

    return emp

def business_manager_user_delete(user, businessManager):
    """Delete specified user from specified busines manager account

    This will take in a user object from Meta and remove them from
    Business Manager in Meta

    Args:
        user (dict): user object from the Meta API
        businessManager (str): this is the city name reference for the
            business manager account

    Returns:
        response (dict): response from the Meta API
    """

    access_token = get_access_token(businessManager)
    uri = FB_API_ADDRESS + FB_API_VERSION + "/"
    uri = uri + user['id']

    response = requests.delete(uri).json()
    return response

def fbdelete(userinfo):
    """Delete the user from business manager accounts
    
    This function will initiate all the required steps to
    remove a user from Facebook Business Manager
    
    Args:
        userinfo (dict): user object with required fields

    Returns:
        resp (list): list of responses from the Meta API
    """
    name = userinfo['fname'] + " " + userinfo['lname']

    for key in keys.BUSINESS_IDS:
        # get Facebook Business Manager Account Admins
        users = get_business_manager_admins(key)
        # search the accounts for the user being deleted
        user = find_fb_admin(users, name)

        # delete the user
        resp = []
        resp.append(business_manager_user_delete(user))
        print("User removed from Business Manager " + key)

    return resp

