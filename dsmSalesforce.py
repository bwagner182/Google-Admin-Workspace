import keys
from salesforce_api import Salesforce


client = Salesforce(username=keys.SF_USERNAME_SANDBOX,
                    password=keys.SF_PASSWORD,
                    security_token=keys.SF_TOKEN_SANDBOX,
                    is_sandbox=True)


def get_user_id(email_address):
    userid = client.sobjects.query("SELECT Id FROM user WHERE email='"+email_address+"'")

    return userid[0]["Id"]
