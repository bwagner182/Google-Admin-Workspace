import keys
from salesforce_api import Salesforce
import requests


client = Salesforce(username=keys.SF_USERNAME_SANDBOX,
                    password=keys.SF_PASSWORD,
                    security_token=keys.SF_TOKEN_SANDBOX,
                    is_sandbox=True)

def get_user(email_address):
    user = client.sobjects.query("SELECT Id, name FROM user WHERE username='"+email_address+"'")[0]

    return user

def deactivate_user(user):
    response = client.sobjects.user.update(user['Id'], {"IsAtive": False})

    return response

def terminate_user(userinfo):
    user = get_user(userinfo['email_address'])
    killed = deactivate_user(user)

    return killed
