import keys
from salesforce_api import Salesforce
import requests


client = Salesforce(username=keys.SF_USERNAME_PROD,
                    password=keys.SF_PASSWORD,
                    security_token=keys.SF_TOKEN_PROD
                    )

def get_user(email_address):
    """query the Salesforce database
    
    searches the Salesforce users for the email address given
    
    Args:
        email_address (string): email address of the terminated user
    
    Returns:
        dict: user object from Salesforce
    """
    user = client.sobjects.query("SELECT Id, name FROM user WHERE username='"+email_address+"'")[0]

    return user

def deactivate_user(user):
    """deactivate the user
    
    set's the user's "IsActive" flag to False
    
    Args:
        user (dict): user object from Salesforce
    
    Returns:
        boolean: result of the deactivation call
    """
    response = client.sobjects.user.update(user['Id'], {"IsActive": False})

    return response

def terminate_user(userinfo):
    """terminate user
    
    wraps the get and deactivate fundtions to one call
    
    Args:
        userinfo (dict): information from the terminated user. email_address required
    
    Returns:
        boolean: result of the deactivation
    """
    user = get_user(userinfo['email_address'])
    killed = deactivate_user(user)
    if killed == True:
        print("User deactivated in Salesforce")
    else:
        print("Issue dativating user in Salesforce, please update manually")

    return killed
