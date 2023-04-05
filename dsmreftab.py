"""
This file will hold my work with the Reftab API to allow for
better testing and code readability
"""

from reftab import ReftabClient

from pprint import pprint

import keys

def create_user_reftab(userinfo):
	body = {
				"name" :  userinfo['fname'] + " " + userinfo['lname'], 
				"email" : userinfo['email_address'],
				"title" : userinfo['title'],
				"employeeId" : userinfo['email_address'],
				"details" : {}
			}

	client = ReftabClient(	
		publicKey=keys.REFTAB_PRIVATE_KEY,
		secretKey=keys.REFTAB_SECRET_KEY
		)

	response = client.post('loanees', body)

	if response['lnid'] and response['lnid'] != '':
		print("Reftab user creation SUCCESS")
		return True
	else:
		print("Reftab Error")
		# pprint(result, width=75)
		return response
