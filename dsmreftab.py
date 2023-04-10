"""
This file will hold my work with the Reftab API to allow for
better testing and code readability
"""

from reftab import ReftabClient

from pprint import pprint

import keys

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
	# Set up API authorization
	client = ReftabClient(	
		publicKey=keys.REFTAB_PRIVATE_KEY,
		secretKey=keys.REFTAB_SECRET_KEY
		)

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
