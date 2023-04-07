"""
This file will hold my work with the Reftab API to allow for
better testing and code readability
"""

from reftab import ReftabClient

from pprint import pprint

import keys

def create_user_reftab(userinfo):
	print("Creating user account in Reftab")
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

	if userinfo['test_mode'] == False:
		response = client.post('loanees', body)

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
		userinfo['reftab_request'] = body
		return userinfo
